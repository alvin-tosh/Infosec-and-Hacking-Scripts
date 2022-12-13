#!/bin/bash


if [ $# -eq 1 ]; then
msfconsole -n -q -r - << EOF
use auxiliary/scanner/smtp/smtp_version
set RHOSTS $1
run
exit
EOF
else
    echo "Please provide the target smtp server."
fi
