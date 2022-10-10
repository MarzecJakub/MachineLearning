# -*- coding: utf-8 -*-
"""
Created on Mon Oct 10 14:38:04 2022

@author: Marzec
"""

#zad1
def przywitanie(name :str, surname :str) -> str:
    return f"Czesc {name} {surname}!"

wynik = przywitanie("Jakub", "Marzec")
print(wynik)


#zad2
def mnozenie(l1 :int, l2 :int):
    return l1*l2

print(mnozenie(4,2))


#zad3
def sprawdzCzyParzysta(liczba) -> bool:
    if liczba%2==0: return True
    else: return False

wynik = sprawdzCzyParzysta(6)
if wynik == True:
    print("Liczba parzysta")
else:
    print("Liczba nieparzysta")
    

#zad4
def sprawdzWartosci(l1 :int, l2 :int, l3 :int) -> bool:
    if l1+l2 >= 3:
        return True
    else:
        return False
    
print(sprawdzWartosci(1, 11, 4))


#zad5
def sprawdzZawieranie(lista :list, liczba :int) -> bool:
    if liczba in lista:
        return True
    else:
        return False

print(sprawdzZawieranie([1,2,3,4,5], 3))


#zad6
def laczenie(lista1 :list, lista2 :list) -> list:
    lista = lista1 + lista2
    listaUnikat = set(lista)
    
    listaUnikat = [x**3 for x in listaUnikat] 
    
    return listaUnikat
    
print(laczenie([1,2,3],[3,2,1,5,4]))
    
    
    
    
    