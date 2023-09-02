"""Listen
Wie man Listen in Python erstellt und bearbeitet.
"""

# Listen sind eine Sammlung von Elementen, die in einer bestimmten Reihenfolge angeordnet sind
# Listen werden mit eckigen Klammern erstellt und die Elemente werden durch Kommas getrennt

# Hier ist ein Beispiel für eine Liste von Zahlen
zahlen = [1, 2, 3, 4, 5]
print(zahlen)

# Man kann auch eine Liste von Strings erstellen
fruits = ["Apfel", "Banane", "Kirsche"]
print(fruits)

# Man kann auf die Elemente einer Liste zugreifen, indem man ihren Index angibt
# Der Index beginnt bei 0 für das erste Element und erhöht sich um 1 für jedes weitere Element
print(fruits[0]) # gibt "Apfel" aus
print(fruits[1]) # gibt "Banane" aus
print(fruits[2]) # gibt "Kirsche" aus

# Man kann auch auf die Elemente einer Liste von hinten zugreifen, indem man negative Indizes verwendet
# Der Index -1 gibt das letzte Element zurück, -2 das vorletzte usw.
print(fruits[-1]) # gibt "Kirsche" aus
print(fruits[-2]) # gibt "Banane" aus
print(fruits[-3]) # gibt "Apfel" aus

# Man kann die Elemente einer Liste ändern, indem man ihren Index angibt und einen neuen Wert zuweist
fruits[1] = "Orange"
print(fruits) # gibt ["Apfel", "Orange", "Kirsche"] aus

# Man kann auch Elemente zu einer Liste hinzufügen, indem man die Methode append() verwendet
fruits.append("Erdbeere")
print(fruits) # gibt ["Apfel", "Orange", "Kirsche", "Erdbeere"] aus

# Man kann auch Elemente aus einer Liste entfernen, indem man die Methode remove() verwendet
fruits.remove("Orange")
print(fruits) # gibt ["Apfel", "Kirsche", "Erdbeere"] aus