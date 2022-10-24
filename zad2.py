from Klasy import library as lib
from Klasy import student2 as st2
from Klasy import employee as emp
from Klasy import book
from Klasy import order


Biblioteka1 = lib.Library("Jastrzębie-Zdrój", "Opolska", "44-335", "8:00-16:00", "531692853")
Biblioteka2 = lib.Library("Katowice", "Bankowa", "40-007", "8:00-16:00", "327865130")

Pracownik1 = emp.Employee("Jan", "Nowak", "06-03-2020", "03-01-1993", "Jastrzębie-Zdrój", "Wrocławska", "44-335", "519283123")
Pracownik2 = emp.Employee("Jakub", "Kowalski", "21-07-2015", "23-08-1991", "Katowice", "Bankowa", "40-007", "123848182")
Pracownik3 = emp.Employee("Kacper", "Kowal", "05-06-2013", "03-11-1976", "Jastrzębie-Zdrój", "Wielkopolska", "44-335", "293108431")

Ksiazka1 = book.Book(Biblioteka1, "01-07-1900", "Henryk", "Sienkiewicz", "638")
Ksiazka2 = book.Book(Biblioteka1, "21-12-1890", "Henryk", "Sienkiewicz", "456")
Ksiazka3 = book.Book(Biblioteka2, "17-07-2019", "Jan", "Drabina", "120")
Ksiazka4 = book.Book(Biblioteka2, "09-11-2015", "Agata", "Christie", "250")
Ksiazka5 = book.Book(Biblioteka2, "04-08-2011", "All", "Dubai", "421")

Student1 = st2.Student("Jakub", "144917")
Student2 = st2.Student("Michal", "131234")
Student3 = st2.Student("Agata", "124234")

lista = [Ksiazka1, Ksiazka2]
lista2 = [Ksiazka3, Ksiazka4, Ksiazka5]

Zamowienie1 = order.Order(Pracownik1, Student1, lista, "03-01-2022")
Zamowienie2 = order.Order(Pracownik2, Student2, lista2, "06-12-2021")

print(Zamowienie1)
print("==========================")
print(Zamowienie2)
