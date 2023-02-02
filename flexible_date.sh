#1/bin/bash

if [ $# -eq 0 ]
then
	input=$( cat /dev/stdin )
else
	input=$1
fi

echo $input
clean_date=$( echo $input | sed 's/[/:\^#]/-/g' )

echo $clean_date
