#!/bin/bash

if [ $USER = 'Bin' ] || [ $USER = 'xia' ]
then
	echo user $USER is permitted to view the following file.
	ls -alh
fi
