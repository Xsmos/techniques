#!/usr/bin/bash
# variables demonstration
# Bin 21/12/2022

name='Bin'
echo Hello $name

echo The name of the script is $0.

pwd
ls

echo The commands used are: $1 $2 and so on.

echo $# commands were given to the script.

echo All of the commands line arguments are: $*.
