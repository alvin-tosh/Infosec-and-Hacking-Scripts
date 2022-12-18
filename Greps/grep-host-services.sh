#!/bin/bash


if [ $# -eq 1 ]; then
  echo "## Services"
  echo

  cat $1/*.gnmap|grep "Ports:"| while read -r line ; do
    os=`echo "$line"|cut -d$'\t' -f3|grep 'OS:'|sed 's/OS: //'`
    host=`echo "$line"|cut -d$'\t' -f1|cut -d' ' -f2`
    ports=`echo "$line"|cut -d$'\t' -f2|sed 's/Ports: //'`

  IFS=","
  space="\n"
  hostports=""

  for port in $ports; do
    openport=$(expr match "$port" '\(.*\(open\|open|filtered\)/\(tcp\|udp\).*\)')
    if [ -n "$openport" ]; then
      hostports=$hostports"* "$(echo $openport|sed 's|/| |g'|sed 's/open//'|sed 's/|filtered//'|sed -r 's/(tcp|udp)//'|sed 's/  */ /g'|sed 's/^ //')$space
    fi
  done

    if [ -n "$hostports" ]; then
      echo "### $host"
      echo
      if [ -n "$os" ]; then
        echo "* $os"
        echo
      fi
      printf "$hostports"
      echo
    fi
  done

else
  echo "Please provide a directory path."
fi
