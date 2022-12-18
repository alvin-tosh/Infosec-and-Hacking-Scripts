#!/bin/bash


if [ $# -eq 1 ]; then

  echo "## Web Servers"
  echo

  cat $1/*.gnmap | grep "/open/tcp//http\|/open/tcp//ssl" | while read -r line ; do
    host=`echo "$line"|cut -d$'\t' -f1|cut -d' ' -f2`
    ports=`echo "$line"|cut -d$'\t' -f2|sed 's/Ports: //'`

    IFS=","
    space=","
    hostports=""
    webports=""

    for port in $ports; do
      openports=$(expr match "$port" '\(.*\(open\|open|filtered\)/\(tcp\|udp\).*\)')
      if [ -n "$openports" ]; then

    ports=`echo "$openports"|tr "," "\n"`
    if [ -n "$ports" ]; then
      for port in $ports; do

        if echo "$port" | grep -q "/open/tcp//http\|/open/tcp//ssl"; then 
          webports=$webports$(echo $port|sed 's|/| |g'|sed -n -e 's/open.*//p'|sed 's/ *//g')$space
        fi
      done
    fi
      fi
    done

      if [ -n "$webports" ]; then
    echo -n "* $host("
    echo -n "${webports::-1}"
    echo -n ")"
    echo
      fi
  echo
  done

else
  echo "Please provide a directory path."
fi
