#!/usr/bin/env bash
set -x
set -e
./preprocess.sh
git commit -am "from Google Docs"
git push origin HEAD:master
