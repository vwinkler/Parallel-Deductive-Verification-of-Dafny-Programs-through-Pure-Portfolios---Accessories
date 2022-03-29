#!/bin/sh

if [ "$#" -lt 1 ]; then
    echo "Illegal number of parameters"
    exit
fi

for filename in "$@"
do
    cat $filename | sed -r "s/^./$filename\t&/g"
done | sort --key=3 --numeric-sort --reverse | column --table
