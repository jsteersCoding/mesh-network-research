#!/bin/bash

while IFS=" " read -r value1 value2 remainder
do
    echo -e "$value1 \t $value2 \t $remainder" >> $1.xlsx
done < $1
