#!/bin/sh

sed "/(check-sat)/q" $1 && printf "(pop 1)\n"
