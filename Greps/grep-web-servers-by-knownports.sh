#!/bin/bash


if [ $# -eq 1 ]; then

  echo "## Web Servers"
  echo

  cat ./*.gnmap | grep "80/open/tcp\|443/open/tcp\|8080/open/tcp\|8443/open/tcp|54071/open/tcp" | while read -r line ; do
  	host=`echo "$line"|cut -d$'\t' -f1|cut -d' ' -f2`
  	ports=`echo "$line"|cut -d$'\t' -f2|sed 's/Ports: //'`

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
      	echo -n "* $host("
      	if echo "$hostports" | grep -q -w "80"; then echo -n '80,'; fi
      	if echo "$hostports" | grep -q -w "443"; then echo -n '443,'; fi
      	if echo "$hostports" | grep -q -w "8080"; then echo -n '8080,'; fi
		    if echo "$hostports" | grep -q -w "8443"; then echo -n '8443,'; fi
        if echo "$hostports" | grep -q -w "54071"; then echo -n '54071,'; fi
		    echo -n ")"
      	echo
    fi
  done

else
  echo "Please provide a directory path."
fi
