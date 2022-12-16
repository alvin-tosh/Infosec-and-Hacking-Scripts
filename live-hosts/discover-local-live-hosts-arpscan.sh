#!/bin/bash

# -I	Use network interface

if [[ $EUID -ne 0 ]]; then
  echo "For better results, please run this script as root." 1>&2
  exit 1
fi

if [ $# -eq 2 ]; then
  LOGNAME="local_live_hosts_arp_scan_$1.txt"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g')
  arp-scan -N -q -I $1 $2 > $LOGNAME
else
  echo "Please provide your network device and the target ip range."
fi


