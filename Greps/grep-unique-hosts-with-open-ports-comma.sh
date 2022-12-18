#!/bin/bash


if [ $# -eq 1 ]; then

  hostslist=""
  data=$(cat $1/*.gnmap|grep "Ports:")

  while read -r line ; do
    host=$(echo "$line"|cut -d$'\t' -f1|cut -d' ' -f2)
    ports=$(echo "$line"|cut -d$'\t' -f2|sed 's/Ports: //')

  IFS=","
  space=","
  hostports=""

  for port in $ports; do
    openport=$(expr match "$port" '\(.*\(open\|open|filtered\)/\(tcp\|udp\).*\)')
    if [ -n "$openport" ]; then
      hostports=$hostports$(echo $openport|sed 's|/| |g'|sed -n -e 's/open.*//p'|sed 's/ *//g')$space
    fi
  done

  if [ -n "$hostports" ]; then
      hostslist=$(echo "$hostslist $host" | tr " " "\n")
  fi
  done <<< "$data"
  
  echo $hostslist | sort -V | uniq | tr '\n' ',' | sed 's/^,//g' | sed 's/,$//g'
 echo 

else
  echo "Please provide a directory path."
fi
