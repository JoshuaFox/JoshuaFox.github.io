#!/usr/bin/env bash
set -x
set -e
./googledocs/download-from-google-docs-and-process.sh
git commit -am "from Google Docs"
git push origin HEAD:master
https://joshuafox.com/yiddish/װו%D6%BCהין%20קײנער%20איז%20פֿרי%D6%B4ער%20נישט%20געפֿאָרן/git