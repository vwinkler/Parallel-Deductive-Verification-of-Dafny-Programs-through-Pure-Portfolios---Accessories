#!/bin/sh

python3 \
    ../../dafnyportfolio/src/evaluation//plot_by_benchmark.py selection_penalized_collection.h5 \
    --max-runtime 600 \
    --y-scale log
