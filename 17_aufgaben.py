#Hausaufgabe 01 (random):
#Entwickle ein interaktives Konsolen-Programm in Python, 
#bei dem der Computer eine zufällige Geheimzahl (zwischen 1 und 99) generiert und der Benutzer diese mit logischen Hinweisen ("zu hoch" / "zu niedrig") erraten muss.
#Am Ende soll die Anzahl der benötigten Versuche ausgegeben werden.


#lösung :
import random 

# Generiert eine ganze Zufallszahl von 1 bis einschließlich 99
geheimzahl = random.randint(1, 99)
versuche = 0

print("willkommen beim zahlen - ratespiel")
print("ich habe mir eine zahl zwischen1 und 99 ausgedacht. finde sie heraus!")

while True :
    eingabe = input("dein tipp :")
    try :
        tipp = int(eingabe)
    except ValueError :
        print("ungültige eingabe! bitte gib eine ganze zahl ein. \n")
        continue
    if tipp <1 or tipp >99 :
        print("die zahl muss zwischen 1 und 99 liegen \n")
        continue
    versuche +=1
    if tipp < geheimzahl :
        print("zu niedrig! versuch es noch einmal. \n")
    elif tipp > geheimzahl :
        print("zu hoch! versuch es noch einmal. \n")
    else :
        print(f"glückwunsch! du hast die zahl {geheimzahl} in {versuche} versuchen erraten!")
        break











#ausaufgabe 02: „Schere, Stein, Papier“ in Python (random):
 
##Schreiben Sie ein Konsolen-Spiel, bei dem ein Spieler unendlich viele Runden „Schere, Stein, Papier“ gegen den Computer spielen kann, bis er das Spiel bewusst beendet.
 
#- Der Computer wählt in jeder Runde zufällig zwischen „Schere“, „Stein“ oder „Papier“ aus.
#- Der Spieler gibt seine Wahl per Text ein. Die Eingabe muss tolerant gegenüber Groß- und Kleinschreibung sein (z. B. schere wird zu Schere).
#- Ungültige Eingaben werden abgefangen und die Abfrage wiederholt.
#- Das Programm prüft auf Unentschieden, Sieg oder Niederlage gibt das Ergebnis aus.
#- Bei der Eingabe 'Ende' stoppt das Spiel mit einer Abschiedsmeldung.
#hat Kontextmenü


