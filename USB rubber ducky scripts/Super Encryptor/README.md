## Ducky Super-Encryptor
![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Windows 11](https://img.shields.io/badge/Windows%2011-%230079d5.svg?style=for-the-badge&logo=Windows%2011&logoColor=white) ![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black) ![Android](https://img.shields.io/badge/Android-3DDC84?style=for-the-badge&logo=android&logoColor=white)

and (unless I am mistaken - haven't tested it yet) 

![iOS](https://img.shields.io/badge/iOS-000000?style=for-the-badge&logo=ios&logoColor=white) ![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)

    - This script uses the nmap command to scan the specified network range for hosts that have port 22 open. 
    - It then filters the output to get only the IP addresses of the hosts, and save them in a file called hosts.txt. 
    - The script then uses the scp command to connect to each host, copy all files and folders, 
    - encrypt all the files and folders, delete the original unencrypted files, and send back the encrypted files to the host.

This script assumes that you have the 'nmap' and 'scp' commands installed, and also the 'ssh_key.pem' 
Also, you need to be able to connect to the hosts using the specified username and ssh key, the 'ssh_key.pem'

#### 🔥 It's important to note that this script can cause serious damage if not used carefully. 
#### 🔥 Encrypting all files on a host may render the system unusable, as many system files are required for the system to function properly. 
#### 🔥 Please ensure you have the necessary permissions, access rights and backups before running this script.
