#!/bin/bash


if [ $# -eq 1 ]; then

  egrep -v "^#|Status: Up" $1/*.gnmap|cut -d' ' -f2,4-| sed 's/Ignored.*//g' | awk '{printf "Host: " $1 "\nOpen ports: " NF-1 "\n"; $1=""; for(i=2; i<=NF; i++) { a=a""$i; }; split(a,s,","); for(e in s) { split(s[e],v,"/"); printf "%s\t%s\n", v[1], v[5]}; a=""; printf "\n"; }'

else
  echo "Please provide a directory path."
fi
