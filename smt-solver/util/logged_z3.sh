#!/bin/sh

logfilename="$(dirname '$0')/logfile"

tee $logfilename | z3 -in $@
