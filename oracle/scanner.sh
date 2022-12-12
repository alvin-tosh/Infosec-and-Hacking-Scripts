#!/bin/bash


if [ $# -eq 2 ]; then
    oscanner -v -s $1 -P $2 2>&1 | tee "oracle_scanner_$1_$2.txt"
else
    echo "Please provide the target host and port."
fi
