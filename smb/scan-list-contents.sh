#!/bin/bash


if [ $# -eq 2 ]; then
	smbmap -H $1 -P $2 -R 2>&1 | tee -a "smbmap-list-contents_$1_$2.txt"; smbmap -u null -p "" -H $1 -P $2 -R 2>&1 | tee -a "smbmap-list-contents_$1_$2.txt"
else
    echo "Please provide the target host and port."
fi
