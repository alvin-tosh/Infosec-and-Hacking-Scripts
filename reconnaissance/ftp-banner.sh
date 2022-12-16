#!/bin/bash


if [ $# -eq 1 ]; then
msfconsole -n -q -r - << EOF
use auxiliary/scanner/ftp/ftp_version
set RHOSTS $1
run
exit
EOF
else
    echo "Please provide the target ftp server."
fi
