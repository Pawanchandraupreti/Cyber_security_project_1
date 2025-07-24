#!/bin/bash
# Blocks malicious IPs using iptables
ATTACKER_IP=$1
sudo iptables -A INPUT -s $ATTACKER_IP -j DROP
sudo iptables-save > /etc/iptables/rules.v4
echo "Blocked IP: $ATTACKER_IP" >> blocked_ips.log