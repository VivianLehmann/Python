import random
import secrets                      #strong pseudo - random

# RANDOM IST NICHT WIRKLICH ZUFFÄLLIG 
# PRNG - Pseudozufallsgenerator 
# Algorithmus : mersenne - twister ->  vorhersehbar !!
# spieleenticklung, simulationen, 

z1 = random.random()                 #float zwischen 0.0 und < 1.0
print(z1)

#random.seed(20)
z2 = random.random()
z3 = random.random()
print(z2,z3)

z4 = random.uniform(2.5,10.5)
print(z4)

z5 = random.randrange(0,10,2)        #start, stopp, schrittweite
print(z5)

wuerfel = random.randrange(1,7)
print(wuerfel)

tiere = ["hund", "katze", "ameise", "elephant", "bär", "taube"]
print(random.choice(tiere))
print(random.choices(tiere,k=3))
print(random.sample(tiere,k=5))

tiere_backup = tiere.copy()
random.shuffle(tiere)               # "in-place" operatonen
print(tiere)

t1 =(1,2,3,4,5,6)
print(random.choice(t1))
s1 = "python"
print(random.choice(s1))

d1 = {"anna":28,"paula":32,"lukas":21}
zufall_schlüssel = random.choice(list(d1.keys()))
print(d1[zufall_schlüssel])
print(zufall_schlüssel)


####################################################################

zufallszahl = secrets.randbelow(10)
print(zufallszahl)
sicheres_token = secrets.token_hex(16)
print(sicheres_token)
print(secrets.choice(tiere))