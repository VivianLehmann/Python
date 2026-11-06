import random

# Beispiel 01 : Name Generator

vorsilben = ["Ar","Bra","Gral","Tho"]
mittelsilben = ["da","do","rin","ma"]
nachsilben = ["kus","nus","rion","li"]

name = random.choice(vorsilben) + random.choice(mittelsilben) + random.choice(nachsilben)
print(f"dein neue charakter heißt : {name}")

######################################################################################

# beispiel 02 : speisekarte (dict) ein gericht wählen, da günstig ist

speisekarte = {
    "pizza":"günstig", "sushi":"teuer", "döner":"günstig",
    "burger":"mittel", "tapioca":"teuer","steak":"teuer"
}

auswahl =[]
for gericht, preis in speisekarte.items():
    if preis == "günstig":
        auswahl.append(gericht)

print(auswahl)
print(f"heute gibt es : {random.choice(auswahl)}")

#######################################################################################

# beispiel 03 : rabat - würfler 

rabatte = [5,10,20,50]
wahrscheinlichkeiten = [0.50, 0.35, 0.13, 0.02]

gewinn = random.choices(rabatte,weights=wahrscheinlichkeiten,k=1)
print(f"du erhälst{gewinn[0]}% rabatt!")

############################################################################################

# beispiel 04: zufällige farbe generieren

def draw_monkey():
    text = "@('_')@"
    print(f"\033[38;2;255;0;0m{text}\033[0m")

draw_monkey()
