#!/bin/bash


if [ $# -eq 1 ]; then
	response=$(ping -c 1 $1 | grep 'received' | cut -d, -f2 | sed 's/received//' | sed 's/ //')
	if [ "$response" -eq "1" ]; then
		echo "$1    YES"
	else
		echo "$1    NO"
	fi
else
	echo "Please provide an IP address."
fi
