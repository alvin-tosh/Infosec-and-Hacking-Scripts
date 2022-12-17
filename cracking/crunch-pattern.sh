#!/bin/bash

if [ $# -eq 3 ]; then
	crunch $1 $2 -t $3 -o crunch-wordlist-$1-$2.txt
else
    echo "Please provide minimum password length, maximum password length and charset string."
fi
