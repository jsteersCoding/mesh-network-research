#!/bin/bash

name=29th-March-Test
#mkdir $name

count=0

meshdevices=$(cat userhost.lst | wc -l)
meshdevices=$((meshdevices+1))
echo $meshdevices

while read userhost; do
    echo ${userhost}
    ssh root@${userhost} 'name=29th-March-Test; mkdir ~/$name; cd ~/$name; ls signal-recordings.py' &
    scp signal-recordings.py root@${userhost}:~/$name/ &
    count=`expr $count + 1`
done < userhost.lst
