#!/bin/bash

if [ $# -eq 2 ]; then
	cewl $1 -m $2 -w $1-wordlist.txt
else
    echo "Please provide a website and a password length."
fi
