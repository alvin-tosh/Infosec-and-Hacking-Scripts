#!/bin/bash


if [[ $EUID -ne 0 ]]; then
  echo "For better results, please run this script as root." 1>&2
  exit 1
fi

if [ $# -eq 1 ]; then
  LOGNAME="live_hosts_tcp_ack_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  LOGNAME2="$LOGNAME.txt"
  nmap -vv -n -sn -PA21,22,23,25,53,80,88,110,135,139,143,443,445,465,587,993,995,1433,3306,3389,8080,8443 -oA $LOGNAME $1 | grep 'report' | grep -v 'host down' | sed 's/Nmap scan report for //' | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | tee $LOGNAME2

  LOGNAME="live_hosts_icmp_echo_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  LOGNAME2="$LOGNAME.txt"
  nmap -vv -n -sn -PE -oA $LOGNAME $1 | grep 'report' | grep -v 'host down' | sed 's/Nmap scan report for //' | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | tee $LOGNAME2

  LOGNAME="live_hosts_tcp_protocol_ping_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  LOGNAME2="$LOGNAME.txt"
  nmap -vv -n -sn -PO -oA $LOGNAME $1 | grep 'report' | grep -v 'host down' | sed 's/Nmap scan report for //' | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | tee $LOGNAME2

  LOGNAME="live_hosts_sctp_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  LOGNAME2="$LOGNAME.txt"
  nmap -vv -n -sn -PY2905 -oA $LOGNAME $1 | grep 'report' | grep -v 'host down' | sed 's/Nmap scan report for //' | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | tee $LOGNAME2

  LOGNAME="live_hosts_tcp_syn_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  LOGNAME2="$LOGNAME.txt"
  nmap -vv -n -sn -PS21,22,23,25,53,80,88,110,135,139,143,443,445,465,587,993,995,1433,3306,3389,8080,8443 -oA $LOGNAME $1 | grep 'report' | grep -v 'host down' | sed 's/Nmap scan report for //' | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | tee $LOGNAME2

  LOGNAME="live_hosts_timestamp_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  LOGNAME2="$LOGNAME.txt"
  nmap -vv -n -sn -PP -oA $LOGNAME $1 | grep 'report' | grep -v 'host down' | sed 's/Nmap scan report for //' | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | tee $LOGNAME2

  LOGNAME="live_hosts_udp_top10_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  LOGNAME2="$LOGNAME.txt"
  nmap -sU -n -Pn --top-ports 10 --reason --open -T4 -oA $LOGNAME $1 | grep 'report' | grep -v 'host down' | grep -v 'closed ports' | sed 's/Nmap scan report for //' | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | tee $LOGNAME2

  LOGNAME="live_hosts_tcp_top100_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  LOGNAME2="$LOGNAME.txt"
  nmap -sS -n -Pn --top-ports 100 --reason --open -T4 -oA $LOGNAME $1 | grep 'report' | grep -v 'host down' | grep -v 'closed ports' | sed 's/Nmap scan report for //' | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | tee $LOGNAME2

  LOGNAME="live_hosts_udp_$1"
  LOGNAME=$(echo "$LOGNAME" | sed -r 's/[/]+/_/g' | sed -r 's/[.]+/_/g')
  LOGNAME2="$LOGNAME.txt"
  nmap -vv -n -sn -PU53,67,68,69,123,135,137,138,139,161,162,445,500,514,520,631,1434,1600,4500,49152 -oA $LOGNAME $1 | grep 'report' | grep -v 'host down' | sed 's/Nmap scan report for //' | sort -u -n -t . -k 1,1 -k 2,2 -k 3,3 -k 4,4 | tee $LOGNAME2

  
else
    echo "Please provide the target IP range."
fi
