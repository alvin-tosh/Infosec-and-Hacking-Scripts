#!/bin/bash


if [ $# -eq 1 ]; then
	LOGNAME="ip_hostname_$1"
  	LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  	LOGNAME="$LOGNAME.txt"
  	echo -n "$1    "
	nslookup $1 | grep 'name' | cut -f2 | sed 's/name = //' | sed ':a;N;$!ba;s/\n/    /g' | tee -a $LOGNAME
	echo
else
    echo "Please provide the target IP address."
fi
