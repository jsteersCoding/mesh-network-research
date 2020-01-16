#!/bin/bash

cat mesh-path-metric.log  | awk {'print $1,$2,$5'} | grep fe | awk {'print $2,$3'} > Path-to-F.txt

sudo migrate-to-excel Path-to-F.txt
