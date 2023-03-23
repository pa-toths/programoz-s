#ord
#A ord()függvény egy megadott karakter unicode kódját képviselő számot adja vissza.
x = ord("a")
print(x)
 #chr()
 #A chr()függvény a megadott unicode-ot képviselő karaktert adja vissza.
x = chr(97)

#min()
#A min()függvény a legalacsonyabb értékű elemet, vagy a legalacsonyabb értékű elemet adja vissza az iterációban.
#Ha az értékek karakterláncok, akkor ábécé szerinti összehasonlítás történik.
x = min(5, 10)

#max()
#A max()függvény a legmagasabb értékű elemet, vagy a legmagasabb értékű elemet adja vissza az iterálható elemben.
#Ha az értékek karakterláncok, akkor ábécé szerinti összehasonlítás történik.
x = max(5, 10)

# index()
#A index()metódus megkeresi a megadott érték első előfordulását.
#A index()metódus kivételt jelent, ha az érték nem található.
#A index()metódus szinte megegyezik a find() metódussal, csak annyi a különbség, hogy a find() metódus -1-et ad vissza, ha nem található az érték. (Lásd a példát lent)

txt = "Hello, welcome to my world."

x = txt.index("welcome")

print(x)

#list()
#A list()függvény egy lista objektumot hoz létre.
#A listaobjektum egy gyűjtemény, amely rendezett és változtatható.
#A listáról bővebben a Python-listák fejezetben olvashat .

x = list(('apple', 'banana', 'cherry'))