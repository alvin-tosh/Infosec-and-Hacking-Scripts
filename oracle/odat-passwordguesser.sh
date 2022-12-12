#!/bin/bash


if [ $# -eq 2 ]; then
    python3 odat.py passwordguesser -s $1 -p $2 -d $3 --accounts-file accounts/accounts_multiple.txt
else
    echo "Please provide the target host and port."
fi
