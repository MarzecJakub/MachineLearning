# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:11:27 2022

@author: Marzec
"""


class Student:
    def __init__(self, name, numer):
        self.name = name
        self.numer = numer

    def __str__(self):
        return f"Imie: {self.name} ID: {self.numer}"
