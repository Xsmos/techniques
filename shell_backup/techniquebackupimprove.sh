#!/usr/bin/bash
# backup techniques
# Bin 21/12/2022

if [ $# != 1 ]
then
	echo $0 requires one argument, which should be the name of the file to be backup.
	exit
fi

if [ ! -e ~/techniques/$1 ]
then
	echo 'The file seems does not exist. Please check your input.'
	exit
fi

date=`date +%F`
backuppath=~/techniquesbackups/$date
mkdir -p $backuppath

if [ -e ~/techniquesbackups/$date/$1 ]
then
	echo $1 seems already backuped, overwrite anyway? yes/[no]
	read answer

	if [ ! $answer = 'yes' ]
	then
		echo I will cancel this command.
		exit
	fi
fi

cp -r ~/techniques/$1 $backuppath
echo File $1 backup completed.
