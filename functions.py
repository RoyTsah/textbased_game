import random
import os
from ui import re
from ui import go_banner
from ui import game_logo
from ui import HERZ, BLITZ

def bildschirm_leeren():
    input("Drücke Enter, um fortzufahren")
    os.system("cls")

def zeige_balken(wert, beschriftung):
    wert = max(0, min(wert, 100))
    if beschriftung == "Leben":
        symbol = " \033[31m♥\033[0m"
    elif beschriftung == "Ausdauer":
        symbol = "⚡"
    voll = "█"
    leer = "░"
    Balkenlänge = 20

    volle_position = wert * Balkenlänge / 100
    leere_position = Balkenlänge - volle_position

    return symbol.ljust(1) + " " + (voll * int(volle_position)) + (leer * int(leere_position))

def status_prüfen(leben, ausdauer):

    if leben <= 0:

        bildschirm_leeren
        print(game_logo)
        print()
        print(zeige_balken(leben, "Leben"))
        print()
        print(zeige_balken(ausdauer, "Ausdauer"))
        print()
        print("Du bist gestorben!")
        print(go_banner)
        input("\nDrücke ENTER zum Beenden...")
        exit()

    elif ausdauer <= 0:

        bildschirm_leeren
        print(game_logo)
        print()
        print(zeige_balken(leben, "Leben"))
        print()
        print(zeige_balken(ausdauer, "Ausdauer"))
        print()
        print("Du bist erschöpft und kannst nicht mehr weitermachen!")
        print(go_banner)
        input("\nDrücke ENTER zum Beenden...")
        exit()

def optionen_mischen(optionen):
    random.shuffle(optionen)
    return optionen
