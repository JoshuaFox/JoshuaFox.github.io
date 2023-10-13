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
startexport=$(date +%s)
python3 ./googledocs/export-yiddish-website-docs.py
endexport=$(date +%s)
echo "Export time is: $((endexport-startexport)) sec"

python3  ./googledocs/fix-googledocs-html.py
python3 ./googledocs/subtitles-right-to-left.py ./yiddish/edit-this-one-where-no-man-yiddish.srt ./yiddish/where-no-man-yiddish.srt
endfixup=$(date +%s)
echo "download-from-google-docs-and-process: $((endfixup-startexport)) sec"
