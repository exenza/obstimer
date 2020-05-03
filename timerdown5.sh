#!/bin/bash
SECONDS=`cat .seconds`
SECONDS="$((SECONDS-300))"
if [[ $SECONDS -gt 0 ]]; then
pkill -f timer.sh
rm .seconds
./timer.sh $SECONDS
fi
exit 0
