#!/bin/bash


if [ $# -eq 2 ]; then
    svwar -D -m INVITE -p $2 $1
else
    echo "Please provide the target host and port."
fi
