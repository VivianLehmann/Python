import csv

csv_path = "deutschebahn.csv"
trains = []

def analyze_delays(trains) :
try:
    with open(csv_path, mode="r", encoding="UTF-8", newline="") as file :
        reader = csv.DictReader(file, delimiter=",")
        for row in reader :
            trains.append(row)
except FileNotFoundError : 
    

print(trains)
delayed_trains, avg_delay = analyze_delays(trains)
print(f"züge mit verspätung: {delayed_trains}")
print(f"durchschnittliche verspätung :{avg_delay:2f}minuten")
