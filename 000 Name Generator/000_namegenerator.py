#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# Aufgabe 000: Name Generator

import os
import sys
import random

def main(arg):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    nachnamen = [line.strip("\n") for line in open(dir_path + "/nachnamen.txt")]
    vornamen = [dir_path + "/jungen.csv", dir_path + "/maedchen.csv"]

    if len(arg) == 1:
        vorname = "Name"
        try:
            vornamen = [line.strip("\n") for line in open(vornamen[random.randint(0, 1)])]
            while (vorname == "Name" or vorname == "vorname"):
                vorname = (vornamen[random.randint(0, len(vornamen)-1)]).split(";")[0]
        except Exception as e:
            print "Unbekannter Fehler mit Vorname"
            raise

        try:
            nachname = nachnamen[random.randint(0, len(nachnamen)-1)]
        except Exception as e:
            print "Unbekannter Fehler mit Nachname"
            raise

        print unicode(vorname + " " + nachname, errors="replace")
        return

    if len(arg) != 1:
        # Andere Sachen machen, mehr Möglichkeiten hinzufügen
        main([arg[0]])


if __name__ == '__main__':
    main(sys.argv)
