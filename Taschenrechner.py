"""Taschenrechner
Jetzt packen wir alles zusammen und erstellen einen einfachen Taschenrechner
"""

# Taschenrechner App

# Zuerst definieren wir eine Funktion, die zwei Zahlen addiert
def addieren(x, y):
    return x + y

# Dann definieren wir eine Funktion, die zwei Zahlen subtrahiert
def subtrahieren(x, y):
    return x - y

# Dann definieren wir eine Funktion, die zwei Zahlen multipliziert
def multiplizieren(x, y):
    return x * y

# Dann definieren wir eine Funktion, die zwei Zahlen dividiert
def dividieren(x, y):
    if y == 0:
        return "Division durch Null nicht möglich"
    else:
        return x / y

# Nun fragen wir den Benutzer nach der gewünschten Operation und den beiden Zahlen
print("Welche Operation möchtest du durchführen?")
print("1. Addieren")
print("2. Subtrahieren")
print("3. Multiplizieren")
print("4. Dividieren")

# Wir lesen die Eingabe des Benutzers ein und konvertieren sie in eine Ganzzahl
wahl = int(input("Deine Wahl (1/2/3/4): "))

# Wir lesen die Eingabe des Benutzers für die beiden Zahlen ein und konvertieren sie in Gleitkommazahlen
zahl1 = float(input("Erste Zahl: "))
zahl2 = float(input("Zweite Zahl: "))

# Wir führen die gewünschte Operation aus, indem wir die entsprechende Funktion aufrufen
if wahl == 1:
    print(zahl1, "+", zahl2, "=", addieren(zahl1, zahl2))

elif wahl == 2:
    print(zahl1, "-", zahl2, "=", subtrahieren(zahl1, zahl2))

elif wahl == 3:
    print(zahl1, "*", zahl2, "=", multiplizieren(zahl1, zahl2))

elif wahl == 4:
    print(zahl1, "/", zahl2, "=", dividieren(zahl1, zahl2))

else:
    print("Ungültige Eingabe")