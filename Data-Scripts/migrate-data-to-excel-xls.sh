#!/bin/bash

# Changed script to write to xls instead of xlsx due to compatibility error

while IFS=" " read -r value1 value2 value3 remainder
do
    sudo echo -e "$value1 \t $value2 \t $value3 \t $remainder" >> ${pwd}${1}.xls 
done < $1

