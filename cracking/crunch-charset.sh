#!/bin/bash

if [ $# -eq 3 ]; then
	crunch $1 $2 -f /usr/share/crunch/charset.lst $3 -o crunch-wordlist-$1-$2-$3.txt
else
    echo "Please provide minimum password length, maximum password length and charset string."
fi
