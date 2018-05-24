#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# Programming Challenge 1.0
# Aufgabe 004: Simple Encryption/ Decryption

def main(arg):
    # Nicht list(arg[2]) benutzt, da dieses aus Nicht-Ascii Zeichen Müll macht!
    zeichen = [ord(x) for x in arg[1]]

    if arg[0] == "e":
        # "Verschlüsselt" jedes Zeichen anhand der obrigen Liste:
        #   - Zeichen mit geradem Index werden durch das Zeichen an der Stelle - n ersetzt
        #   - Zeichen mit ungeradem Index werden durch das Zeichen an der Stelle + n ersetzt
        #   => n ist in diesem Fall 2!
        #   => man könnte das dann noch weiter verschlüsseln ...

        for index in xrange(0, len(zeichen)):
            nvalue = zeichen[index]

            if nvalue % 2 == 0:
                if nvalue < 2: zeichen[index] = nvalue+253
                else: zeichen[index] = nvalue-2
            else:
                if nvalue > 253: zeichen[index] = nvalue-253
                else: zeichen[index] = nvalue+2

        return "".join([chr(x) for x in zeichen])

    for index in xrange(0, len(zeichen)):
        nvalue = zeichen[index]

        if nvalue % 2 == 0:
            if nvalue > 253: zeichen[index] = nvalue-253
            else: zeichen[index] = nvalue+2
        else:
            if nvalue < 2: zeichen[index] = nvalue+253
            else: zeichen[index] = nvalue-2

    return "".join([chr(x) for x in zeichen])

if __name__ == '__main__':
    print "Disclaimer: Kann nicht mit übergebenen Parametern aus der Shell aus benutzt werden :(\n\n"

    eingabe = "Das ist ein Text, es kommen Preise in € vor und auch überarbeitete $§%& /|\ *^°"
    print eingabe
    ausgabe = main(["e", eingabe])
    print ausgabe
    endergebnis = main(["d", ausgabe])
    print endergebnis
    print endergebnis == eingabe
