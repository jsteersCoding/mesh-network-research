#!/bin/bash

tmpdir=${TMPDIR:-/tmp}/pssh-mesh-path.$$

eval "sudo iw dev mesh0 mpath dump" > ${tmpdir}/"laptop" 2>&1

mkdir -p $tmpdir

count=0

meshdevices=$(cat userhost.lst | wc -l)
meshdevices=$((meshdevices+1))
echo $meshdevices

#for i in $meshdevices; do
while read userhost; do
    ssh root@${userhost} 'iw dev mesh0 mpath dump' > ${tmpdir}/${userhost} 2>&1 &
    #ssh -n -o BatchMode=yes ${userhost} 'uname -a' > ${tmpdir}/${userhost} 2>&1 &
    count=`expr $count + 1`
done < userhost.lst
#done

while [ $count -gt 0 ]; do
    wait $pids
    count=`expr $count - 1`
done
echo "Output from each host is inside $tmpdir"
echo -e "\n"
arp -an
echo -e "\n"
cat ${tmpdir}/*
echo -e "\n"
ls -1 ${tmpdir}/* | sort

#Wildcard prints files in order: i.e. Numbers then Letters, e.g. 192.168.30.100 before 192.168.30.130, before 192.168.30.190, before laptop

#Write all values to script and record mesh paths onto files corresponding to each device
