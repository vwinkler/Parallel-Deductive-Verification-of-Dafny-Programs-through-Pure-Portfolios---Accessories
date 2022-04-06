#!/bin/sh

files=$(cat)
numfiles=$(echo "$files" | wc -l)

echo "$files" |
    while read -r file
    do
        timeout 3s dafny /compile:0 $file > /dev/null 2> /dev/null
        if [ $? -eq 124 ]
        then
            cp $file $1 > /dev/null 2> /dev/null
            echo "copied $file"
        else
            echo "ignored $file"
        fi
    done | pv -l -s $numfiles > /dev/null
