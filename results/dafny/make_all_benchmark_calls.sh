#!/bin/sh

cmd="python make_benchmark_calls.py"

seeds="286325 752764 522591 842099 811175"

for seed in $seeds; do
  echo "mkdir -p no-portfolio && cd no-portfolio"
  $cmd seed-diversification "_$seed" "--num-threads 1 --seed=$seed"
  echo "cd .."

  echo "mkdir -p no-diversification && cd no-diversification"
  $cmd no-diversification "_$seed" "--num-threads 4 --seed=$seed"
  echo "cd .."

  echo "mkdir -p seed-diversification && cd seed-diversification"
  $cmd seed-diversification "_$seed" "--num-threads 4 --seed=$seed"
  echo "cd .."
done
