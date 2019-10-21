#!/bin/sh
DISPLAY=":0"
# in ms
LOCK=500000
while :
do
  IDLE=$(xprintidle)
  if [ $IDLE -gt $LOCK ]; then
    cd /home/idf3da97df/Desktop/SHP/IndProm/Sep-28/5/
    python game.py&
  fi
  sleep 1
done
