## Ducky Super-Encryptor
    - This script uses the nmap command to scan the specified network range for hosts that have port 22 open. 
    - It then filters the output to get only the IP addresses of the hosts, and save them in a file called hosts.txt. 
    - The script then uses the scp command to connect to each host, copy all files and folders, 
    - encrypt all the files and folders, delete the original unencrypted files, and send back the encrypted files to the host.

This script assumes that you have the 'nmap' and 'scp' commands installed, and also the 'ssh_key.pem' 
Also, you need to be able to connect to the hosts using the specified username and ssh key, the 'ssh_key.pem'

#### 🔥 It's important to note that this script can cause serious damage if not used carefully. 
#### 🔥 Encrypting all files on a host may render the system unusable, as many system files are required for the system to function properly. 
#### 🔥 Please ensure you have the necessary permissions, access rights and backups before running this script.
