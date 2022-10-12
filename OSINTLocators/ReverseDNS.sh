#!/bin/bash 
# DNS reverse lookup script for PWK 
for ip in $(seq 72 91); do 
host -t ptr 38.100.193.$ip | grep "megacorpone" | cut -d " "  -f 1,5 
done 
