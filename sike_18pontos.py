"""
def adatbekeres() :
    szo = None
    while szo != '':
        szo = input('Kerem nevét:')  
        print(f'A neve {szo} 10D osztály tanulója.')  


adatbekeres()
"""


def adatbekeres_break():
    while True:
        nev2= input("Kérek egy masiknevet: ")
        if nev2 == "":
            break
        print (f"Ez egy {nev2} masik nev")


adatbekeres_break()