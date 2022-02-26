#/bin/sh

cmd="python make_benchmark_calls.py"

echo "mkdir -p no-portfolio && cd no-portfolio"
$cmd no-diversification "--num-threads 1"
echo "cd .."

echo "mkdir -p seed-diversification && cd seed-diversification"
$cmd seed-diversification "--num-threads 4"
echo "cd .."
