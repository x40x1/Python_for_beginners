"""Dictionaries
Wie man Dictionaries in Python erstellt und bearbeitet.
"""

# Dictionaries sind eine Sammlung von Schlüssel-Wert-Paaren
# Jeder Schlüssel muss eindeutig sein und auf einen Wert verweisen
# Dictionaries werden mit geschweiften Klammern erstellt und die Schlüssel-Wert-Paare werden durch Kommas getrennt
# Der Schlüssel und der Wert werden durch einen Doppelpunkt getrennt

# Hier ist ein Beispiel für ein Dictionary von Personen
personen = {"Max": 25, "Anna": 30, "Peter": 40}
print(personen)

# Man kann auf den Wert eines Schlüssels zugreifen, indem man den Schlüssel angibt
print(personen["Max"]) # gibt 25 aus

# Man kann auch den Wert eines Schlüssels ändern, indem man den Schlüssel angibt und einen neuen Wert zuweist
personen["Max"] = 26
print(personen) # gibt {"Max": 26, "Anna": 30, "Peter": 40} aus

# Man kann auch ein neues Schlüssel-Wert-Paar hinzufügen, indem man den Schlüssel angibt und einen neuen Wert zuweist
personen["Lisa"] = 35
print(personen) # gibt {"Max": 26, "Anna": 30, "Peter": 40, "Lisa": 35} aus

# Man kann auch ein Schlüssel-Wert-Paar aus einem Dictionary entfernen, indem man den Schlüssel angibt
del personen["Peter"]
print(personen) # gibt {"Max": 26, "Anna": 30, "Lisa": 35} aus