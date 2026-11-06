import csv
liste_csv = []

try:
    with open("kundeInfos.csv", mode="r", encoding="utf-8", newline="") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            liste_csv.append(row)
except FileNotFoundError:
    print("error: file not found")

print(liste_csv[1][1])

dict_csv=[]
try:
    with open("kundeInfos.csv",mode="r",encoding="utf-8", newline="") as file :
        reader = csv.DictReader(file, delimiter=";")
        for row in reader :
            dict_csv.append(row)
except FileNotFoundError:
    print("error: file not found.")

print(dict_csv)