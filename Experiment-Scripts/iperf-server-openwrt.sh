#!/bin/bash

#Must be called inside /etc/rc.local of every Openwrt deployment (2>&1 is POSIX syntax used by /etc/rc.local)

iperf3 -s >> store-transmission-`date +%d-%m-%Y.%H:%M:%S`.txt 2>&1
