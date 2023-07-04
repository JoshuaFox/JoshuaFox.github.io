# coding utf-8
import os
import re
import urllib.parse
from pathlib import Path

from bs4 import BeautifulSoup


def out_folder():
    return os.path.abspath("./yiddish")


def folder_in():
    return os.path.abspath("./_yiddish_from_google_docs")


def insert_videoembed(html_filepath):
    if "װוּהין" in html_filepath:
        with open(html_filepath, "r") as f:
            data1 = f.read()
            # example https://drive.google.com/file/d/1rmem-G9-Z5_ElgkcATCdZsHaCQA_daqP/preview
            data2 = re.sub(
                r"\*VIDEOEMBED(.+?)ENDVIDEOEMBED\*",
                r'<iframe src="\1" width="640" height="480" allow="autoplay"></iframe>',
                data1,
            )
        with open(html_filepath, "wt") as fout:
            if data1 != data2:
                fout.write(data2)
                print("insert_videoembed wrote", html_filepath)


def clean_missing_font_link(filename):
    if "הײַנט בין" in filename:
        with open(filename, "r") as f:
            data = f.read()
            inserted = data.replace(
                "@import url(https://themes.googleusercontent.com/fonts/css?kit=wAPX1HepqA24RkYW1AuHYA);",
                "",
            )
        if inserted != data:  # Do this after filehandle for read is closed
            with open(filename, "wt") as fout:
                fout.write(inserted)
                print("remove_missing_font_link wrote", filename)
        else:
            print("remove_missing_font_link found nothing in", filename)


def clean_half_spaces(filename):
    if "הירהורים" in filename:
        with open(filename, "r") as f:
            data = f.read()
            inserted = re.sub(r"(?<![A-Za-z0-9])Q(?![A-Za-z0-9])", "&#x202F;", data)
        if inserted != data:  # Do this after filehandle for read is closed
            with open(filename, "wt") as fout:
                fout.write(inserted)
                print("clean_half_spaces wrote", filename)
        else:
            print("clean_half_spaces found nothing in", filename)


def add_analytics(filename):
    ua = "UA-24142341-1"
    analytics = f"""
        <!-- Google Analytics -->
            <script>
                (function(i,s,o,g,r,a,m){{i['GoogleAnalyticsObject']=r;i[r]=i[r]||function(){{
                (i[r].q=i[r].q||[]).push(arguments)}},i[r].l=1*new Date();a=s.createElement(o),
                m=s.getElementsByTagName(o)[0];a.async=1;a.src=g;m.parentNode.insertBefore(a,m)
                }})(window,document,'script','//www.google-analytics.com/analytics.js','ga');
                ga('create', '{ua}', 'auto');
                ga('send', 'pageview');
            </script>
            <!-- End Google Analytics -->
        """

    inserted = None
    if filename.endswith(".html"):
        with open(filename, "r") as f:
            data = f.read()

            if ua in data:
                print("Did not add  Google Analytics in", filename)
            else:
                inserted = data.replace("</body>", analytics + "\n</body>")
                print("Added Google Analytics in", filename)

        if inserted:  # Do this after filehandle for read is closed
            with open(filename, "wt") as fout:
                fout.write(inserted)
                print("add_analytics wrote", filename)


def add_rtl(filename):
    rtl_style = "body{direction:rtl}</style>"

    with open(filename, "r") as f:

        def replace_rtl_align_style():
            data1 = f.read()
            data2 = data1.replace(";text-align:left", "")
            if data2 != data1:
                print("Removed text-align:left in", filename)
            else:
                print("Did not remove text-align:left in", filename)
            return data2

        def add_rtl_div(data2):
            if rtl_style not in data2:
                data3 = data2.replace("</style>", rtl_style)
                print("Inserted RTL in", filename)
            else:
                data3 = data2
                print("Did not insert RTL in", filename)
            return data3

        with_rtl_style = replace_rtl_align_style()

        with_rtl_div = add_rtl_div(with_rtl_style)

    # Do this after filehandle for read is closed
    with open(filename, "wt") as fout:
        fout.write(with_rtl_div)
        print("add_rtl wrote", filename)


def generate_md(html_filepath, folder_out):
    title = os.path.basename(html_filepath).split(".")[:-1][0]
    if not re.match(r".*[א-ת]+.*", title):
        print("Not making markdown from", html_filepath)
    else:
        md_filepath = folder_out + "/" + title + ".md"

        if os.path.exists(md_filepath):
            os.remove(md_filepath)
            print("Deleted", md_filepath)
        else:
            print("Markdown", md_filepath, "does not exist")

        md_header = f"""---
layout: page
title: "{title}"
subtitle:
tags: [ yiddish]
css: yiddish
lang: yi
---

"""
        with open(html_filepath, "r") as f:
            html = f.read()

        md_header += html

        with open(md_filepath, "w") as fout:
            fout.write(md_header)
            print("generate_md wrote", md_filepath)


def replace_img(html_filepath):
    return  # The below is not doing what it looks like, because img urls are long GUIDs
    if html_filepath.endswith("/דער פֿראָסט־ריזעס טאָכטער.html"):
        with open(html_filepath, "r") as f:
            data = f.read()
            inserted = data.replace('src="images/image1.png"', 'src="/img/conan.jpg"')

        if data != inserted:
            print("changed image tag in Conan story")

        with open(html_filepath, "wt") as fout:
            fout.write(inserted)
            print("replace_image wrote", html_filepath)


def fix_link(html_filepath):
    return
    # TODO not clear that this does anything or that it is needed.
    def fix_google_redirects_once(data, html_filepath):

        # Google-redirects send a browser pretty fast to the right place, with no interstitial
        return
        # # THere is also some query-string junk, but just leaving that.
        # intro_s = 'https://www.google.com/url?q=https://'
        # try:
        #     idx = data.index(intro_s)
        # except ValueError:
        #     return data
        # idx_end_of_real_url = data.index('&amp;sa', idx)
        # idx_end_of_link = data.index('"', idx_end_of_real_url)
        # before = data[0: idx]
        # real_url_encoded = "https://" + data[idx + len(intro_s):idx_end_of_real_url]
        # real_url = urllib.parse.unquote(real_url_encoded)
        # rest = data[idx_end_of_link:]
        # replaced = before + real_url + rest
        # print("replaced link", real_url, "in", html_filepath)
        # return replaced
        # # else:
        # #    print("Did not replace link",real_url,"in", html_filepath)
        # #    return data

    while True:
        with open(html_filepath, "r") as f:
            data = f.read()
        replaced = fix_google_redirects_once(data, html_filepath)
        if replaced == data:
            break
        else:
            with open(html_filepath, "wt") as fout:
                fout.write(replaced)
            print("fix_link wrote", html_filepath)


def pretty_print(html_filepath):
    with open(html_filepath, "r") as f:
        data = f.read()
        soup = BeautifulSoup(data)  # make BeautifulSoup
        prettyHTML = soup.prettify()  # prettify the html
    with open(html_filepath, "wt") as fout:
        fout.write(prettyHTML)


def insert_gist(html_filepath):
    with open(html_filepath, "r") as f:
        data1 = f.read()
        data2 = re.sub(
            r"\*GIST([0-9a-f]+)\*",
            r'<script src="https://gist.github.com/JoshuaFox/\1.js"></script>',
            data1,
        )
    with open(html_filepath, "wt") as fout:
        fout.write(data2)
        print("insert_gist wrote", html_filepath)


def main():
    os.chdir(Path(Path(__file__).parent.absolute()).parent.absolute())
    assert (
        "_site" not in os.getcwd()
    ), "Do not run script in _site, which is meant for generated content"
    for file in os.listdir(folder_in()):
        html_filepath = folder_in() + "/" + file
        if html_filepath.endswith(".html"):
            insert_gist(html_filepath)
            clean_missing_font_link(html_filepath)
            insert_videoembed(html_filepath)
            clean_half_spaces(html_filepath)
            add_analytics(html_filepath)
            add_rtl(html_filepath)
            replace_img(html_filepath)
            fix_link(html_filepath)
            # pretty_print(html_filepath)
            generate_md(html_filepath, out_folder())


if __name__ == "__main__":
    main()
