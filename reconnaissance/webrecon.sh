#!/bin/bash

if [ $# -eq 2 ]; then
	python web-reconnaissance.py -u $1 -o $2
	pandoc -s -o $2.html $2
	xdg-open $2.html
else
    echo "Please provide the target url and a filepath to save logs."
fi
