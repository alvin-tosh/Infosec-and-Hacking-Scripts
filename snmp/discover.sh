#!/bin/bash


if [ $# -eq 1 ]; then
	nmap -sU --open -p 161 $1
else
    echo "Please provide a target host or a target ip range."
fi
