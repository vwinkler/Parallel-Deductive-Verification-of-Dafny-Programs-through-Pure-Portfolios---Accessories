#!/bin/sh

for benchmark in "$@"
do
    basename=${benchmark##*/}
    (set -x; dafny /xml:"${basename%.*}.xml" $benchmark)
done
