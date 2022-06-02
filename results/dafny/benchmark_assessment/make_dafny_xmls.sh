#!/bin/sh

for benchmark in "$@"
do
    basename=${benchmark##*/}
    filename=$(echo "${basename%.*}" | # slugify
        iconv -t ascii//TRANSLIT |
        sed -r s/[^a-zA-Z0-9]+/-/g |
        sed -r s/^-+\|-+$//g |
        tr A-Z a-z).xml
    
    if [ ! -f $filename ]
    then
        (set -x; timeout 600 dafny /xml:"$filename" /compile:0 $benchmark)
    else
        echo "skipping $filename"
    fi
done
