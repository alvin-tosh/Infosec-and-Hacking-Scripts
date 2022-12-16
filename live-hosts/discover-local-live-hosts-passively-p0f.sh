#!/bin/bash



if [[ $EUID -ne 0 ]]; then
  echo "For better results, please run this script as root." 1>&2
  exit 1
fi

if [ $# -eq 1 ]; then
  LOGNAME="local_live_hosts_p0f_$1.txt"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g')
  p0f -i $1 > $LOGNAME
else
  echo "Please provide your network device."
fi

