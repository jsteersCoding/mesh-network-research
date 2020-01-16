#!/bin/bash

#ssh root@192.168.30.100 nohup python signal-recordings.py > signal-recorded-`date +%d-%m-%Y.%H:%M:%S`.log 2>&1 # Openwrt does not have nohup installed

#ssh root@192.168.30.100 'cd ~/28th-March; python ~/28th-March/signal-recordings.py > ~/28th-March/signal-recorded-`date +%d-%m-%Y.%H:%M:%S`.log 2>&1' &

name=29th-March-Test

tmpdir=${TMPDIR:-/tmp}/pssh-signal-strength.$$

eval "python signal-recordings-from-laptop.py" > ${tmpdir}/"laptop" 2>&1

mkdir -p $tmpdir

count=0

meshdevices=$(cat userhost.lst | wc -l)
meshdevices=$((meshdevices+1))
echo $meshdevices

while read userhost; do
    ssh root@${userhost} 'name=29th-March-Test; python ~/$name/signal-recordings.py' > ${tmpdir}/${userhost} 2>&1 &
    count=`expr $count + 1`
done < userhost.lst

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

#nohup python signal-recordings.py

#Use nohup on a server to run a command as a child process and detaches from the terminal and continues running if it receives a SIGHUP

#The signal means that sig hangup and will become triggered if you close a terminal and a process is still attached to it

#The output of the process wil be redirected to a file called nohup.out inside the current directory

#Can also use disown -> Run script, then press Ctrl+Z and type disown -> the process would run in the background and detached from the terminal -> The scripts output can also be redirected to a log file with 2>&1 - i.e. python signal-recordings.py > signal-recorded.log 2>&1


