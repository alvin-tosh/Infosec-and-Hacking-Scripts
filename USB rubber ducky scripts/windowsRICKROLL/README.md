## WindowsRICKROLL Ducky script
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white)
### Scans for windows hosts on a network and launches default browsers and plays rick roll on youtube on a loop
To use this script, you will need to replace [IP_ADDRESS] with the IP address of the network you want to scan. 
- For example, if you want to scan the 192.168.1.0/24 network, you would use 192.168.1.* as the IP address.

    - The script first opens the Run dialog (by pressing the Windows key and "r"), 
    - then opens a command prompt and runs the nbtstat command with the -a flag and the specified IP address. 
    - The nbtstat command is a Windows utility that displays protocol statistics and current TCP/IP connections using NetBIOS over TCP/IP. 
    - The -a flag tells nbtstat to resolve the NetBIOS name to an IP address.

This script will scan the specified network for Windows hosts and display the NetBIOS names and IP addresses of any hosts that are found. Note that this script will only work on Windows systems.

