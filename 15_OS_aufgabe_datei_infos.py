import os

def finde_datei_infos(ordner_pfad): 
    groeßte_datei  = ""
    aelteste_datei =""
    max_groeße = -1
    min_zeit = float('inf')

    for eintrag in os.scandir(ordner_pfad):
        if eintrag.is_file(): 
            infos = eintrag.stat()

        if infos.st_size > max_groeße:
            max_groeße = infos.st_size
            groeßte_datei = eintrag.name

        if infos.st_birthtime < min_zeit :
            min_zeit = infos.st_birthtime
            aelteste_datei = eintrag.name

    return groeßte_datei , aelteste_datei

pfad ="."
groeße , alter = finde_datei_infos(pfad)
print(f"größte datei:{groeße}")
print(f"älteste datei:{alter}")