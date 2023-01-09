magassag = int(input('kérem egy számot'))
szelesseg = int(input('Kérek még egy számot'))
T = szelesseg * magassag
if magassag > szelesseg:
    print('Álló', T )
elif magassag < szelesseg:
    print('Fekvő' ,T )
elif magassag == szelesseg:
    print('négyzet', T )
