# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:13:24 2022

@author: Marzec
"""


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
