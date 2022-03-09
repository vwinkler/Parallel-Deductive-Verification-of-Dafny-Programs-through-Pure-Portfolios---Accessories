#!/bin/sh

cmd="python make_benchmark_calls.py"

seeds="286325 752764 522591 842099 811175"

for seed in $seeds; do
  echo "mkdir -p with_isntance_selection/split-limit-diversification && cd with_isntance_selection/split-limit-diversification"
  $cmd split-limit-diversification "_004t_${seed}_id0" "--num-instances 4 --seed=$seed --only-instances 0"
  $cmd split-limit-diversification "_004t_${seed}_id1" "--num-instances 4 --seed=$seed --only-instances 1"
  $cmd split-limit-diversification "_004t_${seed}_id2" "--num-instances 4 --seed=$seed --only-instances 2"
  $cmd split-limit-diversification "_004t_${seed}_id3" "--num-instances 4 --seed=$seed --only-instances 3"
  $cmd split-limit-diversification "_004t_$seed" "--num-instances 4 --seed=$seed"
  echo "cd .."

  echo "mkdir -p with_isntance_selection/dynamic-split-limit-diversification && cd with_isntance_selection/dynamic-split-limit-diversification"
  $cmd dynamic-split-limit-diversification "_004t_${seed}_id0" "--num-instances 4 --seed=$seed --only-instances 0"
  $cmd dynamic-split-limit-diversification "_004t_${seed}_id1" "--num-instances 4 --seed=$seed --only-instances 1"
  $cmd dynamic-split-limit-diversification "_004t_${seed}_id2" "--num-instances 4 --seed=$seed --only-instances 2"
  $cmd dynamic-split-limit-diversification "_004t_${seed}_id3" "--num-instances 4 --seed=$seed --only-instances 3"
  $cmd dynamic-split-limit-diversification "_004t_$seed" "--num-instances 4 --seed=$seed"
  echo "cd .."
done
