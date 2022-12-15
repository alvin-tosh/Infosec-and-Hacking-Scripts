#!/bin/bash


if [ $# -eq 1 ]; then
	while read line || [[ -n "$line" ]]; do
		echo "IP Lookup - $line"
		host $line | grep "has address" | cut -d" " -f4 > "ip-address-$line.txt"
	done < "$1"
else
    echo "Please provide a file containing a list of target hosts."
fi
