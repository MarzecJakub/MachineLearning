# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 15:05:12 2022

@author: Marzec
"""
import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

listaimg = ['img1.png','img2.png','img3.png','img4.png','img5.png']


def wyswietltekst(listaimg):
    for img in listaimg:
        print(pytesseract.image_to_string(cv2.imread(img)))



wyswietltekst(listaimg)