#A ami órán igazából újdonságnak a for loopokat vettük,
#de ma jeleztétek sokan, hogy nem igazán maradtak meg a korábbi pythonos cuccok sem.
#emiatt azok a részek is ki lesznek kommentelve


#pythonban - javascripthez hasonlóan - nem kell megadni a típusát az adott változónak.

a = 1
b = "bé"
nem_egesz_szam = 3.141597538389
igaz = True

#pythonban így kell változót deklarálni. változónév = érték. Jelen esetekben az a értéke 1, a b értéke pedig a szó "bé"
#a nyelv ki tudja találni hogy at string, integer, float, vagy boolean 

#floatról még nem volt szó, de az igazából olyan mint a double.
#boolean pedig az igaz, vagy hamisat jelenti. 

tort1 = 3.3
integer = 9

kevert_osszeg = tort1 + integer
print(kevert_osszeg)

#ha azt lefuttatjátok, akkor látjátok, hogy a pythonnak nincs baja abból, 
#ha nem egész számot akarsz egészhez adni.

print(int(tort1))

#float és int közt is egyszerű a váltás

#a python egy általános programozási nyelv, viszont gyakran használják adatok feldolgozására

#ilyen egyszerű pythonban lekérni adatot a felhasználótól.
nev = input("Hogy hívnak?")
kor = input("Hány éves vagy?")
lista = [] #listát is lehet deklarálni, de arról majd máskor

#szuletesi_ev = 2022 - kor ez így viszont nem jó, mert az input alapjáraton string
#mi pedig vagy floattal, vagy integerrel tudunk dolgozni. Ezt egy szimpla int()-vel tudunk orvosolni
#ha mi ezt utána ki is akarjuk iratni, akkor vissza kell stringgé alakítani.
#Ez moderáltan idegesítő lesz
szuletesi_ev = 2022 - int(kor)
print("Szóval a neved "+nev+"és "+kor+"éves vagy? akkor "+str(szuletesi_ev)+"-ben születtél.")


#emellett vettük a funkciókat, vagy metódusokat. Fogalmam sincs mi a helyes név
#én functionként fogomnevezni őket

def functionName():
    print("hívta a function name funkciót")

functionName()

#itt a szintaktika az, hogy 
# def név(paraméterek):
#    #kód

#alakítsuk az eddigi példát functionné

def pelda(nev, kor):
    szuletesi_ev = 2022 - int(kor)
    return nev+" "+str(szuletesi_ev)+"-ben született."

print(pelda("zalán", 49))



#mai órán a for loopokkal foglalkoztunk. 
#Ez egy hasznos dolog olyanokra, mint betüre bontás, 

for i in "dolgok":
    print(i)

#lista elemek kiirása
for i in ["egy","két","há","négy","öt", "hat"]:
    print(i)

#lista elem számoltatás
for i in range(len(["egy","két","há","négy","öt", "hat"])):
    print(i)

#x alkalomszot lefuttatni valamit
for i in range(1, 10):
    print(i)

#nem muszály 
#for i in ____-nek lennie, lehetne for x in ____ vagy for cica in ____, 
#de a for i verzió a norma

#a mai órán kitaláltunk 
#valami agyonkomplikánt megoldást a hatványozás függvényre
#ez valami ilyesmi módon nézett ki

def hatvany(hatvanyalap, hatvanykitevo):
    alap = hatvanyalap
    for i in range(1, hatvanykitevo):
        hatvanyalap = hatvanyalap*alap

    return hatvanyalap


szam1 = int(input("melyik számot emeljük >>>"))
szam2 = int(input("a hányadikra >>>"))
print(str(szam1)+" a "+str(szam2)+"-dik hatványon : "+str(hatvany(szam1, szam2)))


#ez egy picit nehezen átlátható, ha kell segítség szívesen elmagyarázom