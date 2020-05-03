#!/bin/bash
STATUS=`cat .go`
if [ "$STATUS" = "GO" ]; then
    rm .go
    pkill -f timer.sh
else
    echo "GO" > .go
    ./timer.sh `cat .seconds`
fi
