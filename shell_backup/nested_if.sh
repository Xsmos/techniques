#!/bin/bash

if [ $1 -gt 100 ]
then
	echo Hey that\'s a large number.

	if (( $1 % 2 == 0 ))
	then
		echo and it is a even number.
	fi
fi
