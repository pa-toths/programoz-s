lista1 = [3,12,3,4,7,15,1]
lista2 = [1,3,5,7]

def osszegzes_tetele(lista_osszegzes):
   osszesen = 0 
   for szam in lista_osszegzes:
      osszesen = osszesen +szam 
   print ("A listában található összege : ",osszesen)

osszegzes_tetele(lista1)
osszegzes_tetele(lista2)
osszegzes_tetele ([10,20,30])