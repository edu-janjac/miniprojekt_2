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
    antal_gissningar = 0
    
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
    for plats, post in enumerate(sorterad, start=1):
        print(f"{plats}. {post['namn']} - {post['gissningar']} gissningar")


# === HUVUDPROGRAM ===

def huvudprogram():
    highscore_lista = ladda_highscore()

    while True:
        print("\n=== HIGH OR LOW ===")
        print("1. spela ny omgång")
        print("2. visa highscore")
        print("3. avsluta")

        val = input("välj alternativ: ").strip()

        if val == "1":
            antal = spela_omgang()
            namn = input("ange ditt namn: ").strip()
            if not namn:
                namn = "anonym"
            highscore_lista.append({"namn": namn, "gissningar": antal})
            spara_highscore(highscore_lista)
            print("din poäng har sparats")
        elif val == "2":
            visa_highscore(highscore_lista)
        elif val == "3":
            print("bye bye")
            break
        else:
            print("ogiltig val, försök igen")


if __name__ == "__main__":
    huvudprogram()