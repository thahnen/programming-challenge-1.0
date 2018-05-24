#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# Aufgabe 003: Calculate age in seconds

import sys
import datetime

def main(arg):
    if len(arg) == 1 or "." not in arg[1]:
        print "Ein Parameter muss übergeben werden im Format:\nDD.MM.YYYY"
        return
        
    birth = [int(i) for i in arg[1].split(".")]
    try:
        birth = datetime.datetime(birth[2], birth[1], birth[0])
    except Exception as e:
        print "Parametereingabe wie folgt:\nDD.MM.YYYY"
        return

    print "Du bist " \
        + str((datetime.datetime.now()-birth).total_seconds()) \
        + " Sekunden alt!"

if __name__ == '__main__':
    main(sys.argv)
