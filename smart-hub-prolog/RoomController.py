# from flask import Flask, render_template, url_for
# from pyswip import Prolog
# app = Flask(__name__)
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from graphviz import Digraph
from pyswip import Prolog

class RoomController:
    def __init__(self):
        self.prologInstance = Prolog()
        self.prologInstance.consult('c:/Users/jmlma/Documents/GitHub/arbol-genealogico-prolog/smart-hub-prolog/arbol.pl')
        self.graph = Digraph()
    
    def findallCousins(self, name):
        cousins = set()
        query = self.prologInstance.query("persona(" + name + ")")
        list(self.prologInstance.query("persona(" + name + ")"))



# @app.route('/')
class EjemploGUI(QMainWindow):
    def __init__(self):
        self.repositorio = RoomController()
        super().__init__()
       # uic.loadUi("/home/saulfeliciano/IdeaProjects/arbol-genealogico-prolog/mainview.ui", self)
        self.repositorio.findallCousins("francisca")
        #query = prolog.query("primo(" + name + ",Cousins)")

    # def hello_world():
    # prolog = Prolog()
    # prolog.consult("smart-hub-prolog/ProyectoFinal_Alaila1.pl")
    # return render_template('index.html')


if __name__ == '__main__':

    app = QApplication(sys.argv)
    GUI = EjemploGUI()
    GUI.show()
    sys.exit(app.exec_())
