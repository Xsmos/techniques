#!/bin/bash

names='Bin Ruina Zijing Quit'

PS3='Select Character: '

select name in $names
do
	if [ $name == 'Quit' ]
	then
		break
	fi

	echo Hi, $name!
done

echo Bye!
