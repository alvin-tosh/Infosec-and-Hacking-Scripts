#!/bin/bash

if [ $# -eq 1 ]; then
	cat $1 | rsmangler --file - > $1_passwordlist.txt
else
    echo "Please provide a list of words."
fi
