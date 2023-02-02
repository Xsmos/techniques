#!/bin/bash

print_sth () {
	a=$1
	return $a
}

print_sth 1
echo return $?

print_sth 2
echo return $?

print_sth 3
echo return $?
