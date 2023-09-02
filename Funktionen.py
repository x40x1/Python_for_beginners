"""Funktionen
Wie man Funktionen in Python definiert und aufruft.
"""

# Funktionen ermöglichen es uns, Code zu organisieren und wiederverwendbar zu machen
# Eine Funktion wird definiert mit dem Schlüsselwort "def", gefolgt vom Funktionsnamen, den Argumenten in Klammern und einem Doppelpunkt
# Der Code, der in der Funktion ausgeführt werden soll, wird eingerückt
# Eine Funktion kann einen Wert zurückgeben mit dem Schlüsselwort "return"

# Hier ist ein Beispiel für eine Funktion, die die Summe von zwei Zahlen berechnet
def addiere(zahl1, zahl2):
    summe = zahl1 + zahl2
    return summe

# Man ruft eine Funktion auf, indem man ihren Namen und die Argumente in Klammern angibt
# Hier ist ein Beispiel für den Aufruf der Funktion addiere
ergebnis = addiere(3, 5)
print(ergebnis) # gibt 8 aus