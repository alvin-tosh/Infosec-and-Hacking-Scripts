#!/bin/bash



if [[ $EUID -ne 0 ]]; then
  echo "For better results, please run this script as root." 1>&2
  exit 1
fi

if [ $# -eq 1 ]; then
  nmap -sS -vv -n -Pn --reason --open -T4 --top-ports 100 -O $1 | grep 'Nmap scan report for\|OS details\|Aggressive OS guesses\|Device type'| sed 's/Nmap scan report for /IP:/'|sed 's/Aggressive OS guesses/OS/'|sed 's/OS details/OS/'
else
  echo "Please provide the target ip range."
fi

