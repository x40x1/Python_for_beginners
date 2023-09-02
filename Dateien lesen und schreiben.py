"""Dateien lesen und schreiben
Wie man Dateien in Python öffnet, liest und schreibt.
"""

# Dateien lesen und schreiben

# Um eine Datei in Python zu öffnen, verwenden wir die Funktion open()
# Die Funktion benötigt den Dateinamen und den Modus, in dem die Datei geöffnet werden soll
# Der Modus kann "r" für Lesen, "w" für Schreiben oder "a" für Anhängen sein
# Wenn der Modus nicht angegeben wird, wird standardmäßig "r" verwendet

# Hier ist ein Beispiel für das Öffnen einer Datei zum Lesen
datei = open("test.txt", "r")

# Wir können nun auf den Inhalt der Datei zugreifen, indem wir die Methode read() verwenden
inhalt = datei.read()
print(inhalt)

# Wir sollten die Datei immer schließen, wenn wir fertig sind
datei.close()

# Hier ist ein Beispiel für das Öffnen einer Datei zum Schreiben
datei = open("neue_datei.txt", "w")

# Wir können nun in die Datei schreiben, indem wir die Methode write() verwenden
datei.write("Dies ist ein Beispieltext.")

# Wir sollten die Datei immer schließen, wenn wir fertig sind
datei.close()

# Hier ist ein Beispiel für das Öffnen einer Datei zum Anhängen
datei = open("bestehende_datei.txt", "a")

# Wir können nun in die Datei schreiben, indem wir die Methode write() verwenden
datei.write("Dies ist ein weiterer Beispieltext.")

# Wir sollten die Datei immer schließen, wenn wir fertig sind
datei.close()