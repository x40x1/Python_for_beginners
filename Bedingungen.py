"""Bedingungen
Wie man Bedingungen in Python schreibt, einschließlich if-else-Anweisungen.
"""

# Bedingungen

# Bedingungen ermöglichen es uns, Code auszuführen, wenn eine bestimmte Bedingung erfüllt ist
# Die grundlegende Syntax für eine Bedingung ist "if", gefolgt von der Bedingung und einem Doppelpunkt
# Der Code, der ausgeführt werden soll, wenn die Bedingung wahr ist, wird eingerückt
#es gibt unterschiedliche Bedingungszeichen:
# == (gleich)
# != (ungleich)
# < (kleiner)
# > (größer)
# <= (kleiner gleich)
# >= (größer gleich)
#
#und noch ein paar mehr

# Hier ist ein Beispiel für eine Bedingung
if 5 > 2:
    print("Fünf ist größer als zwei")

# Man kann auch eine "else"-Anweisung hinzufügen, die ausgeführt wird, wenn die Bedingung falsch ist
# Hier ist ein Beispiel für eine Bedingung mit "else"
if 5 < 2:
    print("Fünf ist kleiner als zwei")
else:
    print("Fünf ist nicht kleiner als zwei")

# Man kann auch mehrere Bedingungen mit "elif" hinzufügen
# Hier ist ein Beispiel für eine Bedingung mit "elif"
x = 5
if x < 0:
    print("x ist negativ")
elif x == 0:
    print("x ist null")
else:
    print("x ist positiv")
