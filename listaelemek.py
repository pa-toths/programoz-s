'''
honapok = ['január', 'február', 'március', 'április', 'május', 'június']

for honap in honapok:
 honap = honap.upper()
'''


szamok = [1, 7, 8, 10, 12, 9, 3]

for szam in szamok:
    if szam % 2 == 0:
        print('Megvan az első páros szám a listában:')
        print(szam)
        break
print('Program vége')
