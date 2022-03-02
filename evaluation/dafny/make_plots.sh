#!/bin/sh

python make_runtime_boxplot.py \
    ../../results/dafny/no-portfolio/*.json \
    ../../results/dafny/no-diversification/*.json \
    ../../results/dafny/seed-diversification/*.json \
    
