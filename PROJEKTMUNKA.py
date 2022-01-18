#Koncepció: Létrehozni egy olyan játékot, ahol 1-100-ig ki kell találni a számot. 5 próbálkozás után elmondjuk neki, hogy 50-100 között van-e, vagy 0-50 között, illetve levisszük a következő próbálkozások számát 3-ra. Ha ezek után se találta el, még jobban lekicsinyítjük a tartományt, amibe van a szám, illetve 5 próbálkozásra visszaemeljük. Ha ezután sem találta el, elmondjuk a megoldást.
import random
szam = random.randint(1,100)
tipp = int(input("Adjon meg egy számot 1-100 között:"))
for i in range(5):
    if tipp == szam:
        print("Gratulálok! Elsőre eltaláltad!")
    else: tipp = int(input("Adjon meg egy másik tippet:"))
print("Mivel nem találtad el 5 próbálkozásból, kicsit könnyítünk rajtad ;)")
if szam >= 50:
    print("A szám 50-100 között van!")
elif szam <= 50:
    print("A szám 0-50 között van!")
for i in range(3):
    tipp = int(input("Adjon meg egy tippet:"))
    if tipp == szam:
        print("Gratulálok! Kicsit nehezen, de eltaláltad!")
        break
print("Mivel még most sem találtad el, ezért még könnyebbé tesszük neked!")
if szam <= 50 and szam >= 30:
    print("A szám 50 és 30 között van!")
elif szam <= 30 and szam >= 0:
    print("A szám 0-30 között van!")
if szam <= 70 and szam >= 50:
    print("A szám 50-70 között van!")
elif szam <= 100 and szam >= 70:
    print("A szám 70-100 között van!")