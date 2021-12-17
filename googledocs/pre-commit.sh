#!/usr/bin/env bash
set -e
set -u

python3 -m venv ./googledocs/venv
source ./googledocs/venv/bin/activate
pip3 install -r ./googledocs/requirements.txt
python3 ./googledocs/export-yiddish-website-docs.py
python3  ./googledocs/fix-googledocs-html.py