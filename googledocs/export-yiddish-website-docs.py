# coding utf-8

import os.path
import shutil
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

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


def export_html(service, doc_id):
    html_content = (
        service.files().export(fileId=("%s" % doc_id), mimeType="text/html").execute()
    )
    doc = service.files().get(fileId=doc_id).execute()
    name = doc["name"]

    with open(download_dir() + "/" + name + ".html", "wb") as f:
        f.write(html_content)
        print('Exported "%s"' % name)


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
    print(
        "",
        "*" * 30,
        "\n",
        "*" * 30,
        '\nIf you see "Removed ...token.json" and then the  processing stops,\n'
        "you may need to kill and rerun, validating in the browser when asked.\n"
        "Make sure that the Google account is correct (joshuatfox@gmail.com).\n"
        'Be sure to choose "Continue" even though it is given as the *non-default* option.\n',
        "*" * 30,
        "\n",
        "*" * 30,
    )

    os.chdir(Path(Path(__file__).parent.absolute()).parent.absolute())
    assert (
        "_site" not in os.getcwd()
    ), "Do not run script in _site, which is meant for generated content"
    main()
