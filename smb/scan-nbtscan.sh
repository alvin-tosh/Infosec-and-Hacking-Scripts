#!/bin/bash


if [ $# -eq 1 ]; then
	nbtscan -rvh $1 2>&1 | tee "nbtscan_$1.txt"
else
    echo "Please provide the target host."
fi
