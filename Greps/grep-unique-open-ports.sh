#!/bin/bash

if [ $# -eq 1 ]; then
	cat $1/*.gnmap | grep "Ports:" | cut -d' ' -f4- | tr ',' '\n' | sed -n -e 's/\/open.*//p' | sed -e 's/^[ \t]*//' | sort -n | uniq
else
  echo "Please provide a directory path."
fi
