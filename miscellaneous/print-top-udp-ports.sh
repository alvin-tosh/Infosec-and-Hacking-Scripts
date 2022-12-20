#!/bin/bash


if [[ $EUID -ne 0 ]]; then
  echo "Please run this script as root." 1>&2
  exit 1
fi

if [ $# -eq 1 ]; then
  nmap -oX - -sU --top-ports $1 2>/dev/null | grep 'services=' | sed 's/<scaninfo type="udp" protocol="udp" numservices="[[:digit:]]\+" services="//g' | sed 's|"/>||g'
else
  echo "Please provide number of ports."
fi
