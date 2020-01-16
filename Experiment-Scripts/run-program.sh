#!/bin/bash

# Run on source to test iperf against a running server, to record the signal strength of neighbouring devices and to record the state of the mesh path

date & . iperf-client.sh & python signal-recordings.py > signal-strength-on-laptop.txt & . record-mesh-path-openwrt.sh
