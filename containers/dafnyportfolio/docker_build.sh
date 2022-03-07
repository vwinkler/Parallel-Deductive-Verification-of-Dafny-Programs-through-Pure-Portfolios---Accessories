#!/bin/sh

docker build ../../ -f Dockerfile -t vwinkler/dafnyportfolio-evaluation --build-arg COMMIT_HASH=$(git rev-parse HEAD)
