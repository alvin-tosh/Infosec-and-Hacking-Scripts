#!/bin/bash


if [ $# -eq 2 ]; then

  echo "#!/bin/bash"
  echo

  echo "if [[ \$EUID -ne 0 ]]; then"
  echo "'Please run this script as root.' 1>&2"
  echo "exit 1"
  echo "fi"
  echo

  cat $1/*.gnmap|grep "Ports:"| while read -r line ; do
    host=`echo "$line"|cut -d$'\t' -f1|cut -d' ' -f2`
    ports=`echo "$line"|cut -d$'\t' -f2|sed 's/Ports: //'`

  IFS=","
  space=","
  hostports=""

  for port in $ports; do
    openport=$(expr match "$port" '\(.*\(open\)/\(tcp\|udp\).*\)')
    if [ -n "$openport" ]; then
      hostports=$hostports$(echo $openport|sed 's|/| |g'|sed -n -e 's/open.*//p'|sed 's/ *//g')$space
    fi
  done

    if [ -n "$hostports" ]; then
      echo "nmap -sU -vv -A -Pn -p$hostports$2 -oA udp_services_$host $host &"
    fi
  done
  echo "wait"
  echo

else
  echo "Please provide a directory path and a random closed port for all hosts."
fi
