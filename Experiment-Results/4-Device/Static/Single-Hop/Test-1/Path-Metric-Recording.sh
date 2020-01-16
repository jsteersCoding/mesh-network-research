#!/bin/bash

cat mesh-path-metric.log  | awk {'print $1,$2,$5'} | grep fe | awk {'print $2,$3'} > Path-to-F.txt

sudo migrate-to-excel Path-to-F.txt

#open xls file
#remove new lines from mesh time fle
#copy mesh times to clipboard
#paste into xls file
#run readtext-to-file.py
#run metric-graph generator
