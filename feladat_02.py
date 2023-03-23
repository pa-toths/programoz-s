#lower()
#A lower()metódus egy olyan karakterláncot ad vissza, amelyben minden karakter kisbetű.
#A szimbólumokat és számokat figyelmen kívül hagyja.

txt = "Hello my FRIENDS"

x = txt.lower()

print(x)

#upper()
#A upper()metódus egy olyan karakterláncot ad vissza, amelyben minden karakter nagybetűs.
#A szimbólumokat és számokat figyelmen kívül hagyja.

txt = "Hello my friends"

x = txt.upper()

print(x)

#capitalize()
#A capitalize()metódus egy karakterláncot ad vissza, ahol az első karakter nagybetű, a többi pedig kisbetű.

txt = "hello, and welcome to my world."

x = txt.capitalize()

print (x)

#endswith()
#A endswith()metódus igaz értéket ad vissza, ha a karakterlánc a megadott értékkel végződik, ellenkező esetben False-t.

txt = "Hello, welcome to my world."

x = txt.endswith(".")

print(x)

txt = "Hello, welcome to my world."

x = txt.endswith("my world.")

print(x)

# find()
#A find()metódus megkeresi a megadott érték első előfordulását.
#A find()metódus -1-et ad vissza, ha az érték nem található.
#A find()metódus szinte megegyezik a index() metódussal, csak annyi a különbség, hogy a index() metódus kivételt vet fel, ha nem található az érték. (Lásd a példát lent)

txt = "Hello, welcome to my world."

x = txt.find("welcome")

print(x)

#isalnum()
#A isalnum()metódus igaz értéket ad vissza, ha az összes karakter alfanumerikus, azaz ábécé betűi (az) és számok (0-9).
#Példa olyan karakterekre, amelyek nem alfanumerikusak: (szóköz)!#%&? stb.

txt = "Company 12"

x = txt.isalnum()

print(x)

#isalpha()
#A isalpha()metódus igaz értéket ad vissza, ha az összes karakter ábécé betűje (az).
#Példa olyan karakterekre, amelyek nem ábécé betűi: (szóköz)!#%&? stb.

txt = "Company10"

x = txt.isalpha()

print(x)

#islower()
#A islower()metódus igaz értéket ad vissza, ha minden karakter kisbetűvel van írva, ellenkező esetben False-t.
#A számok, szimbólumok és szóközök nincsenek bejelölve, csak az ábécé karakterei.

a = "Hello world!"
b = "hello 123"
c = "mynameisPeter"

print(a.islower())
print(b.islower())
print(c.islower())

#join()
#A join()metódus az összes elemet iterálhatóvá teszi, és egyetlen karakterláncba egyesíti.
#Elválasztóként egy karakterláncot kell megadni.

myDict = {"name": "John", "country": "Norway"}
mySeparator = "TEST"

x = mySeparator.join(myDict)

print(x)

# replace()
#A replace()metódus lecserél egy megadott kifejezést egy másik megadott kifejezésre.
txt = "one one was a race horse, two two was one too."

x = txt.replace("one", "three")

print(x)

#rfind()
#A rfind()metódus megkeresi a megadott érték utolsó előfordulását.
#A rfind()metódus -1-et ad vissza, ha az érték nem található.
#A rfind()módszer majdnem megegyezik a rindex() módszerrel. Lásd alább a példát.

txt = "Hello, welcome to my world."

x = txt.rfind("e", 5, 10)

print(x)

#rstrip()
#A rstrip()metódus eltávolítja a záró karaktereket (a karakterlánc végén lévő karaktereket), a szóköz az alapértelmezett eltávolítandó karakter.

txt = "     banana     "

x = txt.rstrip()

print("of all fruits", x, "is my favorite")

#startswith()
#A startswith()metódus igaz értéket ad vissza, ha a karakterlánc a megadott értékkel kezdődik, ellenkező esetben False-t.

txt = "Hello, welcome to my world."

x = txt.startswith("Hello")

print(x)

#strip()
#A strip()metódus eltávolítja a kezdő (szóköz az elején) és a záró (szóköz a végén) karaktereket (a szóköz az eltávolítandó alapértelmezett kezdő karakter).

txt = ",,,,,rrttgg.....banana....rrr"

x = txt.strip(",.grt")

print(x)
#swapcase() 
#A swapcase()metódus egy karakterláncot ad vissza, ahol az összes nagybetű kisbetű, és fordítva.
txt = "Hello My Name Is PETER"

x = txt.swapcase()

print(x)

# title()
#A title()metódus egy karakterláncot ad vissza, ahol minden szó első karaktere nagybetű. Mint egy fejléc vagy egy cím.
#Ha a szó számot vagy szimbólumot tartalmaz, az utána lévő első betű nagybetűvé alakul. 
txt = "Welcome to my world"

x = txt.title()

print(x)

# center()
#A center()metódus középre igazítja a karakterláncot, és egy megadott karaktert használ (a szóköz az alapértelmezett) kitöltési karakterként.

txt = "banana"

x = txt.center(20)

print(x)