#!/usr/bin/python3
#coding utf-8
import os
import re
def add_analytics_one_file(filename):
    ua = 'UA-24142341-1'
    analytics = \
        f"""
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
        with open(filename, 'r') as f:
            data = f.read()

            if ua in data:
                print('Did not add  Google Analytics in', filename)
            else:
                inserted = data.replace("</body>", analytics + "\n</body>")
                print('Added Google Analytics in', filename)

        if inserted:  # Do this after filehandle for read is closed
            with open(filename, 'wt') as fout:
                fout.write(inserted)


def add_rtl_one_file(filename):
    rtl_style = "body{direction:rtl}</style>"

    with open(filename, 'r') as f:
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
    with open(filename, 'wt') as fout:
        fout.write(with_rtl_div)


def generate_md_one_file(html_filepath, folder_out):
    title = os.path.basename(html_filepath).split('.')[:-1][0]
    if not re.match(r'.*[א-ת]+.*', title):
        print('Not making markdown from', html_filepath)
    else:
        md_filepath = folder_out+"/"+title+ '.md'
        if os.path.exists(md_filepath):
            os.remove(md_filepath)
            print('Deleted', md_filepath)
        else:
            print('Markdown', md_filepath, "does not exist")

        md_header = \
            f"""---
layout: page
title: "{title}"
subtitle:
tags: [ yiddish]
---

"""
        with open(html_filepath, 'r') as f:
            html = f.read()

        md_header += html

        with open(md_filepath, 'w') as fout:
            fout.write(md_header)
            print("Wrote", md_filepath)

folder_out= "./yiddish"
folder_in= "./_yiddish_from_google_docs"

for file in os.listdir(folder_in):
    html_filepath = folder_in+ '/' + file
    if html_filepath.endswith(".html")  :
     add_analytics_one_file(html_filepath)
     add_rtl_one_file(html_filepath)
     generate_md_one_file(html_filepath, folder_out)
