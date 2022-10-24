# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:08:52 2022

@author: Marzec
"""


class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_passed(self):
        if (sum(self.marks) / len(self.marks) > 50):
            return True
        else:
            return False
