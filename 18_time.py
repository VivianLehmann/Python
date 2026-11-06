import time
import random 

# modul time : sehr maschinennah, einfachen unix - zeitstempel
# ideal für : messungen von code - laufzeit

# 1) programm pausiere mit time.sleep()

def countdown(sekunden) :
    print("countdown startet.....")
    for i in range(sekunden,0,-1) :
        print(f"noch{i} sekunden....", end="\r")     # \r= carriage return
        time.sleep(1)
    print("zeit abgelaufen")

#countdown(5)

def draw_art(size): 
    for i in range(size):
        zeichen = random.choice(["^","°"])
        print(zeichen, end="",flush=True)
        time.sleep(0.1)

#draw_art(50)


#laufzeit messen mit time.perf_counter()
start_zeit =time.perf_counter()

#print("code wir ausgeführt...")
time.sleep(1)

end_zeit = time.perf_counter()
laufzeit = end_zeit - start_zeit
#print(f"das programm hat {laufzeit} sekundengebraucht.")

#####################################################################

# aufgabe : listen vs. sets

größe = 10_000_000 
daten_liste = list(range(größe))
daten_set = set(daten_liste)

such_element = 9_999_999

print("suche startet....")

#messung 1 liste
start_liste = time.perf_counter()
gefunden = such_element in daten_liste
end_liste = time.perf_counter()
zeit_liste = end_liste - start_liste
print(f"liste:{zeit_liste:.6f}sekunden")

# messung 2 : set
start_set = time.perf_counter()
gefunden = such_element in daten_set
end_set = time.perf_counter()
zeit_set = end_set - start_set
print(f"set:{zeit_set:.6f}sekunden")