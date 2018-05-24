#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# Aufgabe 010: Password Generator

import sys
import random

def main(arg):
    length = 12     # Mindestens 12 Zeichen lang!
    unsicher = True

    try:
        length = int(arg[1])
    except Exception as e:
        pass

    while (unsicher):
        password = []
        for x in xrange(0, length):
            password.append(chr(random.randint(33, 127)))

        for i in password:
            if ord(i) < 65:
                unsicher = False

    print "".join(password)

if __name__ == '__main__':
    main(sys.argv)
