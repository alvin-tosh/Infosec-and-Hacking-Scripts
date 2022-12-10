#!/bin/bash



if [ $# -eq 1 ]; then
  nmap -oX - -sT --top-ports $1 2>/dev/null | grep 'services=' | sed 's/<scaninfo type="connect" protocol="tcp" numservices="[[:digit:]]\+" services="//g' | sed 's|"/>||g'
else
  echo "Please provide number of ports."
fi
