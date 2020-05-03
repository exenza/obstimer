#!/bin/bash
pkill -f timer.sh
echo "GO" > .go
rm seconds
./timer.sh 900
exit 0