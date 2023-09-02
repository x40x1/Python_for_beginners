"""Module und Pakete
Wie man Module und Pakete in Python importiert und verwendet.
"""

# Module und Pakete

# In Python können wir Code in Module und Pakete organisieren, um ihn wiederverwendbar zu machen
# Ein Modul ist eine Datei mit Python-Code, die Funktionen, Klassen und Variablen enthält
# Ein Paket ist ein Verzeichnis, das Module und andere Pakete enthalten kann

# Um ein Modul in Python zu importieren, verwenden wir das Schlüsselwort "import", gefolgt vom Modulnamen
# Hier ist ein Beispiel für den Import des Moduls "math"
import math

# Wir können nun auf die Funktionen und Variablen des Moduls "math" zugreifen
print(math.pi) # gibt die Kreiszahl Pi aus

# Wir können auch nur bestimmte Funktionen oder Variablen aus einem Modul importieren, indem wir sie mit Kommas getrennt angeben
from math import sqrt, pow

# Wir können nun auf die Funktionen "sqrt" und "pow" zugreifen, ohne den Modulnamen "math" zu verwenden
print(sqrt(16)) # gibt 4.0 aus
print(pow(2, 3)) # gibt 8.0 aus

# Wenn wir ein Modul mit einem anderen Namen importieren möchten, können wir es mit dem Schlüsselwort "as" umbenennen
import math as m
print(m.pi) # gibt die Kreiszahl Pi aus

# Um ein Paket in Python zu importieren, verwenden wir das Schlüsselwort "import", gefolgt vom Paketnamen
# Hier ist ein Beispiel für den Import des Pakets "os"
import os

# Wir können nun auf die Funktionen und Variablen des Pakets "os" zugreifen
print(os.getcwd()) # gibt das aktuelle Arbeitsverzeichnis aus

# Wir können auch nur bestimmte Module aus einem Paket importieren, indem wir sie mit Kommas getrennt angeben
from os import path, listdir

# Wir können nun auf die Module "path" und "listdir" zugreifen, ohne den Paketnamen "os" zu verwenden
print(path.abspath("test.txt")) # gibt den absoluten Pfad der Datei "test.txt" aus
print(listdir(".")) # gibt eine Liste der Dateien im aktuellen Verzeichnis aus

# Wenn wir ein Paket mit einem anderen Namen importieren möchten, können wir es mit dem Schlüsselwort "as" umbenennen
import os as o
print(o.getcwd()) # gibt das aktuelle Arbeitsverzeichnis aus