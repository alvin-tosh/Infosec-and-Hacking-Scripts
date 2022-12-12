#!/bin/bash


if [ $# -eq 2 ]; then
    tnscmd10g ping -h $1 -p $2 2>&1 | tee "oracle_tnscmd_ping_$1_$2.txt"
else
    echo "Please provide the target host and port."
fi
