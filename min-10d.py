lista = [12 , 5 , 4, 8, 11, 10, 6, 13]
min = lista[0]
max = lista[0]
for szam in lista :
    if szam < min :
        min = szam
    if szam > max:
        max = szam
print('A legkisebb szam! ' ,min )
print('A legnagyobb szam! ' ,max)