#!/bin/bash
pkill -f timer.sh
echo "GO" > .go
rm seconds
./timer.sh 2700
exit 0