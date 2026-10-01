#TEST - Projektarbeit Nedim Jasikovic & Roy Tsah
import scenarios
from functions import zeige_balken
from ui import chris
from ui import game_logo
from functions import bildschirm_leeren

#Variablen
leben = 100
ausdauer = 100

print(game_logo)

#startloop
while True:
    start = input("Starten? (ja / nein) ")

    if start == "ja":
        print("Spiel startet!")
        break

    elif start == "nein":
        print("Spiel beendet!")
        exit()

    else:
        print("Ungültige Eingabe. Bitte ja oder nein eingeben." )
        continue
    
name = input("Bitte gib Deinen Namen ein: ")
while True:
    if len(name) <= 15:
        print("Hallo, " + name + "! Willkommen auf" + "\033[1;38;5;226m" + " DOOM ISLAND" + "\033[0m" + "!")
        break
    else:
        print("Dein Name ist zu lang! Die maximale Länge beträgt 15 Zeichen.")
        print("Bitte gib Deinen Namen erneut ein: ") 
        name = input()
print()

if name == "chris" or name == "Chris":
    print(chris)
    input("\nDrücke ENTER zum Beenden...")
    exit()

else:
    print(zeige_balken(leben, "Leben"))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    print()

import scenarios
bildschirm_leeren()
scenarios.start(name, leben, ausdauer)
