PwnVPN - Exploiting known SSL VPN 0 day vulnerabilities to pwn the result from it. Since may be 2018, 
Orange Tsai has found many vulnerabilities from over 3 popular SSL VPN services which tottaly impressive.
After I saw his blog about that vulnerabilies, I found that SSL VPN (portal) is really dangerous and 
exploitable. I found over 2 RCE from bug bounty programs and just feel cool with that. I realized that
all of that vulnerabilities are new, about 1 or 2 years ago, which mean it's will hard to know and fix it.
So, I decided to create the best SSL VPN exploit tool for hackers to can have the best exploit enviroment 
and the sucessful exploitation when most of exploits I found are really bad.



Usage:
 Scan for VPN service:         python[3] pwnvpn.py -s [HOST] -n [-OPTIONS]
 Exploit VPN 0day:             python[3] pwnvpn.py -s [HOST] -e [CVE] [-OPTIONS]
 Show list of 0day:            python[3] pwnvpn.py -l [-OPTIONS]
 
 Example:
  - python[3] pwnvpn.py -s site.co -n
  - python[3] pwnvpn.py -s vpn.site.co -e CVE-2019-1579
  - python[3] pwnvpn.py -l
  - python[3] pwnvpn.py -s 745.123.5.88 -e CVE-2019-1579 -p 8081
  
  
  
(?) Does PwnVPN work with Python2?
Yes, PwnVPN is support both python2 and python3.

(?) Does PwnVPN work in Windows?
PwnVPN works with both Windows and Unix, it will give the best
experience for each OS.

(?) Does PwnVPN is the best SSL VPN exploitation tool?
Yeah, I bringing the best experience for the hackers with the best 
exploit code that both reduce False Posotive and False Negative and 
give hackers the best shell interface with the best exploitation analyst. 
And if there is any issue, I will fix it and even update the code.
  
  
Author: @shelld3v (working at HackerOne and BugCrowd)
Inspired by: Orange Tsai
Maintainer: Ronaldson Bellande (University Student)
