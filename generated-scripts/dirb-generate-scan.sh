#!/bin/bash


if [ $# -eq 2 ]; then

  echo "#!/bin/bash"
  echo

  i=1
  oldIFS=$IFS

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
		for port in $webports; do
			echo -n "dirb http://$host:$port/ /usr/share/dirb/wordlists/big.txt -a \"$2\" -o dirb-results-http-$host-$port.txt -f & dirb https://$host:$port/ /usr/share/dirb/wordlists/big.txt -a \"$2\" -o dirb-results-https-$host-$port.txt -f &"
			if [ $(($i%10)) == 0 ]; then
				echo -n " wait"
				echo
				echo
			fi
		i=$((i + 1))
		done
	    fi
  done
  IFS=$oldIFS
else
  echo "Please provide a directory path and a User-Agent string."
fi
