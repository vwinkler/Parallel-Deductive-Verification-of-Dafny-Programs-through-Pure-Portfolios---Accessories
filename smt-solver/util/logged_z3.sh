#!/bin/sh

logfilename="$(dirname '$0')/logfile"

#cat - | z3 -in $@ | tee $logfilename
tee $logfilename | z3 -in $@
