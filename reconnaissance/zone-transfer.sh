#!/bin/bash


if [ $# -eq 2 ]; then
	host -l $1 $2
else
    echo "Please provide a target host and a nameserver."
fi
