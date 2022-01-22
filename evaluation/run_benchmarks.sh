#!/bin/sh

cmd="python3 ../smt-solver/main.py"
problems_dir=../smt-solver/dafny
problems_regex="$problems_dir/(.*).problem.json"
results_dir=results/dafny
result_suffix=result.json

declare -a problems=("test.problem.json")
declare -a seeds=("874136" "020391" "118326" "710007" "559237")

for problem in "${problems[@]}"
do
    problem_filename=$problems_dir/$problem
    if [[ $problem_filename =~ $problems_regex ]]
    then
        problem_file=${BASH_REMATCH[0]}
        base_name=${BASH_REMATCH[1]}
        result_file=$results_dir/$base_name.$result_suffix
        for seed in "${seeds[@]}";
        do
            mkdir -p $results_dir
            result_file=$results_dir/${base_name}_$seed.$result_suffix
            $cmd --seed $seed --problems $problem_file:$result_file
        done
    fi
done
