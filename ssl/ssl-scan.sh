#!/bin/bash

if [ $# -eq 2 ]; then
    sslscan --show-certificate --verbose --no-colour --xml=sslscan_$1_$2.xml $1:$2 2>&1 | tee "$1_$2_sslscan.txt"
else
    echo "Please provide the target ip address and the port."
fi
