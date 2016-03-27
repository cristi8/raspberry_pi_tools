#!/bin/bash

while true; do
    bt-network -c `cat /root/phone_bluetooth_mac` nap
    sleep 60
done

