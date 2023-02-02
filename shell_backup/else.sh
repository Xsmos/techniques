#!/bin/bash

if [ $# -eq 1 ]
then
	nl $1
	echo '$#=1'
else
	nl /dev/stdin
	echo '$#!=1'
fi
