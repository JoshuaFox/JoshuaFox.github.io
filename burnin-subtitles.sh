#!/usr/bin/env bash
SUBTITLES=$(pwd)/yiddish/where-no-man-yiddish.srt

pushd ../../../Desktop ||exit

ffmpeg -i WhereNoMan.m4v -vf subtitles=${SUBTITLES}   burned-in-subtitles-WhereNoMan.m4v
popd ||exit


