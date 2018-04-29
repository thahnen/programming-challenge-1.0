#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# Aufgabe 001: Heads or Tails

import sys
import random

def main(arg):
    # 1 = Heads, 0 = Tails
    result = "It is: Heads" if random.randint(0, 1) == 1 else "It is: Tails"

    if len(arg) > 1:
        if (arg[1] != "Heads" and arg[1] != "Tails" or len(arg) > 2):
            print "Fehlerhafte Eingabe!\nEntweder keine Parameter oder 'Heads'/'Tails!'"
            return
        result += "\nYou were right!" if result.split(" ")[2] == arg[1] else "\nYou were wrong!"

    print result

if __name__ == '__main__':
    main(sys.argv)
