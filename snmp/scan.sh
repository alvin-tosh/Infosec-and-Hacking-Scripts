#!/bin/bash

if [ $# -eq 1 ]; then
	onesixtyone -c /usr/share/seclists/Discovery/SNMP/common-snmp-community-strings-onesixtyone.txt -dd $1 2>&1 | tee "snmp_onesixtyone_$1.txt"
else
    echo "Please provide a target host."
fi
