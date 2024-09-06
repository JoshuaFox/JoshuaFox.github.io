#!/usr/bin/env bash
set -x
set -e

./googledocs/download-from-google-docs-and-process.sh
git add yiddish/*.md
git commit -am "from Google Docs"
git push origin HEAD:master