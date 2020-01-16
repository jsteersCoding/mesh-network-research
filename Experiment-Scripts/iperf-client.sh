#!/bin/bash

# iperf3 client script

iperf3 -c 192.168.30.190 -u -w10000 -l1472 -t60 -i0.1 -b 200k >> multipath-`date +%d-%m-%Y.%H:%M:%S`-.txt
