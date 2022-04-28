#!/bin/sh
touch $2 &&
docker run \
    --volume=$(realpath $1):/source_file.dfy:ro \
    --volume=$(realpath $2):/target_file.bpl:z \
    vwinkler/convert_dafny_to_boogie /source_file.dfy /target_file.bpl
