#!/bin/bash

for value in $1/*
do
	used=$( df $1 | tail -1 | awk '{ print $5 }' | sed 's/%//' )
	echo used: $used

	if [ $used -gt 10 ]
	then
		echo free space is less than 10%, copy command ceased.
		break
	fi

	cp $value $1/py_backup
done
