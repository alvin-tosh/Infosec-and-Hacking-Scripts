#!/bin/bash


if [ $# -eq 1 ]; then
	snmpwalk -c public -v 1 $1 2>&1 | tee "snmpwalk.txt"

    snmpwalk -c public -v 1 $1 1.3.6.1.2.1.25.1.6.0 2>&1 | tee "snmpwalk_system_processes.txt"

    snmpwalk -c public -v 1 $1 1.3.6.1.2.1.25.4.2.1.2 2>&1 | tee "snmpwalk_running_processes.txt"

    snmpwalk -c public -v 1 $1 1.3.6.1.2.1.25.4.2.1.4 2>&1 | tee "snmpwalk_process_paths.txt"

    snmpwalk -c public -v 1 $1 1.3.6.1.2.1.25.2.3.1.4 2>&1 | tee "snmpwalk_storage_units.txt"

    snmpwalk -c public -v 1 $1 1.3.6.1.2.1.25.6.3.1.2 2>&1 | tee "snmpwalk_software_names.txt"

    snmpwalk -c public -v 1 $1 1.3.6.1.4.1.77.1.2.25 2>&1 | tee "snmpwalk_user_accounts.txt"

    snmpwalk -c public -v 1 $1 1.3.6.1.2.1.6.13.1.3 2>&1 | tee "snmpwalk_tcp_ports.txt"

else
    echo "Please provide a target host."
fi
