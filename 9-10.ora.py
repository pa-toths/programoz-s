#első feladat 9.dk
from os import sep


idei_ev = 2022
print(type(idei_ev))
print( "azidei_ev változó értéke" , idei_ev , sep='--->')
felhasznalo_kora = input("hány éves vagy?")
print(' a felhasználók kora változó ', type(felhasznalo_kora))
print('Te most' , felhasznalo_kora , 'éves vagy.')
felhasznalo_kora = int(felhasznalo_kora)
születési_év = idei_ev - felhasznalo_kora
print('Ekkor születtél: ' , születési_év, '.', sep='')
