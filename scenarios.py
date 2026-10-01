import pyfiglet
from functions import zeige_balken
from functions import status_prüfen
import random
from functions import bildschirm_leeren
from functions import optionen_mischen
from ui import go_banner
from ui import animal
from ui import game_logo
from ui import art
from ui import finish_banner
from ui import rahmen
from ui import abspann

def start(name, leben, ausdauer):
    print(game_logo)
    print()
    print (zeige_balken(leben, "Leben"))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    print()

    rahmen([    
         "",
        "Du erwachst an einem Strand," + " " + name + ".",
        "Dein Schädel dröhnt und Du weißt nicht, wie Du hierher gekommen bist.",
        "Du siehst Dich um, hinter Dir das offene Meer,",
        "vor Dir ein dichter Dschungel",
        "und links von Dir ein zerschelltes Boot.",
        "",
    ])
    print()

    optionen = [
        ("Das Boot untersuchen.", boot, 0, 10),
        ("In den Dschungel gehen.", dschungel, 0, 20),
        ("Im Meer schwimmen.", hai, 0, 0) 
    ]

    optionen = optionen_mischen(optionen)

    while True:
        print("Was machst Du, " + name + "?")

        for nummer, option in enumerate(optionen, 1):
                    print(f"{nummer}: {option[0]}")

        auswahl = input("Deine Wahl: ")

        if auswahl in ["1", "2", "3"]:

            option = optionen[int(auswahl) - 1]

            leben -= option[2]
            ausdauer -= option[3]

            nächstes_szenario = option[1]

            status_prüfen(leben, ausdauer) 
            bildschirm_leeren()
            nächstes_szenario(name, leben, ausdauer)

        else:
            print("Ungültige Eingabe!")
            continue

def dschungel(name, leben, ausdauer):
    print(game_logo)
    print()
    print(zeige_balken(leben, "Leben" ))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    print()
    rahmen([
    "",
    "Der Weg durch den Dschungel ist lang und schwieriger als gedacht.",
    "Du kämpfst Dich durch das Dickicht,",
    "findest einen Dschungelpfad und folgst ihm.",
    "Nach einiger Zeit kommt eine Weggabelung.",
    "Du siehst einen Fluss, hohes Gras und eine dunkle Höhle.",
    "",
    ])
    print()

    optionen = [
        ("Gehst Du den Fluss entlang?", hütte, 0, 10),
        ("Durch das hohe Gras gehen.", gras, 10, 20),
        ("In die dunkle Höhle gehen.", None, 100, 100)
    ]

    optionen = optionen_mischen(optionen)

    while True:
        print("Was machst Du, " + name + "?")

        for nummer, option in enumerate(optionen, 1):
                    print(f"{nummer}: {option[0]}")

        auswahl = input("Deine Wahl: ")

        if auswahl in ["1", "2", "3"]:

            option = optionen[int(auswahl) - 1]

            leben -= option[2]
            ausdauer -= option[3]

            nächstes_szenario = option[1]

            if nächstes_szenario is None:
                bildschirm_leeren()
                print(game_logo)
                print()
                print(zeige_balken(leben, "Leben"))
                print()
                print(zeige_balken(ausdauer, "Ausdauer"))
                print()
                rahmen([
                "",
                "\033[91m" + name + " Wirklich? Ohne Ausrüstung in eine DUNKLE Höhle?" + "\033[0m",
                "\033[91m" + "Du stolperst über einen Felsen und brichst Dir das Genick." + "\033[0m",
               "",
                ])
                print()
                print(go_banner)
                print()
                input("\nDrücke ENTER zum Beenden...")
                exit()

            status_prüfen(leben, ausdauer) 
            bildschirm_leeren()
            nächstes_szenario(name, leben, ausdauer)

        else:
            print("Ungültige Eingabe!")
            continue
  
def boot(name, leben, ausdauer):
    print(game_logo)
    print()
    print (zeige_balken(leben, "Leben"))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    
    print()
    rahmen([
    "",
    "Du gehst den Strand entlang bis Du an ein kleines Wrack",
    "eines Fischerbootes gelangst.",
    "Vorsichtig gehst Du an Bord und siehst Dich um.",
    "Das Boot sieht schwer mitgenommen aus, als läge es",
    "schon Jahre hier an diesem Strand.",
    "Kisten und Möbel liegen umgestürzt auf dem Boden.",
    "In einer der Kisten entdeckst Du eine Karte,",
    "die einen Weg zu einer Hütte beschreibt.",
    "Eine kleine Schale erregt Deine Aufmerksamkeit!",
    "Eine handvoll, gelb-rötlicher Früchte liegen darin.",
    "Du hast solche Früchte noch nie gesehen,",
    "aber ihr Geruch ist betörend.",
    "",
    ])
    print()

    optionen = [
        ("Du nimmst die Karte und siehst sie Dir an.", hütte, 0, 10),
        ("Du gehst doch im Meer schwimmen, um Dich abzukühlen.", hai, 0, 0),
        ("Dein Magen knurrt und Du isst die Frucht. ", None, 100, 100)
    ]

    optionen = optionen_mischen(optionen)

    while True:
        print("Was machst Du, " + name + "?")

        for nummer, option in enumerate(optionen, 1):
                    print(f"{nummer}: {option[0]}")

        auswahl = input("Deine Wahl: ")

        if auswahl in ["1", "2", "3"]:

            option = optionen[int(auswahl) - 1]

            leben -= option[2]
            ausdauer -= option[3]

            nächstes_szenario = option[1]

            if nächstes_szenario is None:
                bildschirm_leeren()
                print(game_logo)
                print()
                print(zeige_balken(leben, "Leben"))
                print()
                print(zeige_balken(ausdauer, "Ausdauer"))
                print()
                rahmen([
                "",
                "\033[91m" + name + ", " + "wirklich? Du beißt in eine Dir UNBEKANNTE Frucht?" + "\033[0m",
                "\033[91m" + "Natürlich ist sie giftig... Was genau hast Du erwartet?" + "\033[0m",
                "",
                ])
                print()
                print(go_banner)
                print()
                input("\nDrücke ENTER zum Beenden...")
                exit()

            status_prüfen(leben, ausdauer)
            bildschirm_leeren()
            nächstes_szenario(name, leben, ausdauer)
           

        else:
            print("Ungültige Eingabe!")
            continue

def hütte(name, leben, ausdauer):
    print(game_logo)
    print()
    print (zeige_balken(leben, "Leben" ))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    print()
    
    rahmen([  
    "",
    "Du gelangst, nach einem langen Fussmarsch,",
    "an eine beinahe idyllische Lichtung.",
    "Eine kleine Holzhütte, die schon Jahrzehnte",
    "hier zu stehen scheint.",
    "Obwohl die Hütte verlassen wirkt,",
    "brennt hinter einem der Fenster ",
    "schwaches Licht.",
    "Der Wind trägt das Knarren der Holzbalken zu Dir herüber.",
    "Für einen Moment scheint alles friedlich zu sein,",
    "doch dann hörst Du aus dem Wald",
    "hinter der Hütte ein seltsames Rascheln.",
    "Deine Beine schmerzen von der Reise",
    "und Dein Magen knurrt vor Hunger.",
    "Die Hütte könnte Schutz, Nahrung oder Antworten bieten!",
    "Du brauchst einen besseren Überblick,",
    "doch Büsche und Bäume nehmen Dir die Sicht.",
    "Trotz aller Mühe gelingt es Dir nicht",
    "vom Boden aus einen besseren Überblick zu erhalten.",
    "",
    ])
    print()
    
    optionen = [
        ("Du untersuchst die Hütte.", hütte_untersuchen, 0, 10),
        ("Das Geräusch verfolgen.", tier, 0, 0),
        ("Auf das Dach der Hütte klettern.", None, 100, 100)
    ]
    optionen = optionen_mischen(optionen)

    while True:
        print("Was machst Du, " + name + "?")

        for nummer, option in enumerate(optionen, 1):
                    print(f"{nummer}: {option[0]}")

        auswahl = input("Deine Wahl: ")

        if auswahl in ["1", "2", "3"]:

            option = optionen[int(auswahl) - 1]

            leben -= option[2]
            ausdauer -= option[3]

            nächstes_szenario = option[1]

            if nächstes_szenario is None:
                bildschirm_leeren()
                print(game_logo)
                print()
                print(zeige_balken(leben, "Leben"))
                print()
                print(zeige_balken(ausdauer, "Ausdauer"))
                print()
                rahmen([
                "",
                "\033[91m" + "Es knackt und knirscht.. Das Dach ist morsch" +"\033[0m",
                "\033[91m" + name + ", " + "wirklich? Du beißt in eine Dir UNBEKANNTE Frucht?" + "\033[0m",
                "",
                ])
                print()
                print(go_banner)
                input("\nDrücke ENTER zum Beenden...")
                exit()

            status_prüfen(leben, ausdauer)     
            bildschirm_leeren()
            nächstes_szenario(name, leben, ausdauer)

        else:
            print("Ungültige Eingabe!")
            continue

def gras(name, leben, ausdauer):
    print(game_logo)
    print()

    print (zeige_balken(leben, "Leben" ))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    print()

    rahmen([
    "",
    "Du gehst durch das hohe Gras und verletzt Dich leicht an Dornenbüschen.",
    "Ein stechender Schmerz fährt durch Dein Bein,",
    "doch die Wunde scheint nicht tief zu sein.",
    "Während Du die Stelle betrachtest,",
    "bemerkst Du einen schmalen Trampelpfad,",
    "der sich zwischen den Büschen hindurchschlängelt. ",
    "Aus einem nahen Gebüsch dringt ein seltsames Rascheln.",
    "Es klingt, als würde sich etwas ",
    "oder jemand zwischen den Pflanzen bewegen.",
    "Die Sonne brennt erbarmungslos auf Dich herab",
    "und Deine Kräfte schwinden langsam.",
    "In der Nähe spendet eine große Dattelpalme ",
    "angenehmen Schatten.",
    "Ein kurzer Rastplatz könnte Dir neue Ausdauer verleihen",
    "und die Gelegenheit bieten, Deine Gedanken zu sammeln.",
    "Nur wenige Meter entfernt endet der",
    "Pfad an einer steilen Klippe.",
    "Tief unter Dir schlagen die Wellen gegen das Gestein.",
    "Der Sprung ins Meer erscheint riskant,",
    "könnte Dich jedoch schneller zu einem unbekannten ",
    "Teil der Insel bringen.",
    "",
    ])
    
    print()

    optionen = [
        ("Verfolgst Du das Geräusch in den Büschen?", tier, 0, 10),
        ("Du legst Dich unter die Palme und rastest.", rast, -10, -25),
        ("Springst Du über die Klippe ins Meer?", hai, 0, 0) 
    ]
    optionen = optionen_mischen(optionen)

    while True:
        print("Was machst Du, " + name + "?")

        for nummer, option in enumerate(optionen, 1):
                    print(f"{nummer}: {option[0]}")

        auswahl = input("Deine Wahl: ")

        if auswahl in ["1", "2", "3"]:
            option = optionen[int(auswahl) - 1]

            leben -= option[2]
            ausdauer -= option[3]

            nächstes_szenario = option[1]

            status_prüfen(leben, ausdauer) 
            bildschirm_leeren()
            nächstes_szenario(name, leben, ausdauer)

        else:
            print("Ungültige Eingabe!")
            continue

def hütte_untersuchen(name, leben, ausdauer):
    print(game_logo)
    print()
    print (zeige_balken(leben, "Leben" ))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    print()

    rahmen([
    "",   
    "Du betrittst die Hütte vorsichtig.",
    "Auf einem verstaubten Tisch liegt",
    "ein altes Funkgerät neben einigen leeren Konservendosen.",
    "Durch das Fenster entdeckst Du in der Ferne",
    "ein großes Schiff auf dem offenen Meer.",
    "Vielleicht ist es Deine Chance auf Rettung!",
    "Plötzlich hörst Du draußen ein Rascheln im Gebüsch.",
    "Gleichzeitig spürst Du die Erschöpfung",
    "des langen Marsches.",
    "Du musst eine Entscheidung treffen!",
    "",
    ])
    
    print()

    optionen = [
        ("Funkgerät untersuchen und benutzen?",funkgerät, 0, 10),
        ("Nach draußen gehen und das Geräusch verfolgen?.", tier, 0, 20),
        ("Von der Klippe springen und zum Schiff schwimmen.", hai, 0, 0)
    ]

    optionen = optionen_mischen(optionen)

    while True:
        print("Was machst Du, " + name + "?")

        for nummer, option in enumerate(optionen, 1):
                    print(f"{nummer}: {option[0]}")

        auswahl = input("Deine Wahl: ")

        if auswahl in ["1", "2", "3"]:

            option = optionen[int(auswahl) - 1]

            leben -= option[2]
            ausdauer -= option[3]

            nächstes_szenario = option[1]

            status_prüfen(leben, ausdauer) 
            bildschirm_leeren()
            nächstes_szenario(name, leben, ausdauer)
            
        else:
            print("Ungültige Eingabe!" )    
            continue    
           
def funkgerät(name, leben, ausdauer):
    print(game_logo)
    print()

    print (zeige_balken(leben, "Leben"))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))

    print()

    rahmen([
    "",
    "Mit zitternden Händen schaltest Du, " + name + ", " "das alte Funkgerät ein.",
    "Nach einigen Momenten gelingt es Dir, ein Signal zu empfangen",
    "und einen Notruf abzusetzen.",
    "Kurz darauf ändert das Schiff am Horizont seinen Kurs",
    "und steuert die Insel an.",
    "Wenig später erreicht ein Rettungsteam das Ufer",
    "und bringt Dich sicher an Bord.",
    "Als die Insel hinter Dir verschwindet, wird Dir klar,",
    "dass Du es geschafft hast.",
    "Dank deiner Entschlossenheit konntest Du Kontakt",
    "zur Außenwelt herstellen und gerettet werden!",
    "",
    ])
    print()
    print(finish_banner)
    abspann()
    input("\nDrücke ENTER zum Beenden...")
    exit()
         
def tier(name, leben, ausdauer):
    print(game_logo)
    print()

    print (zeige_balken(leben, "Leben"))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    print()

    rahmen([
    "",
    "Du siehst ein wildes Tier, Zähne gebleckt!",
    "Du hast keine Waffe, um Dich zu verteidigen.",
    "Panisch siehst Du Dich nach etwas um.",
    "Du siehst einen Stock, den Du als Waffe benutzen könntest.",
    "Das Tier kommt näher. Es faucht und Du weißt,",
    "dass Du schnell handeln musst.",
    "",
    ])
    print()

    optionen = [
        ("Den Stock nehmen und kämpfen.", tier_tod, 0, 0),
        ("Mit bloßen Händen kämpfen.", tier_tod, 0, 0),
        ("Fliehen und über die Klippe ins Meer springen.", hai, 0, 0) 
    ]

    optionen = optionen_mischen(optionen)

    while True:
        print("Was machst Du, " + name + "?")

        for nummer, option in enumerate(optionen, 1):
                    print(f"{nummer}: {option[0]}")

        auswahl = input("Deine Wahl: ")

        if auswahl in ["1", "2", "3"]:

            option = optionen[int(auswahl) - 1]

            leben -= option[2]
            ausdauer -= option[3]

            nächstes_szenario = option[1]
           
            status_prüfen(leben, ausdauer)    
            bildschirm_leeren()
            nächstes_szenario(name, leben, ausdauer)
           
        else:
            print("Ungültige Eingabe!")
            continue

def tier_tod(name, leben, ausdauer):
    #bildschirm_leeren()
    print(game_logo)
    leben -= 100
    ausdauer -= 100 
    print()
    print(zeige_balken(leben, "Leben"))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    print()
    rahmen([
    "",
    "\033[91m" + name + " " + "wurde zerfleischt!" + "\033[0m",
    "",
    ])
    print()
    print(animal)
    print()
    print(go_banner)
    input("\nDrücke ENTER zum Beenden...")
    exit()

def hai(name, leben, ausdauer):
    #bildschirm_leeren()
    print(game_logo)
    leben -= 100
    ausdauer -= 100
    print()
    print(zeige_balken(leben, "Leben"))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    print() 
    rahmen([
    "",
    "\033[91m" + name + " " + "wurde von einem Hai gefressen!" + "\033[0m",
    "",
    ])
    print()
    print(art)
    print()
    print(go_banner)
    input("\nDrücke ENTER zum Beenden...")
    exit()

def rast(name, leben, ausdauer):
    print(game_logo)
    print()
    print(zeige_balken(leben, "Leben"))
    print()
    print(zeige_balken(ausdauer, "Ausdauer"))
    print() 
    rahmen([
    "",
    name + ", " + "Du schläfst friedlich unter einer Dattelpalme.",
    "Du fühlst Dich erholt und wieder voller Tatendrang!",
    "Es muss einen Weg von dieser Insel geben!",
    "In weiter Ferne erkennst Du eine kleine Hütte am Horizont.",
    "Am anderen Ende deines kleinen Rastplatzes, könntest Du von der Klippe",
    "ins Meer springen und versuchen, in die Freiheit zu schwimmen.",
    "Doch wärend Du Dich umsiehst, ",
    "reißt Dich ein leises Knurren aus Deinen Gedanken.",
    "",
    ])
    print()

    optionen = [
            ("Du gehst zur Hütte.", hütte, 0, 15),
            ("Du folgst dem Knurren.", tier, 0, 5),
            ("Über die Klippe ins Meer springen.", hai, 0, 0) 
        ]
    optionen = optionen_mischen(optionen)
    
    while True:
        print("Was machst Du, " + name + "?")
    
        for nummer, option in enumerate(optionen, 1):
                        print(f"{nummer}: {option[0]}")
    
        auswahl = input("Deine Wahl: ")

        if auswahl in ["1", "2", "3"]:
            option = optionen[int(auswahl) - 1]

            leben -= option[2]
            ausdauer -= option[3]

            nächstes_szenario = option[1]

            # status_prüfen(leben, ausdauer) 
            bildschirm_leeren()
            nächstes_szenario(name, leben, ausdauer)

        else:
            print("Ungültige Eingabe!")
            continue
   