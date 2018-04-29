#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# Aufgabe 002: Temperature Converter

import sys
import random

def main(arg):
    if len(arg) < 4 or not (arg[2] in ["C", "F", "K"] or arg[3] in ["C", "F", "K"]):
        print "Fehlerhafte Eingabe!\nMindestens 3 Parameter:\n" \
            + "1. Temperatur als Zahl\n2. Einheit\n3. In zu konvertierende Einheit\n" \
            + "Einheiten können Kelvin(K), Celsius(C) oder Fahrenheit(F) sein"
        return
    elif arg[2] == arg[3]:
        print "Wieso sollte man die Temperatur in die gleiche Enheit konvertieren?"
        return

    temp = int(arg[1])
    if arg[2] == "C": res = temp + 273.15 if arg[3] == "K" else temp*1.8 + 32
    elif arg[2] == "F": res = (temp - 32)/1.8 if arg[3] == "C" else (temp + 459.67)/1.8
    else: res = temp*1.8 - 459.67 if arg[3] == "F" else temp - 273.15

    print "Das Ergebnis ist " + str(res) + " " + arg[3]

if __name__ == '__main__':
    main(sys.argv)
