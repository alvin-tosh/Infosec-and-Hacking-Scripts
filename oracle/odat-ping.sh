#!/bin/bash

if [ $# -eq 2 ]; then
    python3 odat.py tnscmd -s $1 -p $2 --ping
else
    echo "Please provide the target host and port."
fi
