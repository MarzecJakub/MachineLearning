# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:17:32 2022

@author: Marzec
"""


class Property:
    def __init__(self, area, rooms: int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
