#!/bin/bash

GREEN='\033[0;32m'
NC='\033[0m' # No Color
dd=$(date +"%Y-%m-%d-%H-%M")

if [ $# -eq 1 ]; then
	logfile="live_hosts_ping_$1"
  	logfile=$(echo "$logfile" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  	logfile="$logfile.txt"

	file=$1
	echo "---- $dd ----" >> $logfile
	while IFS= read -r ipaddr
	do
		echo "Pinging $ipaddr.."
		response=$(ping -c 1 -W 1 $ipaddr | grep 'bytes from' | cut -d' ' -f4 |sed 's/://')
		if [ ! -z "$response" ]; then
			printf "${GREEN}%s${NC} responds..\n" "$ipaddr"
			echo "$ipaddr" >> $logfile
		fi
	done <"$file"
else
	echo "Please provide a file containing a list of IP addresses."
fi
