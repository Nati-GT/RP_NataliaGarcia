import sys
import typing
import PyQt5.QtWidgets as PyQt
from PyQt5 import QtCore, uic
from PyQt5.QtWidgets import QWidget
# from views.inter import principal

class principal(PyQt.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("views\interfaz_p.ui",self)
        self.convertir.clicked.connect(self.ConvertirDatos)
    
    def ConvertirDatos(self):
        if self.dec2bin.isChecked()  == True:
            resultado = int(self.valor.text())
            convercion = []
            while resultado > 0:
                residuo = resultado%2
                resultado = resultado//2
                convercion.append(residuo)
            convercion.reverse()
            text = str(convercion).replace(",","")
            text = text.replace("'","")
            text = text.replace("[","")
            text = text.replace("]","")
            text = text.replace(" ","")
            self.resultado.setText(text)

        elif self.dec2hex.isChecked() == True:
            resultado = int(self.valor.text())
            convercion = []
            while resultado > 0:
                residuo = resultado%16
                resultado = resultado//16
                if residuo == 10:
                    residuo = "A"
                elif residuo == 11:
                    residuo = "B"
                elif residuo == 12:
                    residuo = "C"
                elif residuo == 13:
                    residuo = "D"
                elif residuo == 14:
                    residuo = "E"
                elif residuo == 15:
                    residuo = "F"
                convercion.append(residuo)
            convercion.reverse()
            text = str(convercion).replace(",","")
            text = text.replace("'","")
            text = text.replace("[","")
            text = text.replace("]","")
            text = text
            self.resultado.setText(text)


        elif self.bin2dec.isChecked() == True:
            resultado = self.valor.text()
            convercion = []
            tot = []
            for i in resultado:
                convercion.append(i)
            for j in range(len(convercion)):
                    tot.append(int(convercion[j])*(2**(len(convercion)-int(j+1))))
            self.resultado.setText(str(sum(tot)))

        elif self.hex2dec.isChecked() == True:
            resultado = self.valor.text().lower()
            convercion = []
            tot = []
            for i in resultado:
                if i == "a":
                    i = 10
                elif i == "b":
                    i = 11
                elif i == "c":
                    i = 12
                elif i == "d":
                    i = 13
                elif i == "e":
                    i = 14
                elif i == "f":
                    i = 15
                convercion.append(i)
            for j in range(len(convercion)):
                    tot.append(int(convercion[j])*(16**(len(convercion)-int(j+1))))
            self.resultado.setText(str(sum(tot)))
