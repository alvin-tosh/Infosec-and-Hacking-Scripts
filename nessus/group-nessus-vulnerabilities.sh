#!/bin/bash


if [ $# -eq 2 ]; then

oldvuln=""
echo "### $2"

cat $1 | grep "\"$2\"" | sed 's/"//g' | awk -F',' 'BEGIN { OFS = ";" }{ print $8, $5, $6, $7 }' | sort | while read -r line ; do

  vuln=$(echo $line | awk -F';' '{print $1}')
  ip=$(echo $line | awk -F';' '{print $2}')
  proto=$(echo $line | awk -F';' '{print $3}')
  port=$(echo $line | awk -F';' '{print $4}')

  if [ "$vuln" != "$oldvuln" ]; then
    if [ "$oldvuln" != "" ]; then
      echo
    fi
    echo
    echo "#### $vuln"
    echo
    echo -n "* $ip ($proto/$port), "
  else
    echo -n "$ip ($proto/$port), "
  fi
  oldvuln=$vuln

done
echo
echo
echo "---"
echo
else
    echo "Please provide a Nessus CSV file and the Risk rate(Critical, High, Medium, Low)."
fi
