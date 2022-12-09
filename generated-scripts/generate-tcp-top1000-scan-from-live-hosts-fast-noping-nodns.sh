#!/bin/bash


if [ $# -eq 1 ]; then

  echo "#!/bin/bash"
  echo

  echo "if [[ \$EUID -ne 0 ]]; then"
  echo "'Please run this script as root.' 1>&2"
  echo "exit 1"
  echo "fi"
  echo

  cat $1/*.gnmap | grep 'Status: Up' | cut -d ' ' -f2 | sort -V | uniq| while read -r host ; do

  	echo "nmap -sS -n -Pn -vv --top-ports 1000 --reason --open -T4 -oA tcp_ports_full_$host $host &"

  done
  echo "wait"
  echo

else
  echo "Please provide a directory path."
fi
