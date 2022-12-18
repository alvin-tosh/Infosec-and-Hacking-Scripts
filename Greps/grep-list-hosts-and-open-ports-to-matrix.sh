#!/bin/bash

if [ $# -eq 1 ]; then

  egrep -v "^#|Status: Up" $1/*.gnmap|cut -d' ' -f2,4-| sed 's/Ignored.*//g' | awk '{printf $1 ";" NF-1 ";"; $1=""; for(i=2; i<=NF; i++) { a=a""$i; }; split(a,s,","); for(e in s) { split(s[e],v,"/"); printf "%s(%s),", v[1], v[5]}; a=""; printf "\n"; }'

else
  echo "Please provide a directory path."
fi
