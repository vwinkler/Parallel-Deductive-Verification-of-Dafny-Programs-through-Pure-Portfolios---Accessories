
sbatch << EOF
#!/bin/sh
#SBATCH --partition=dev_single
#SBATCH --exclusive
#SBATCH --time 00:00:30
if [[ ! -e 'dev/test-dfy-impl-module-default-triple-seed-diversification-10-0-286325.json' ]]; then enroot start --mount=/storage/vwinkler/Studium/Masterarbeit/ParallelVerification/results/dafny/dev:/result/ --mount=/storage/vwinkler/Studium/Masterarbeit/ParallelVerification/benchmarks/dafny:/benchmarks/ vwinkler+dafnyportfolio-evaluation /benchmarks/test.dfy 'Impl$$_module.__default.Triple' seed-diversification /result/test-dfy-impl-module-default-triple-seed-diversification-10-0-286325.json --dafny-cmd /opt/dafny/dafny --num-instances 10 --seed 286325 --only-instances 0 ; else echo skipping 'dev/test-dfy-impl-module-default-triple-seed-diversification-10-0-286325.json'; fi
if [[ ! -e 'dev/test-dfy-impl-module-default-triple-seed-diversification-10-1-286325.json' ]]; then enroot start --mount=/storage/vwinkler/Studium/Masterarbeit/ParallelVerification/results/dafny/dev:/result/ --mount=/storage/vwinkler/Studium/Masterarbeit/ParallelVerification/benchmarks/dafny:/benchmarks/ vwinkler+dafnyportfolio-evaluation /benchmarks/test.dfy 'Impl$$_module.__default.Triple' seed-diversification /result/test-dfy-impl-module-default-triple-seed-diversification-10-1-286325.json --dafny-cmd /opt/dafny/dafny --num-instances 10 --seed 286325 --only-instances 1 ; else echo skipping 'dev/test-dfy-impl-module-default-triple-seed-diversification-10-1-286325.json'; fi
if [[ ! -e 'dev/test-dfy-impl-module-default-triple-seed-diversification-10-2-286325.json' ]]; then enroot start --mount=/storage/vwinkler/Studium/Masterarbeit/ParallelVerification/results/dafny/dev:/result/ --mount=/storage/vwinkler/Studium/Masterarbeit/ParallelVerification/benchmarks/dafny:/benchmarks/ vwinkler+dafnyportfolio-evaluation /benchmarks/test.dfy 'Impl$$_module.__default.Triple' seed-diversification /result/test-dfy-impl-module-default-triple-seed-diversification-10-2-286325.json --dafny-cmd /opt/dafny/dafny --num-instances 10 --seed 286325 --only-instances 2 ; else echo skipping 'dev/test-dfy-impl-module-default-triple-seed-diversification-10-2-286325.json'; fi
EOF

