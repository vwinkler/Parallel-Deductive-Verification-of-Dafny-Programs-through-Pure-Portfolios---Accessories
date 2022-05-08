#!/bin/sh

find ../../results/dafny/{portfolio_assembling,bool_params}/ -name '*.json' |
python make_matrix.py -
