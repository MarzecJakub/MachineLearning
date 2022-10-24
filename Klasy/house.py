# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 14:17:50 2022

@author: Marzec
"""


import Klasy.property as prop


class House(prop.Property):
    def __init__(self, area, rooms, price, address, plot: int):
        super().__init__(area, rooms, price, address)
        self.plot = plot

    def __str__(self):
        return f"""--Dom--\nArea: {self.area}\nRooms:{self.rooms}
Price:{self.price}\nAdress:{self.address}\nPlot:{self.plot}"""
