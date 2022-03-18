#!/bin/sh
docker run --volume=$(pwd):/result/:z --volume=$(pwd)/../../benchmarks/:/benchmarks/:ro dafnyportfolio-evaluation $@
