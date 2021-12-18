#!/usr/bin/env bash
set -e
set -u

# Run in root dir./

source ./googledocs/virtual_env/bin/activate
pip3 install -r ./googledocs/requirements.txt
python3 ./googledocs/export-yiddish-website-docs.py
python3  ./googledocs/fix-googledocs-html.py