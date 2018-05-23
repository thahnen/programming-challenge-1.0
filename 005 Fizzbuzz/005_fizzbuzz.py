#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# Aufgabe 005: Fizzbuzz

import sys
import time

def main(arg):
    if len(arg) == 1:
        print "Ein Parameter, der Anzahl an FizzBuzz-Nummern angibt nötig!"
        return

    i = fb = 1
    numbers = []
    while fb < int(arg[1])+1:
        if (i % 3 == 0) and (i % 5 == 0):
            numbers.append(i)
            i += 1
            fb += 1
        else: i += 1

    print numbers

if __name__ == '__main__':
    before = time.time()
    main(sys.argv)
    print "It took: " + str(time.time()-before) + " seconds!"
