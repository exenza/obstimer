#!/bin/bash
pkill -f timer.sh
echo "GO" > .go
rm seconds
./timer.sh 1800
exit 0