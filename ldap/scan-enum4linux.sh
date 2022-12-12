#!/bin/bash


if [ $# -eq 1 ]; then
	enum4linux -a -v -M -l -d $1 2>&1 | tee "enum4linux_$1.txt"
else
    echo "Please provide the target host."
fi
