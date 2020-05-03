#!/bin/bash
pkill -f timer.sh
echo "GO" > .go
rm seconds
./timer.sh 3600
exit 0