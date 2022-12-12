#!/bin/bash


if [ $# -eq 2 ]; then
    python3 odat.py sidguesser -s $1 -p $2
else
    echo "Please provide the target host and port."
fi
