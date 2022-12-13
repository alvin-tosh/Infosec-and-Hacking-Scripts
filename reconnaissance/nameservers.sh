#!/bin/bash


if [ $# -eq 1 ]; then
	host -t ns $1
else
    echo "Please provide the target host."
fi
