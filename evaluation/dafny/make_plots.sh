#!/bin/sh

mkdir -p compare_portfolios && cd compare_portfolios &&
python ../make_runtime_boxplot.py \
    ../../../results/dafny/no-diversification/*.json \
    ../../../results/dafny/seed-diversification/*.json \
    ../../../results/dafny/sat-seed-diversification/*.json \
    ../../../results/dafny/split-limit-diversification/*.json \
    ../../../results/dafny/dynamic-split-limit-diversification/*.json
cd ..

mkdir -p compare_instances && cd compare_instances &&
python ../make_runtime_boxplot.py \
    ../../../results/dafny/with_instance_selection/split-limit-diversification/*.json \
    ../../../results/dafny/with_instance_selection/dynamic-split-limit-diversification/*.json
cd ..
    

    
