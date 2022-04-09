#!/bin/sh

mkdir -p pc && cd pc &&
python ../make_runtime_boxplot.py \
    ../../../results/dafny/no-diversification/*.json \
    ../../../results/dafny/seed-diversification/*.json \
    ../../../results/dafny/sat-seed-diversification/*.json \
    ../../../results/dafny/split-limit-diversification/*.json \
    ../../../results/dafny/dynamic-split-limit-diversification/*.json
python ../make_runtime_boxplot.py \
    ../../../results/dafny/with_instance_selection/split-limit-diversification/*.json \
    ../../../results/dafny/with_instance_selection/dynamic-split-limit-diversification/*.json
cd ..
    
mkdir -p cluster && cd cluster &&
python ../make_runtime_boxplot.py ../../../results/dafny/experiments/*.json
python ../make_matrix.py ../../../results/dafny/experiments/*.json
cd ..
