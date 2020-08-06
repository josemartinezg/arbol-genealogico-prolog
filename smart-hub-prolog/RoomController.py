# from flask import Flask, render_template, url_for
# from pyswip import Prolog
# app = Flask(__name__)
import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication

# @app.route('/')
class EjemploGUI(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("/home/saulfeliciano/IdeaProjects/arbol-genealogico-prolog/mainview.ui", self)

    # def hello_world():
    # prolog = Prolog()
    # prolog.consult("smart-hub-prolog/ProyectoFinal_Alaila1.pl")
    # return render_template('index.html')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    GUI = EjemploGUI()
    GUI.show()
    sys.exit(app.exec_())
