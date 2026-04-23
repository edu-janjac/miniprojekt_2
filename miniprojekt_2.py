"""
Projekt 2: Högt/lågt-spel med highscore
Ett spel där användaren gissar ett slumpmässigt tal.
Highscore sparas i JSON-format.
"""

import random
import json

# === FILHANTERING ===

def ladda_highscore(filnamn="highscore.json"):
    try:
        with open(filnamn, "r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        return []


def spara_highscore(highscore_lista, filnamn="highscore.json"):
    with open(filnamn, "w", encoding="utf-8") as f:
        json.dump(highscore_lista, f, indent=4, ensure_ascii=False)

# === SPELMECKANIK ===

def spela_omgang():
    
    okända_talet = random.randint(1, 100)
    gissningar = 0
    
    print("\nGissa talet mellan 1 och 100")

    while True:
        try:
            gissning = int(input("Din gissning: "))
        except ValueError:
            print("Ange ett heltal.")
            continue
        
        antal_gissningar += 1

        if gissning < okända_talet:
            print("för lågt")
        elif gissning > okända_talet:
            print("för högt")
        else:
            print(f"korrekt, du gissade på {antal_gissningar} försök")
            return antal_gissningar

def visa_highscore(highscore_lista):
    if not highscore_lista:
        print("\ningen highscore än.")
        return
    
    sorterad = sorted(highscore_lista, key=lambda x: x["gissningar"])

    print("\n=== HIGHSCORE ===")
    for plats, post in enumerate(sorted, start=1):
        print(f"{plats}. {post['namn']} - {post['gissningar']} gissningar")


# === HUVUDPROGRAM ===

def huvudprogram():
    """
    Huvudprogrammet som styr menyn och programflödet.
    """
    # TODO: Implementera huvudprogrammet
    # 1. Ladda highscore med ladda_highscore()
    # 2. Skapa en while-loop som visar menyn
    # 3. Menyn ska ha alternativen:
    #    1. Spela ny omgång
    #    2. Visa highscore
    #    3. Avsluta
    # 4. Vid val 1:
    #    - Anropa spela_omgang() för att få antalet gissningar
    #    - Fråga efter spelarens namn
    #    - Skapa en dictionary {"namn": namn, "gissningar": antal}
    #    - Lägg till i highscore-listan
    #    - Spara med spara_highscore()
    # 5. Vid val 2: anropa visa_highscore()
    # 6. Vid val 3: avsluta loopen
    pass


# Starta programmet om filen körs direkt
if __name__ == "__main__":
    huvudprogram()