#!/bin/sh

find ../../results/dafny/{portfolio_assembling,bool_params}/ -name '*.json' |
python make_matrix.py -

(
mkdir -p noassert &&
cd noassert &&
find ../../../results/dafny/noassert/ -name '*.json' |
    python ../make_matrix.py -
)
