#!/bin/sh

for benchmark in "$@"
do
    basename=${benchmark##*/}
    filename=${basename%.*}.xml
    if [ ! -f $filename ]
    then
        (set -x; dafny /xml:"$filename" /compile:0 $benchmark)
    else
        echo "skipping $filename"
    fi
done
