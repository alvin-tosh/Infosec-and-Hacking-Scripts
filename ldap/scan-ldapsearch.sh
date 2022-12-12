#!/bin/bash


if [ $# -eq 5 ]; then
	ldapsearch -v -x -D $3 -w $4 -p $2 -h $1 -b $5 -s sub "(objectclass=*)" 2>&1 | tee > "ldap_all-entries_$1_$2.txt"
else
    echo "Please provide the target host, port, username, password and base dn(dc=example,dc=com)."
fi
