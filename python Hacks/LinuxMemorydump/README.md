# Linux Memory Dump
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com) 

![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)![Kubuntu](https://img.shields.io/badge/-KUbuntu-%230079C1?style=for-the-badge&logo=kubuntu&logoColor=white)![Debian](https://img.shields.io/badge/Debian-D70A53?style=for-the-badge&logo=debian&logoColor=white)![Arch](https://img.shields.io/badge/Arch%20Linux-1793D1?logo=arch-linux&logoColor=fff&style=for-the-badge)![Linux Mint](https://img.shields.io/badge/Linux%20Mint-87CF3E?style=for-the-badge&logo=Linux%20Mint&logoColor=white)

This will prompt the user to enter the PID of the process they want to dump and the name of the file they want to save the dump to. It then uses the subprocess module to call the "gcore" command, which creates a core dump of the process with the specified PID and saves it to the specified file.

    Note that to run gcore command you need to have gdb installed on the machine and running the script as root user. 
    Also, this script is just a template so you kinda have to tweak it to suit your specific needs.
