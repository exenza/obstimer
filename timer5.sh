#!/bin/bash
pkill -f timer.sh
SECONDS=`cat .seconds`
rm seconds
./timer.sh "$((SECONDS+300))"
exit 0