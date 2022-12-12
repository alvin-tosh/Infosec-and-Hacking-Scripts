#!/bin/bash


if [ $# -eq 1 ]; then
	smbclient -L\\ -N -I $1 2>&1 | tee "smbclient_$1.txt"
else
    echo "Please provide the target host."
fi
