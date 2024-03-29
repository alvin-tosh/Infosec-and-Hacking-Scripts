#!/bin/bash

#    This file is part of PenTestKit
#    Copyright (C) 2017-2020 @maldevel
#    https://github.com/maldevel/PenTestKit
#
#    PenTestKit - Useful tools for Penetration Testing.
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
#    For more see the file 'LICENSE' for copying permission.


if [[ $EUID -ne 0 ]]; then
  echo "Please run this script as root." 1>&2
  exit 1
fi

if [ $# -eq 2 ]; then
	nmap -sS -vv --top-ports 1000 --reason --open --max-rate $2 -oA tcp_ports_1000_maxrate_$1 $1
else
    echo "Please provide the target IP address or an IP range and the max rate."
fi
