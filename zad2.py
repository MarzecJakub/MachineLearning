class Student:
    def __init__(self, name, numer):
        self.name = name
        self.numer = numer

    def __str__(self):
        return f"Imie: {self.name} ID: {self.numer}"


class Library:
    def __init__(self, city, street, zip_code, open_hours: str, phone):
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.open_hours = open_hours
        self.phone = phone

    def __str__(self):
        return f"""Miasto: {self.city}, Ulica: {self.street}, Kod pocztowy: {self.zip_code}
Godziny otwarcia: {self.open_hours}, Tel: {self.phone}"""


class Employee:
    def __init__(self, first_name, last_name, hire_date, birth_date, city, street, zip_code, phone):
        self.first_name = first_name
        self.last_name = last_name
        self.hire_date = hire_date
        self.birth_date = birth_date
        self.city = city
        self.street = street
        self.zip_code = zip_code
        self.phone = phone

    def __str__(self):
        return f"""Imie: {self.first_name}, Nazwisko: {self.last_name}, Zatrudniony: {self.hire_date},
Urodzony: {self.birth_date}, Miasto: {self.city}, Ulica: {self.street}, Kod pocztowy: {self.zip_code}, Tel: {self.phone}"""


class Book:
    def __init__(self, library, publication_date, author_name, author_surname, number_of_pages):
        self.library = library
        self.publication_date = publication_date
        self.author_name = author_name
        self.author_surname = author_surname
        self.number_of_pages = number_of_pages

    def __str__(self):
        return f"Biblioteka: {self.library}\nData publikacji: {self.publication_date}, Imie autora: {self.author_name}, Nazwisko autora: {self.author_surname},Ilosc stron: {self.number_of_pages}"


class Order:
    def __init__(self, employee, student, books: list, order_date):
        self.employee = employee
        self.student = student
        self.books = books
        self.order_date = order_date

    def __str__(self):
        ksiazki = ""
        for el in self.books:
            ksiazki += "---"
            ksiazki += el.__str__()
            ksiazki += "\n"
        return f"Pracownik:\n{self.employee}\nWypozyczajacy:\n{self.student}\nKsiążki:\n{ksiazki}Data: {self.order_date}"


Biblioteka1 = Library("Jastrzębie-Zdrój", "Opolska", "44-335", "8:00-16:00", "531692853")
Biblioteka2 = Library("Katowice", "Bankowa", "40-007", "8:00-16:00", "327865130")

Pracownik1 = Employee("Jan", "Nowak", "06-03-2020", "03-01-1993", "Jastrzębie-Zdrój", "Wrocławska", "44-335", "519283123")
Pracownik2 = Employee("Jakub", "Kowalski", "21-07-2015", "23-08-1991", "Katowice", "Bankowa", "40-007", "123848182")
Pracownik3 = Employee("Kacper", "Kowal", "05-06-2013", "03-11-1976", "Jastrzębie-Zdrój", "Wielkopolska", "44-335", "293108431")

Ksiazka1 = Book(Biblioteka1, "01-07-1900", "Henryk", "Sienkiewicz", "638")
Ksiazka2 = Book(Biblioteka1, "21-12-1890", "Henryk", "Sienkiewicz", "456")
Ksiazka3 = Book(Biblioteka2, "17-07-2019", "Jan", "Drabina", "120")
Ksiazka4 = Book(Biblioteka2, "09-11-2015", "Agata", "Christie", "250")
Ksiazka5 = Book(Biblioteka2, "04-08-2011", "All", "Dubai", "421")

Student1 = Student("Jakub", "144917")
Student2 = Student("Michal", "131234")
Student3 = Student("Agata", "124234")

lista = [Ksiazka1, Ksiazka2]
lista2 = [Ksiazka3, Ksiazka4, Ksiazka5]

Zamowienie1 = Order(Pracownik1, Student1, lista, "03-01-2022")
Zamowienie2 = Order(Pracownik2, Student2, lista2, "06-12-2021")

print(Zamowienie1)
print("==========================")
print(Zamowienie2)
