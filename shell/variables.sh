#!/usr/bin/bash
#test variables
#Bin Xia, Dec 23 2022

echo the name of the Bash script is $0.
echo The first argumemt given is $1.
echo The second argument given is $2.
echo et. al.

echo How many arguments are given? $#
echo all the arguments given are: $@

echo the exit status of the most recently run process is $?

echo process ID: $$
echo hostname: $HOSTNAME
echo current line number $LINENO
