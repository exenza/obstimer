#!/bin/bash
pkill -f timer.sh

#Evaluate parameters to set timer time
if [ "$1" != "" ]; then
    echo $1 > .seconds
else
    x=0
    while :
    do
        x=$(($x+1))
        printf '%02dh:%02dm:%02ds\n' $(($x/3600)) $(($x%3600/60)) $(($x%60)) > timer.txt
        sleep 1
    done
fi
START=`cat .seconds`
END=$START

STATUS=`cat .go`
if [ "$STATUS" = "GO" ]; then
    END=0
fi

for i in $(eval echo "{$START..$END}")
do
    printf '%02dh:%02dm:%02ds\n' $(($i/3600)) $(($i%3600/60)) $(($i%60)) > timer.txt
    echo $i > .seconds
        sleep 1
done
