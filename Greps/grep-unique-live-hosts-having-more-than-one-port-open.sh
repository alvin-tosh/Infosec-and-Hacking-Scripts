#!/bin/bash

if [ $# -eq 1 ]; then
	cat $1/*.gnmap | grep "open.*open" | cut -d ' ' -f2 | sort -V | uniq
else
  echo "Please provide a directory path."
fi
