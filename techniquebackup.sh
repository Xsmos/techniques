#!/usr/bin/bash
# backup techniques
# Bin 21/12/2022

date=`date +%F`
backuppath=~/techniquesbackups/$date
mkdir -p $backuppath

cp -r ~/techniques/$1 $backuppath

echo File $1 backup completed.
