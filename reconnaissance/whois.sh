#!/bin/bash


if [ $# -eq 1 ]; then
	while read line || [[ -n "$line" ]]; do
		echo "Whois Lookup - $line"
		whois $line > "whois-$line.txt"
	done < "$1"
else
    echo "Please provide a file containing a list of target hosts."
fi
