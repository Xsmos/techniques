#!/bin/bash

if [ $1 -gt 18 ]
then
	echo You may go to the party.
elif [ $2 = 'yes' ]
then
	echo You parents allow you to go.
else
	echo You may not go to the party.
fi	
