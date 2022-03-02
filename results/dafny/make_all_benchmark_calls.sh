#!/bin/sh

cmd="python make_benchmark_calls.py"

seeds="286325 752764 522591 842099 811175"

for seed in $seeds; do
  echo "mkdir -p seed-diversification && cd seed-diversification"
  $cmd seed-diversification "_001t_$seed" "--num-threads 1 --seed=$seed"
  $cmd seed-diversification "_004t_$seed" "--num-threads 4 --seed=$seed"
  echo "cd .."

  echo "mkdir -p sat-seed-diversification && cd sat-seed-diversification"
  $cmd sat-seed-diversification "_001t_$seed" "--num-threads 1 --seed=$seed"
  $cmd sat-seed-diversification "_004t_$seed" "--num-threads 4 --seed=$seed"
  echo "cd .."

  echo "mkdir -p no-diversification && cd no-diversification"
  $cmd no-diversification "_004t_$seed" "--num-threads 4 --seed=$seed"
  echo "cd .."
done
