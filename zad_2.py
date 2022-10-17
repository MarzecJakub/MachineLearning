#zad2a
def wyswietl(lista):
    for el in lista:
        print(el)


lista = ["Ola", "Jakub", "Agata", "Michał", "Kacper"]
wyswietl(lista)


#zad2b
liczby = [1, 2, 3, 4, 5]


def wyswietl(liczby):
    for i in range(len(liczby)):
        liczby[i] = liczby[i] * 2
    return liczby


print(wyswietl(liczby))


liczby = [1, 2, 3, 4, 5]


def wyswietlv2(liczby):
    liczby = [el*2 for el in liczby]
    return liczby


print(wyswietlv2(liczby))


#zad2c
def wyswietlParzyste(lista):
    for i in range(len(lista)):
        if lista[i] % 2 == 0:
            print(lista[i])


lista = [2, 3, 4, 6, 8, 11, 10, 15, 17, 12]
wyswietlParzyste(lista)


#zad2d
def wyswietlCoDruga(lista):
    for el in lista[::2]:
        print(el)


lista = [2, 3, 4, 6, 8, 11, 10, 15, 17, 12]
wyswietlCoDruga(lista)
