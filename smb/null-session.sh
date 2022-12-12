#!/bin/bash


if [ $# -eq 1 ]; then
	rpcclient -U "" -N $1
else
    echo "Please provide a target host."
fi
