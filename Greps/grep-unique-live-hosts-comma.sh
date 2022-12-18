#!/bin/bash

if [ $# -eq 1 ]; then
	cat $1/*.gnmap | grep 'Status: Up' | cut -d ' ' -f2 | sort -V | uniq | tr '\n' ',' | sed 's/,$//g'
	echo 
else
  echo "Please provide a directory path."
fi
