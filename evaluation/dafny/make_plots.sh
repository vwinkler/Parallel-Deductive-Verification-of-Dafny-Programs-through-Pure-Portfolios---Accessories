#!/bin/sh

python make_runtime_boxplot.py \
    ../../results/dafny/no-diversification/*.json \
    ../../results/dafny/seed-diversification/*.json \
    ../../results/dafny/sat-seed-diversification/*.json \
    ../../results/dafny/split-limit-diversification/*.json \
    ../../results/dafny/dynamic-split-limit-diversification/*.json \
    
