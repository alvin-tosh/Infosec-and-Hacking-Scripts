#!/bin/bash

if [ $# -eq 1 ]; then

  egrep -v "^#|Status: Up" *.gnmap|cut -d' ' -f2,4-|sed 's/Ignored.*//g' |sed 's/ /_/'| sed 's/, /,/g'| awk -v FS=_ '{printf $1 ";" NF ";"; $1=""; for(i=2; i<=NF; i++){ a=a""$i; }; split(a,s,","); for(e in s) { split(s[e],v,"/"); printf "%s(%s)[%s],", v[1], v[5], v[7]}; a=""; printf "\n"; }'

else
  echo "Please provide a directory path."
fi
