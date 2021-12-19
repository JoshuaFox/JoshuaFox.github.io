#!/usr/bin/env bash
set -e
set -u
set -x
SCRIPT_DIR=$( cd -- "$( dirname -- "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
PARENT_DIR="$(dirname "$SCRIPT_DIR")"

if [[ $PWD != "$PARENT_DIR" ]]; then
    echo "Please run this script from the parent directory of the script."
    exit 1
fi

source ./googledocs/virtual_env/bin/activate
pip3 install -r ./googledocs/requirements.txt
python3 ./googledocs/export-yiddish-website-docs.py
python3  ./googledocs/fix-googledocs-html.py