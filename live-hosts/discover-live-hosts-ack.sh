#!/bin/bash


if [[ $EUID -ne 0 ]]; then
  echo "For better results, please run this script as root." 1>&2
  exit 1
fi

if [ $# -eq 1 ]; then
  LOGNAME="live_hosts_tcp_ack_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  LOGNAME2="$LOGNAME.txt"
  nmap -vv -n -sn -PA21,22,23,25,53,80,88,110,111,135,139,143,199,443,445,465,587,993,995,1025,1433,1723,3306,3389,5900,8080,8443 -oA $LOGNAME $1 | grep -w 'report' | grep -v 'host down' | sed 's/Nmap scan report for //' | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | tee $LOGNAME2
else
    echo "Please provide the target IP range."
fi
