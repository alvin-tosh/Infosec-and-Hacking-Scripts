#!/bin/bash


if [ $# -eq 2 ]; then
	smtp-user-enum -M VRFY -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -t $1 -p $2 2>&1 | tee "smtp_user-enum_$1_$2.txt"
else
    echo "Please provide the target host and port."
fi
