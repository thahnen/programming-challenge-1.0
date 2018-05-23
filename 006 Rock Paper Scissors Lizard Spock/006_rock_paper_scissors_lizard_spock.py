#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# Aufgabe 006: Rock Paper Scissors Lizard Spock

import sys
import random

def main(arg):
    if len(arg) == 1:
        print "Ein Parameter, der deine Wahl angibt benötigt!"
        return

    mglkeiten = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]
    auswahl = arg[1]
    gewonnen = False

    if auswahl not in mglkeiten:
        print "Falsche Angabe, nur 'Rock', 'Paper', 'Scissors', 'Lizard' und 'Spock' möglich!"
        return

    computer = mglkeiten[random.randint(0, len(mglkeiten)-1)]
    if computer == auswahl:
        print "Unentschieden, beide haben das gleiche gewählt!"
        return

    if auswahl == "Rock":
        if computer == "Lizard" or computer == "Scissors": gewonnen = True
    elif auswahl == "Paper":
        if computer == "Rock" or computer == "Spock": gewonnen = True
    elif auswahl == "Scissors":
        if computer == "Paper" or computer == "Lizard": gewonnen = True
    elif auswahl == "Lizard":
        if computer == "Paper" or computer == "Spock": gewonnen = True
    else:
        if computer == "Scissors" or computer == "Rock": gewonnen = True

    if gewonnen: print auswahl + " schlägt " + computer + ". Du hast gewonnen!"
    else: print computer + " schlägt " + auswahl + ". Du hast verloren!"

if __name__ == '__main__':
    main(sys.argv)
