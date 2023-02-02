#!/usr/bin/bash
# demo for backticks
# Bin Xia 21/12/2022

lines=`cat $1 | wc -l`
echo The number of lines in the file $1 is $lines.
