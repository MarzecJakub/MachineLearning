# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:19:23 2022

@author: Marzec
"""


import Klasy.property as prop


class Flat(prop.Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor

    def __str__(self):
        return f"""--Mieszkanie--\nArea: {self.area}\nRooms:{self.rooms}
Price:{self.price}\nAdress:{self.address}\nFloor:{self.floor}"""
