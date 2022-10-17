# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 14:52:59 2022

@author: Marzec
"""
#zadanie3

class Property:
    def __init__(self, area, rooms :int, price, address):
        self.area = area
        self.rooms = rooms
        self.price = price
        self.address = address
        
        
class House(Property):
    def __init__(self, area, rooms, price, address, plot :int):
        super().__init__(area, rooms, price, address)
        self.plot = plot
    
    def __str__(self):
        return f"--Dom--\nArea: {self.area}\nRooms:{self.rooms}\nPrice:{self.price}\nAdress:{self.address}\nPlot:{self.plot}"
        
    
class Flat(Property):
    def __init__(self, area, rooms, price, address, floor):
        super().__init__(area, rooms, price, address)
        self.floor = floor
        
    def __str__(self):
        return f"--Mieszkanie--\nArea: {self.area}\nRooms:{self.rooms}\nPrice:{self.price}\nAdress:{self.address}\nFloor:{self.floor}"

    

Dom = House("150m2", 10, 11000000, "Katowice ul.Budowlana 8", 1300)
Mieszkanie = Flat("60m2", 4, 600000, "Jastrzębie-Zdrój ul.Wrocławska 11/13", "60m2")

print(Dom)
print("==================")
print(Mieszkanie)