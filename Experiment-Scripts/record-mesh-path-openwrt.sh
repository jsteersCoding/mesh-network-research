#!/bin/bash

#Records mesh path at current timestamp and status of mesh path for the duration the script is executed for

while true; do date +%s%N | cut -b1-13 >> mesh-time.log; sudo iw dev mesh0 mpath dump >> mesh-path-metric.log; echo -e "\n" >> mesh-time.log; echo -e "\n" >> mesh-path-metric.log; done
