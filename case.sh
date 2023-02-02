#!/bin/bash

case $1 in
	start)
		echo starting
		;;
	stop)
		echo stopping
		;;
	*)
		echo Nothing matchs.
		;;

	restart)
		echo restarting
		;;
esac
