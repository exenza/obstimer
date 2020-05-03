#!/bin/bash
pkill -f timer.sh
SECONDS=`cat .seconds`
rm seconds
./timer.sh "$((SECONDS+60))"
exit 0