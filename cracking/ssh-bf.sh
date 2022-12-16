#!/bin/bash


if [ $# -eq 3 ]; then
	patator ssh_login host=$1 user=$2 password=FILE0 0=$3
else
    echo "Please provide a target host, a username and a password list."
fi
