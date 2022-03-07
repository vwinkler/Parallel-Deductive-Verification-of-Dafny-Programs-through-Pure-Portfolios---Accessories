#!/bin/sh

python make_runtime_boxplot.py \
    ../../../results/dafny/with_instance_selection/split-limit-diversification/*.json \
    ../../../results/dafny/with_instance_selection/dynamic-split-limit-diversification/*.json \
    
