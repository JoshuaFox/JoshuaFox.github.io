# coding utf-8

import os
import os.path
import shutil
import sys
from pathlib import Path

import os
import requests
import backoff

from google.auth.transport.requests import Request  
import googleapiclient.errors
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
import os
import requests
from google.auth.transport.requests import Request  # Used to refresh token if needed
import googleapiclient.errors
import backoff

WEBSITE_YIDDISH_DOCS_GDRIVE_FOLDER = "1Hvb0MpR91LOHcb6SbhB1-Hxih8W_07Ba"


def download_dir():
    return os.path.abspath("./_yiddish_from_google_docs")


# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/drive.readonly"]


def token_json():
    return credentials_dir() + "/" + "token.json"


def credentials_json():
    return credentials_dir() + "/" + "credentials.json"


def credentials_dir():
    home = str(Path.home())
    return home + "/" + ".googledrive"


def remake_download_dir():
    try:
        shutil.rmtree(download_dir())
    except FileNotFoundError:
        pass
    os.mkdir(download_dir())


def _backoff_hdlr(details):
    print(
        "Backing off {wait:0.1f} seconds after {tries} tries "
        "calling function {target}. "
        "Exception: {exception}".format(**details)
    )




@backoff.on_exception(
    backoff.expo, (googleapiclient.errors.HttpError,), on_backoff=_backoff_hdlr
)
def export_html(service, doc_id):
    # Ensure we fetch 'exportLinks' in the metadata
    doc_metadata = service.files().get(fileId=doc_id, fields="id, name, exportLinks").execute()
    name = doc_metadata["name"]

    dest_directory = download_dir()
    base_filename = os.path.join(dest_directory, name)
    
    html_content = None

    try:
        # Attempt standard API export
        html_content = (
            service.files().export(fileId=doc_id, mimeType="text/html").execute()
        )
    except googleapiclient.errors.HttpError as http_ex:
        # Check for various "too large" error messages (API sometimes varies wording)
        error_msg = str(http_ex).lower()
        if "too large" in error_msg:
            print(f"'{name}' is too large for standard API export. Attempting direct download link...")
            
            # 1. Extract the specific link for HTML
            export_links = doc_metadata.get("exportLinks", {})
            download_link = export_links.get("text/html")

            if not download_link:
                print(f"No HTML export link available for {doc_id}")
                return

            # 2. Retrieve and Validate Credentials
            creds = service._http.credentials
            if not creds.valid:
                creds.refresh(Request())

            # 3. Download manually using requests with the Bearer token
            headers = {"Authorization": f"Bearer {creds.token}"}
            response = requests.get(download_link, headers=headers)

            if response.status_code == 200:
                html_content = response.content
            else:
                print(f"Direct download failed: {response.status_code} - {response.text}")
                return
        else:
            # Re-raise if it's a different kind of error (e.g., 404, 500)
            raise http_ex

    # Save the content if we successfully retrieved it via either method
    if html_content:
        with open(base_filename + ".html", "wb") as f:
            f.write(html_content)
            print("Exported", name)


def iterate(service):
    results = (
        service.files()
        .list(
            pageSize=100,
            q=f'"{WEBSITE_YIDDISH_DOCS_GDRIVE_FOLDER}" in parents',
            fields="nextPageToken, files(id)",
        )
        .execute()
    )
    items = results.get("files", [])
    print("Exporting to", download_dir())
    for item in items:
        export_html(service, item["id"])
    print("Done, exported", len(items), "files")
 

def authenticate():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.

    if os.path.exists(token_json()):
        if Path(token_json()).read_text().strip() == "":
            print("Deleting empty file", token_json())
            os.remove(token_json())
        else:
            creds = Credentials.from_authorized_user_file(token_json(), SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            do_refresh = True
            while do_refresh:
                try:
                    creds.refresh(Request())
                except Exception as e:
                    if "google.auth.exceptions.RefreshError" in str(type(e)):
                        try:
                            os.remove(token_json())
                        except FileNotFoundError:
                            pass
                        else:
                            print("Removed", token_json())

                            print(
                                """
                            ************ ************ ************
                            If you see this message, then probably you see above 
                            "Removed ...token.json" and  the  processing has stopped.
                            Next steps:
                            * Open the browser for the relevant Google account
                            * Kill this process and rerun
                            * Validate in the browser when asked.
                                 * Be sure to choose "Continue" even though it is the *non-default* option.
                            ************ ************ ************               
                            """
                            )
                            python = sys.executable
                            os.execl(python, python, *sys.argv)  # *Replaces* corrent pr

                        do_refresh = True
                else:
                    do_refresh = False
        else:

            flow = InstalledAppFlow.from_client_secrets_file(credentials_json(), SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(token_json(), "w") as token:
            token.write(creds.to_json())
    return creds


def main():
    remake_download_dir()
    iterate(make_service())


def make_service():
    creds = authenticate()
    service = build("drive", "v3", credentials=creds)
    return service


if __name__ == "__main__":

    os.chdir(Path(Path(__file__).parent.absolute()).parent.absolute())
    assert (
        "_site" not in os.getcwd()
    ), "Do not run script in _site, which is meant for generated content"
    main()
