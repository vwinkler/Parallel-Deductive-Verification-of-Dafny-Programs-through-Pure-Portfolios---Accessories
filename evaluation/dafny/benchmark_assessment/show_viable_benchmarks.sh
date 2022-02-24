#!/bin/sh

cat benchmark_results.txt | egrep "real\s[^0]" --context=2 --group-separator=""
