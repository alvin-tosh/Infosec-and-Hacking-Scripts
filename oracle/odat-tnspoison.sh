#!/bin/bash

if [ $# -eq 2 ]; then
    python3 odat.py tnspoison -s $1 -p $2 -d $3 --test-module
else
    echo "Please provide the target host and port."
fi
