# from flask import Flask, render_template, url_for
# from pyswip import Prolog
# app = Flask(__name__)
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QLineEdit
from PyQt5.uic.properties import QtWidgets, QtCore
from graphviz import Digraph
from pyswip import Prolog

class RoomController:
    def __init__(self):
        self.prologInstance = Prolog()
        self.prologInstance.consult('/home/saulfeliciano/Documents/Java Projects/arbol-genealogico-prolog/smart-hub-prolog/final.pl')
        self.graph = Digraph()
    
    def findallCousins(self, name):
        cousins = set()
        query = self.prologInstance.query("primo(" + name + ",Cousins)")
        for solution in query:
            cousins.add(solution["Cousins"])
            print("solution")
        return cousins



# @app.route('/')
class EjemploGUI(QMainWindow):
    def __init__(self):
        self.repositorio = RoomController()
        #self.repositorio.findallCousins("francisca")
        super().__init__()
        uic.loadUi("/home/saulfeliciano/IdeaProjects/arbol-genealogico-prolog/mainview.ui", self)
        self.btnagregarpuerta = QPushButton("pushButton_agregarpuerta")
        self.btnagregarpuerta.clicked.connect(self.agregarpuerta)
        #query = prolog.query("primo(" + name + ",Cousins)")

    def agregarpuerta(self):
        query = self.prologInstance.query("agregar_puerta(puertaID,lugar,tipo)")
        #query2 = self.prologInstance.query() TODO insertar hecho para poder contar la cantidad de puertas
        i = 0
        for puertas in query: #Aca va query2
            i = i+1
        self.textpuerta = QLineEdit("lineEdit_puerta")
        self.textpuerta.setText(i)

    def eliminarpuerta(self):
        query = self.prologInstance.query("remover_puerta(puertaID,lugar,tipo)")
        # query2 = self.prologInstance.query() TODO insertar hecho para poder contar la cantidad de puertas
        i = 0
        for puertas in query:  # Aca va query2
            i = i - 1
        self.textpuerta = QLineEdit("lineEdit_puerta")
        self.textpuerta.setText(i)

    # def hello_world():
    # prolog = Prolog()
    # prolog.consult("smart-hub-prolog/ProyectoFinal_Alaila1.pl")
    # return render_template('index.html')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    GUI = EjemploGUI()
    GUI.show()
    sys.exit(app.exec_())
