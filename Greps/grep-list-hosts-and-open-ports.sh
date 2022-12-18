#!/bin/bash


if [ $# -eq 1 ]; then

  echo "## Open Ports"
  echo

  cat $1/*.gnmap|grep "Ports:"| while read -r line ; do
    host=`echo "$line"|cut -d$'\t' -f1|cut -d' ' -f2`
    ports=`echo "$line"|cut -d$'\t' -f2|sed 's/Ports: //'`

  IFS=","
  space=","
  hostports=""

  echo "### $host"
  echo
  echo -n "* "
  
  for port in $ports; do
    openport=$(expr match "$port" '\(.*\(open\|open|filtered\)/\(tcp\|udp\).*\)')
    if [ -n "$openport" ]; then
      cleanport=$(echo $openport|sed 's|/| |g'|sed -n -e 's/open.*//p'|sed 's/ *//g')" "
      echo -n $cleanport
    fi
  done
  echo
  echo
done
else
  echo "Please provide a directory path."
fi
