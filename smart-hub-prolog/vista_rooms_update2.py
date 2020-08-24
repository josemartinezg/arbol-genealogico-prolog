# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainview.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from graphviz import Digraph
from pyswip import Prolog
import random

class RoomController:
    def __init__(self):
        self.prolog_instance = Prolog()
        self.prolog_instance.consult('/home/saulfeliciano/IdeaProjects/arbol-genealogico-prolog/smart-hub-prolog/proyectofinal.pl')
        self.graph = Digraph()


    def cantidad_puertas(self):
        puertas = 0
        query2 = self.prolog_instance.query("puertas(Identificador,Habitacion,Ubicacion)")
        for puerta in query2:
            print(puerta)
            puertas = puertas+1
        result = bool(query2)
        return result

    def accionar_puerta_ventana(self, relacion, codigo, habitacion, tipo):
        query = self.prolog_instance.query(relacion + "(" + codigo + "," + habitacion + ")")
        if relacion == "abrir_puerta":
            flag = False
            query_verificar = self.prolog_instance.query("puertasCerradas(Puerta," + habitacion + "," + tipo + ")")
            for verificar in query_verificar:
                if verificar["Puerta"] == codigo:
                    flag = True
            if flag is True:
                queryRetract = self.prolog_instance.retract("puertasCerradas(" + codigo + "," + habitacion + "," + tipo + ")")
            query2 = self.prolog_instance.assertz("puertasAbiertas(" + codigo + "," + habitacion + "," + tipo + ")")
            query3 = self.prolog_instance.query("puertasAbiertas(Puerta," + habitacion + ",_)")
            for valor in query3:
                if valor["Puerta"] == codigo:
                    return "True"

        elif relacion == "cerrar_puerta":
            flag = False
            query_verificar = self.prolog_instance.query("puertasAbiertas(Puerta," + habitacion + "," + tipo + ")")
            for verificar in query_verificar:
                if verificar["Puerta"] == codigo:
                    flag = True
            if flag is True:
                queryRetract = self.prolog_instance.retract("puertasAbiertas(" + codigo + "," + habitacion + "," + tipo + ")")
            query2 = self.prolog_instance.assertz("puertasCerradas(" + codigo + "," + habitacion + "," + tipo + ")")
            query3 = self.prolog_instance.query("puertasCerradas(Puerta," + habitacion + ",_)")
            for valor in query3:
                if valor["Puerta"] == codigo:
                    return "False"

        elif relacion == "abrir_ventana":
            flag = False
            query_verificar = self.prolog_instance.query("ventanasCerradas(Ventana," + habitacion + ")")
            for verificar in query_verificar:
                if verificar["Ventana"] == codigo:
                    flag = True
            if flag is True:
                queryRetract = self.prolog_instance.retract(
                    "ventanasCerradas(" + codigo + "," + habitacion + ")")
            query2 = self.prolog_instance.assertz("ventanasAbiertas(" + codigo + "," + habitacion + ")")
            query3 = self.prolog_instance.query("ventanasAbiertas(Ventana," + habitacion + ")")
            for valor in query3:
                if valor["Ventana"] == codigo:
                    return "True"

        elif relacion == "cerrar_ventana":
            flag = False
            query_verificar = self.prolog_instance.query("ventanasAbiertas(Ventana," + habitacion + ")")
            for verificar in query_verificar:
                if verificar["Ventana"] == codigo:
                    flag = True
            if flag is True:
                queryRetract = self.prolog_instance.retract(
                    "ventanasAbiertas(" + codigo + "," + habitacion + ")")
            query2 = self.prolog_instance.assertz("ventanasCerradas(" + codigo + "," + habitacion + ")")
            query3 = self.prolog_instance.query("ventanasCerradas(Ventana," + habitacion + ")")
            for valor in query3:
                if valor["Ventana"] == codigo:
                    return "False"

        elif relacion == "encender_luz":
            flag = False
            query_verificar = self.prolog_instance.query("lucesApagadas(Luz," + habitacion + ")")
            for verificar in query_verificar:
                if verificar["Luz"] == codigo:
                    flag = True
            if flag is True:
                queryRetract = self.prolog_instance.retract(
                    "lucesApagadas(" + codigo + "," + habitacion + ")")
            query2 = self.prolog_instance.assertz("lucesEncendidas(" + codigo + "," + habitacion + ")")
            query3 = self.prolog_instance.query("lucesEncendidas(Luz," + habitacion + ")")
            for valor in query3:
                if valor["Luz"] == codigo:
                    return "True"

        elif relacion == "apagar_luz":
            flag = False
            query_verificar = self.prolog_instance.query("lucesEncendidas(Luz," + habitacion + ")")
            for verificar in query_verificar:
                if verificar["Luz"] == codigo:
                    flag = True
            if flag is True:
                queryRetract = self.prolog_instance.retract(
                    "lucesEncendidas(" + codigo + "," + habitacion + ")")
            query2 = self.prolog_instance.assertz("lucesApagadas(" + codigo + "," + habitacion + ")")
            query3 = self.prolog_instance.query("lucesApagadas(Luz," + habitacion + ")")
            for valor in query3:
                if valor["Luz"] == codigo:
                    return "False"

    def agregar_persona_habitacion(self, relacion, habitacion, cantidad):
        query = self.prolog_instance.query(relacion + "(" + habitacion + "," + cantidad + ")")
        query2 = self.prolog_instance.query(relacion + "(" + habitacion + ",Cantidad)")
        for cantidadRetornada in query2:
            cantidad = str(query2["Cantidad"])
        return cantidad

    def eliminar_personas_habitacion(self, relacion, habitacion, cantidad):
        query = self.prolog_instance.query(relacion + "(" + habitacion + ",0)")
        query2 = self.prolog_instance.query(relacion + "(" + habitacion + ",Cantidad)")
        for cantidadRetornada in query2:
            cantidad = str(query2["Cantidad"])
        return cantidad

    def apagar_todo(self):
        habitacion = "_"
        tipo = "_"
        puertas = []
        ventanas = []
        luces = []
        query1 = self.prolog_instance.query("puertas(X,Y,Tipo)")
        for valor in query1:
            puertas.append(valor["X"])
        query2 = self.prolog_instance.query("ventanas(X,Y)")
        for valor in query2:
            ventanas.append(valor["X"])
        query3 = self.prolog_instance.query("luces(X,Y)")
        for valor in query3:
            luces.append(valor["X"])

        for puerta in puertas:
            self.accionar_puerta_ventana("cerrar_puerta", puerta, habitacion, tipo)
        for ventana in ventanas:
            self.accionar_puerta_ventana("cerrar_ventana", ventana, habitacion, tipo)
        for luz in luces:
            self.accionar_puerta_ventana("apagar_luz", luz, habitacion, tipo)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 908)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(0, 0, 1091, 781))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.scrollArea = QtWidgets.QScrollArea(self.verticalLayoutWidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1085, 775))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalScrollBar = QtWidgets.QScrollBar(self.scrollAreaWidgetContents)
        self.verticalScrollBar.setGeometry(QtCore.QRect(1070, 0, 16, 781))
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        self.widget = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget.setGeometry(QtCore.QRect(40, 80, 451, 341))
        self.widget.setMouseTracking(False)
        self.widget.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-color: rgb(136, 138, 133);")
        self.widget.setObjectName("widget")
        self.ledit_movimiento1 = QtWidgets.QLineEdit(self.widget)
        self.ledit_movimiento1.setGeometry(QtCore.QRect(170, 90, 100, 31))
        self.ledit_movimiento1.setObjectName("ledit_movimiento1")
        self.lbl_sensor1 = QtWidgets.QLabel(self.widget)
        self.lbl_sensor1.setGeometry(QtCore.QRect(40, 50, 71, 31))
        self.lbl_sensor1.setObjectName("lbl_sensor1")
        self.lbl_movimiento1 = QtWidgets.QLabel(self.widget)
        self.lbl_movimiento1.setGeometry(QtCore.QRect(40, 90, 91, 22))
        self.lbl_movimiento1.setObjectName("lbl_movimiento1")
        self.lbl_estado1 = QtWidgets.QLabel(self.widget)
        self.lbl_estado1.setGeometry(QtCore.QRect(190, 50, 68, 22))
        self.lbl_estado1.setObjectName("lbl_estado1")
        self.btn_temperatura1 = QtWidgets.QPushButton(self.widget)
        self.btn_temperatura1.setGeometry(QtCore.QRect(320, 120, 99, 38))
        self.btn_temperatura1.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_temperatura1.setObjectName("btn_temperatura1")
        self.btn_movimiento1mas = QtWidgets.QPushButton(self.widget)
        self.btn_movimiento1mas.setGeometry(QtCore.QRect(320, 80, 51, 38))
        self.btn_movimiento1mas.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_movimiento1mas.setObjectName("btn_movimiento1mas")
        self.btn_luz1 = QtWidgets.QPushButton(self.widget)
        self.btn_luz1.setGeometry(QtCore.QRect(320, 160, 99, 38))
        self.btn_luz1.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_luz1.setObjectName("btn_luz1")
        self.btn_ventana1 = QtWidgets.QPushButton(self.widget)
        self.btn_ventana1.setGeometry(QtCore.QRect(320, 200, 99, 38))
        self.btn_ventana1.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_ventana1.setObjectName("btn_ventana1")
        self.btn_puerta1 = QtWidgets.QPushButton(self.widget)
        self.btn_puerta1.setGeometry(QtCore.QRect(320, 240, 99, 38))
        self.btn_puerta1.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_puerta1.setObjectName("btn_puerta1")
        self.lbl_accion1 = QtWidgets.QLabel(self.widget)
        self.lbl_accion1.setGeometry(QtCore.QRect(340, 50, 68, 22))
        self.lbl_accion1.setObjectName("lbl_accion1")
        self.lbl_temp1 = QtWidgets.QLabel(self.widget)
        self.lbl_temp1.setGeometry(QtCore.QRect(40, 130, 101, 22))
        self.lbl_temp1.setObjectName("lbl_temp1")
        self.lbl_luz1 = QtWidgets.QLabel(self.widget)
        self.lbl_luz1.setGeometry(QtCore.QRect(40, 170, 101, 22))
        self.lbl_luz1.setObjectName("lbl_luz1")
        self.lbl_ventana1 = QtWidgets.QLabel(self.widget)
        self.lbl_ventana1.setGeometry(QtCore.QRect(40, 210, 101, 22))
        self.lbl_ventana1.setObjectName("lbl_ventana1")
        self.lbl_puerta1 = QtWidgets.QLabel(self.widget)
        self.lbl_puerta1.setGeometry(QtCore.QRect(40, 250, 101, 22))
        self.lbl_puerta1.setObjectName("lbl_puerta1")
        self.ledit_temperatura1 = QtWidgets.QLineEdit(self.widget)
        self.ledit_temperatura1.setGeometry(QtCore.QRect(170, 130, 101, 31))
        self.ledit_temperatura1.setObjectName("ledit_temperatura1")
        self.ledit_luz1 = QtWidgets.QLineEdit(self.widget)
        self.ledit_luz1.setGeometry(QtCore.QRect(170, 170, 101, 31))
        self.ledit_luz1.setObjectName("ledit_luz1")
        self.ledit_ventana1 = QtWidgets.QLineEdit(self.widget)
        self.ledit_ventana1.setGeometry(QtCore.QRect(170, 210, 101, 31))
        self.ledit_ventana1.setObjectName("ledit_ventana1")
        self.ledit_puerta1 = QtWidgets.QLineEdit(self.widget)
        self.ledit_puerta1.setGeometry(QtCore.QRect(170, 250, 101, 31))
        self.ledit_puerta1.setObjectName("ledit_puerta1")
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setGeometry(QtCore.QRect(0, 30, 451, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.lbl_habitacion1 = QtWidgets.QLabel(self.widget)
        self.lbl_habitacion1.setGeometry(QtCore.QRect(20, 0, 151, 31))
        self.lbl_habitacion1.setObjectName("lbl_habitacion1")
        self.btn_movimiento1menos = QtWidgets.QPushButton(self.widget)
        self.btn_movimiento1menos.setGeometry(QtCore.QRect(370, 80, 51, 38))
        self.btn_movimiento1menos.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_movimiento1menos.setObjectName("btn_movimiento1menos")
        self.lbl_aire1 = QtWidgets.QLabel(self.widget)
        self.lbl_aire1.setGeometry(QtCore.QRect(40, 290, 91, 22))
        self.lbl_aire1.setObjectName("lbl_aire1")
        self.ledit_aire1 = QtWidgets.QLineEdit(self.widget)
        self.ledit_aire1.setGeometry(QtCore.QRect(170, 290, 101, 31))
        self.ledit_aire1.setObjectName("ledit_aire1")
        self.btn_aire1 = QtWidgets.QPushButton(self.widget)
        self.btn_aire1.setGeometry(QtCore.QRect(320, 280, 99, 38))
        self.btn_aire1.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_aire1.setObjectName("btn_aire1")
        self.widget_2 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_2.setGeometry(QtCore.QRect(520, 80, 451, 341))
        self.widget_2.setMouseTracking(False)
        self.widget_2.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-color: rgb(136, 138, 133);")
        self.widget_2.setObjectName("widget_2")
        self.ledit_movimiento2 = QtWidgets.QLineEdit(self.widget_2)
        self.ledit_movimiento2.setGeometry(QtCore.QRect(170, 90, 100, 31))
        self.ledit_movimiento2.setObjectName("ledit_movimiento2")
        self.lbl_sensor2 = QtWidgets.QLabel(self.widget_2)
        self.lbl_sensor2.setGeometry(QtCore.QRect(40, 50, 71, 31))
        self.lbl_sensor2.setObjectName("lbl_sensor2")
        self.lbl_movimiento2 = QtWidgets.QLabel(self.widget_2)
        self.lbl_movimiento2.setGeometry(QtCore.QRect(40, 90, 91, 22))
        self.lbl_movimiento2.setObjectName("lbl_movimiento2")
        self.lbl_estado2 = QtWidgets.QLabel(self.widget_2)
        self.lbl_estado2.setGeometry(QtCore.QRect(190, 50, 68, 22))
        self.lbl_estado2.setObjectName("lbl_estado2")
        self.btn_temperatura2 = QtWidgets.QPushButton(self.widget_2)
        self.btn_temperatura2.setGeometry(QtCore.QRect(320, 120, 99, 38))
        self.btn_temperatura2.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_temperatura2.setObjectName("btn_temperatura2")
        self.btn_movimiento2mas = QtWidgets.QPushButton(self.widget_2)
        self.btn_movimiento2mas.setGeometry(QtCore.QRect(320, 80, 51, 38))
        self.btn_movimiento2mas.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_movimiento2mas.setObjectName("btn_movimiento2mas")
        self.btn_luz2 = QtWidgets.QPushButton(self.widget_2)
        self.btn_luz2.setGeometry(QtCore.QRect(320, 160, 99, 38))
        self.btn_luz2.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_luz2.setObjectName("btn_luz2")
        self.btn_ventana2 = QtWidgets.QPushButton(self.widget_2)
        self.btn_ventana2.setGeometry(QtCore.QRect(320, 200, 99, 38))
        self.btn_ventana2.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_ventana2.setObjectName("btn_ventana2")
        self.btn_puerta2 = QtWidgets.QPushButton(self.widget_2)
        self.btn_puerta2.setGeometry(QtCore.QRect(320, 240, 99, 38))
        self.btn_puerta2.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_puerta2.setObjectName("btn_puerta2")
        self.lbl_accion2 = QtWidgets.QLabel(self.widget_2)
        self.lbl_accion2.setGeometry(QtCore.QRect(340, 50, 68, 22))
        self.lbl_accion2.setObjectName("lbl_accion2")
        self.lbl_temp2 = QtWidgets.QLabel(self.widget_2)
        self.lbl_temp2.setGeometry(QtCore.QRect(40, 130, 101, 22))
        self.lbl_temp2.setObjectName("lbl_temp2")
        self.lbl_temp2_2 = QtWidgets.QLabel(self.widget_2)
        self.lbl_temp2_2.setGeometry(QtCore.QRect(40, 170, 101, 22))
        self.lbl_temp2_2.setObjectName("lbl_temp2_2")
        self.lbl_ventana2 = QtWidgets.QLabel(self.widget_2)
        self.lbl_ventana2.setGeometry(QtCore.QRect(40, 210, 101, 22))
        self.lbl_ventana2.setObjectName("lbl_ventana2")
        self.lbl_puerta2 = QtWidgets.QLabel(self.widget_2)
        self.lbl_puerta2.setGeometry(QtCore.QRect(40, 250, 101, 22))
        self.lbl_puerta2.setObjectName("lbl_puerta2")
        self.ledit_temperatura2 = QtWidgets.QLineEdit(self.widget_2)
        self.ledit_temperatura2.setGeometry(QtCore.QRect(170, 130, 101, 31))
        self.ledit_temperatura2.setObjectName("ledit_temperatura2")
        self.ledit_luz2 = QtWidgets.QLineEdit(self.widget_2)
        self.ledit_luz2.setGeometry(QtCore.QRect(170, 170, 101, 31))
        self.ledit_luz2.setObjectName("ledit_luz2")
        self.ledit_ventana2 = QtWidgets.QLineEdit(self.widget_2)
        self.ledit_ventana2.setGeometry(QtCore.QRect(170, 210, 101, 31))
        self.ledit_ventana2.setObjectName("ledit_ventana2")
        self.ledit_puerta2 = QtWidgets.QLineEdit(self.widget_2)
        self.ledit_puerta2.setGeometry(QtCore.QRect(170, 250, 101, 31))
        self.ledit_puerta2.setObjectName("ledit_puerta2")
        self.line_2 = QtWidgets.QFrame(self.widget_2)
        self.line_2.setGeometry(QtCore.QRect(0, 30, 451, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.lbl_habitacion2 = QtWidgets.QLabel(self.widget_2)
        self.lbl_habitacion2.setGeometry(QtCore.QRect(20, 0, 151, 31))
        self.lbl_habitacion2.setObjectName("lbl_habitacion2")
        self.btn_movimiento2menos = QtWidgets.QPushButton(self.widget_2)
        self.btn_movimiento2menos.setGeometry(QtCore.QRect(370, 80, 51, 38))
        self.btn_movimiento2menos.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_movimiento2menos.setObjectName("btn_movimiento2menos")
        self.lbl_aire2 = QtWidgets.QLabel(self.widget_2)
        self.lbl_aire2.setGeometry(QtCore.QRect(40, 290, 91, 22))
        self.lbl_aire2.setObjectName("lbl_aire2")
        self.ledit_aire2 = QtWidgets.QLineEdit(self.widget_2)
        self.ledit_aire2.setGeometry(QtCore.QRect(170, 290, 101, 31))
        self.ledit_aire2.setObjectName("ledit_aire2")
        self.btn_aire2 = QtWidgets.QPushButton(self.widget_2)
        self.btn_aire2.setGeometry(QtCore.QRect(320, 280, 99, 38))
        self.btn_aire2.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_aire2.setObjectName("btn_aire2")
        self.widget_3 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_3.setGeometry(QtCore.QRect(40, 430, 451, 331))
        self.widget_3.setMouseTracking(False)
        self.widget_3.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-color: rgb(136, 138, 133);")
        self.widget_3.setObjectName("widget_3")
        self.ledit_movimiento3 = QtWidgets.QLineEdit(self.widget_3)
        self.ledit_movimiento3.setGeometry(QtCore.QRect(170, 90, 100, 31))
        self.ledit_movimiento3.setObjectName("ledit_movimiento3")
        self.lbl_sensor3 = QtWidgets.QLabel(self.widget_3)
        self.lbl_sensor3.setGeometry(QtCore.QRect(40, 50, 71, 31))
        self.lbl_sensor3.setObjectName("lbl_sensor3")
        self.lbl_movimiento3 = QtWidgets.QLabel(self.widget_3)
        self.lbl_movimiento3.setGeometry(QtCore.QRect(40, 90, 91, 22))
        self.lbl_movimiento3.setObjectName("lbl_movimiento3")
        self.lbl_estado3 = QtWidgets.QLabel(self.widget_3)
        self.lbl_estado3.setGeometry(QtCore.QRect(190, 50, 68, 22))
        self.lbl_estado3.setObjectName("lbl_estado3")
        self.btn_temperatura3 = QtWidgets.QPushButton(self.widget_3)
        self.btn_temperatura3.setGeometry(QtCore.QRect(320, 120, 99, 38))
        self.btn_temperatura3.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_temperatura3.setObjectName("btn_temperatura3")
        self.btn_movimiento3mas = QtWidgets.QPushButton(self.widget_3)
        self.btn_movimiento3mas.setGeometry(QtCore.QRect(320, 80, 51, 38))
        self.btn_movimiento3mas.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_movimiento3mas.setObjectName("btn_movimiento3mas")
        self.btn_luz3 = QtWidgets.QPushButton(self.widget_3)
        self.btn_luz3.setGeometry(QtCore.QRect(320, 160, 99, 38))
        self.btn_luz3.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_luz3.setObjectName("btn_luz3")
        self.btn_ventana3 = QtWidgets.QPushButton(self.widget_3)
        self.btn_ventana3.setGeometry(QtCore.QRect(320, 200, 99, 38))
        self.btn_ventana3.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_ventana3.setObjectName("btn_ventana3")
        self.btn_puerta3 = QtWidgets.QPushButton(self.widget_3)
        self.btn_puerta3.setGeometry(QtCore.QRect(320, 240, 99, 38))
        self.btn_puerta3.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_puerta3.setObjectName("btn_puerta3")
        self.lbl_accion3 = QtWidgets.QLabel(self.widget_3)
        self.lbl_accion3.setGeometry(QtCore.QRect(340, 50, 68, 22))
        self.lbl_accion3.setObjectName("lbl_accion3")
        self.lbl_temp3 = QtWidgets.QLabel(self.widget_3)
        self.lbl_temp3.setGeometry(QtCore.QRect(40, 130, 101, 22))
        self.lbl_temp3.setObjectName("lbl_temp3")
        self.lbl_luz3 = QtWidgets.QLabel(self.widget_3)
        self.lbl_luz3.setGeometry(QtCore.QRect(40, 170, 101, 22))
        self.lbl_luz3.setObjectName("lbl_luz3")
        self.lbl_ventana3 = QtWidgets.QLabel(self.widget_3)
        self.lbl_ventana3.setGeometry(QtCore.QRect(40, 210, 101, 22))
        self.lbl_ventana3.setObjectName("lbl_ventana3")
        self.lbl_puerta3 = QtWidgets.QLabel(self.widget_3)
        self.lbl_puerta3.setGeometry(QtCore.QRect(40, 250, 101, 22))
        self.lbl_puerta3.setObjectName("lbl_puerta3")
        self.ledit_temperatura3 = QtWidgets.QLineEdit(self.widget_3)
        self.ledit_temperatura3.setGeometry(QtCore.QRect(170, 130, 101, 31))
        self.ledit_temperatura3.setObjectName("ledit_temperatura3")
        self.ledit_luz3 = QtWidgets.QLineEdit(self.widget_3)
        self.ledit_luz3.setGeometry(QtCore.QRect(170, 170, 101, 31))
        self.ledit_luz3.setObjectName("ledit_luz3")
        self.ledit_ventana3 = QtWidgets.QLineEdit(self.widget_3)
        self.ledit_ventana3.setGeometry(QtCore.QRect(170, 210, 101, 31))
        self.ledit_ventana3.setObjectName("ledit_ventana3")
        self.ledit_puerta3 = QtWidgets.QLineEdit(self.widget_3)
        self.ledit_puerta3.setGeometry(QtCore.QRect(170, 250, 101, 31))
        self.ledit_puerta3.setObjectName("ledit_puerta3")
        self.line_3 = QtWidgets.QFrame(self.widget_3)
        self.line_3.setGeometry(QtCore.QRect(0, 30, 451, 16))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.lbl_habitacion3 = QtWidgets.QLabel(self.widget_3)
        self.lbl_habitacion3.setGeometry(QtCore.QRect(20, 0, 151, 31))
        self.lbl_habitacion3.setObjectName("lbl_habitacion3")
        self.btn_movimiento3menos = QtWidgets.QPushButton(self.widget_3)
        self.btn_movimiento3menos.setGeometry(QtCore.QRect(370, 80, 51, 38))
        self.btn_movimiento3menos.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_movimiento3menos.setObjectName("btn_movimiento3menos")
        self.lbl_aire3 = QtWidgets.QLabel(self.widget_3)
        self.lbl_aire3.setGeometry(QtCore.QRect(40, 290, 91, 22))
        self.lbl_aire3.setObjectName("lbl_aire3")
        self.ledit_aire3 = QtWidgets.QLineEdit(self.widget_3)
        self.ledit_aire3.setGeometry(QtCore.QRect(170, 290, 101, 31))
        self.ledit_aire3.setObjectName("ledit_aire3")
        self.btn_aire3 = QtWidgets.QPushButton(self.widget_3)
        self.btn_aire3.setGeometry(QtCore.QRect(320, 280, 99, 38))
        self.btn_aire3.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_aire3.setObjectName("btn_aire3")
        self.widget_4 = QtWidgets.QWidget(self.scrollAreaWidgetContents)
        self.widget_4.setGeometry(QtCore.QRect(520, 430, 451, 331))
        self.widget_4.setMouseTracking(False)
        self.widget_4.setStyleSheet("background-color: rgb(238, 238, 236);\n"
"border-color: rgb(136, 138, 133);")
        self.widget_4.setObjectName("widget_4")
        self.ledit_movimiento4 = QtWidgets.QLineEdit(self.widget_4)
        self.ledit_movimiento4.setGeometry(QtCore.QRect(170, 90, 100, 31))
        self.ledit_movimiento4.setObjectName("ledit_movimiento4")
        self.lbl_sensor4 = QtWidgets.QLabel(self.widget_4)
        self.lbl_sensor4.setGeometry(QtCore.QRect(40, 50, 71, 31))
        self.lbl_sensor4.setObjectName("lbl_sensor4")
        self.lbl_movimiento4 = QtWidgets.QLabel(self.widget_4)
        self.lbl_movimiento4.setGeometry(QtCore.QRect(40, 90, 91, 22))
        self.lbl_movimiento4.setObjectName("lbl_movimiento4")
        self.lbl_estado4 = QtWidgets.QLabel(self.widget_4)
        self.lbl_estado4.setGeometry(QtCore.QRect(190, 50, 68, 22))
        self.lbl_estado4.setObjectName("lbl_estado4")
        self.btn_temperatura4 = QtWidgets.QPushButton(self.widget_4)
        self.btn_temperatura4.setGeometry(QtCore.QRect(320, 120, 99, 38))
        self.btn_temperatura4.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_temperatura4.setObjectName("btn_temperatura4")
        self.btn_movimiento4mas = QtWidgets.QPushButton(self.widget_4)
        self.btn_movimiento4mas.setGeometry(QtCore.QRect(320, 80, 51, 38))
        self.btn_movimiento4mas.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_movimiento4mas.setObjectName("btn_movimiento4mas")
        self.btn_luz4 = QtWidgets.QPushButton(self.widget_4)
        self.btn_luz4.setGeometry(QtCore.QRect(320, 160, 99, 38))
        self.btn_luz4.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_luz4.setObjectName("btn_luz4")
        self.btn_ventana4 = QtWidgets.QPushButton(self.widget_4)
        self.btn_ventana4.setGeometry(QtCore.QRect(320, 200, 99, 38))
        self.btn_ventana4.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_ventana4.setObjectName("btn_ventana4")
        self.btn_puerta4 = QtWidgets.QPushButton(self.widget_4)
        self.btn_puerta4.setGeometry(QtCore.QRect(320, 240, 99, 38))
        self.btn_puerta4.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_puerta4.setObjectName("btn_puerta4")
        self.lbl_accion4 = QtWidgets.QLabel(self.widget_4)
        self.lbl_accion4.setGeometry(QtCore.QRect(340, 50, 68, 22))
        self.lbl_accion4.setObjectName("lbl_accion4")
        self.lbl_temp4 = QtWidgets.QLabel(self.widget_4)
        self.lbl_temp4.setGeometry(QtCore.QRect(40, 130, 101, 22))
        self.lbl_temp4.setObjectName("lbl_temp4")
        self.lbl_luz4 = QtWidgets.QLabel(self.widget_4)
        self.lbl_luz4.setGeometry(QtCore.QRect(40, 170, 101, 22))
        self.lbl_luz4.setObjectName("lbl_luz4")
        self.lbl_ventana4 = QtWidgets.QLabel(self.widget_4)
        self.lbl_ventana4.setGeometry(QtCore.QRect(40, 210, 101, 22))
        self.lbl_ventana4.setObjectName("lbl_ventana4")
        self.lbl_puerta4 = QtWidgets.QLabel(self.widget_4)
        self.lbl_puerta4.setGeometry(QtCore.QRect(40, 250, 101, 22))
        self.lbl_puerta4.setObjectName("lbl_puerta4")
        self.ledit_temperatura4 = QtWidgets.QLineEdit(self.widget_4)
        self.ledit_temperatura4.setGeometry(QtCore.QRect(170, 130, 101, 31))
        self.ledit_temperatura4.setObjectName("ledit_temperatura4")
        self.ledit_luz4 = QtWidgets.QLineEdit(self.widget_4)
        self.ledit_luz4.setGeometry(QtCore.QRect(170, 170, 101, 31))
        self.ledit_luz4.setObjectName("ledit_luz4")
        self.ledit_ventana4 = QtWidgets.QLineEdit(self.widget_4)
        self.ledit_ventana4.setGeometry(QtCore.QRect(170, 210, 101, 31))
        self.ledit_ventana4.setObjectName("ledit_ventana4")
        self.ledit_puerta4 = QtWidgets.QLineEdit(self.widget_4)
        self.ledit_puerta4.setGeometry(QtCore.QRect(170, 250, 101, 31))
        self.ledit_puerta4.setObjectName("ledit_puerta4")
        self.line_4 = QtWidgets.QFrame(self.widget_4)
        self.line_4.setGeometry(QtCore.QRect(0, 30, 451, 16))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.lbl_habitacion4 = QtWidgets.QLabel(self.widget_4)
        self.lbl_habitacion4.setGeometry(QtCore.QRect(20, 0, 151, 31))
        self.lbl_habitacion4.setObjectName("lbl_habitacion4")
        self.btn_movimiento4menos = QtWidgets.QPushButton(self.widget_4)
        self.btn_movimiento4menos.setGeometry(QtCore.QRect(370, 80, 51, 38))
        self.btn_movimiento4menos.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_movimiento4menos.setObjectName("btn_movimiento4menos")
        self.lbl_aire4 = QtWidgets.QLabel(self.widget_4)
        self.lbl_aire4.setGeometry(QtCore.QRect(40, 290, 91, 22))
        self.lbl_aire4.setObjectName("lbl_aire4")
        self.ledit_aire4 = QtWidgets.QLineEdit(self.widget_4)
        self.ledit_aire4.setGeometry(QtCore.QRect(170, 290, 101, 31))
        self.ledit_aire4.setObjectName("ledit_aire4")
        self.btn_aire4 = QtWidgets.QPushButton(self.widget_4)
        self.btn_aire4.setGeometry(QtCore.QRect(320, 280, 99, 38))
        self.btn_aire4.setStyleSheet("background-color: rgb(114, 159, 207);")
        self.btn_aire4.setObjectName("btn_aire4")
        self.lbl_rooms = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_rooms.setGeometry(QtCore.QRect(610, 20, 351, 41))
        self.lbl_rooms.setObjectName("lbl_rooms")
        self.lbl_paneles = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_paneles.setGeometry(QtCore.QRect(70, 30, 191, 22))
        self.lbl_paneles.setObjectName("lbl_paneles")
        self.ledit_dir_paneles = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ledit_dir_paneles.setGeometry(QtCore.QRect(260, 20, 113, 38))
        self.ledit_dir_paneles.setObjectName("ledit_dir_paneles")
        self.lbl_hora_actual = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.lbl_hora_actual.setGeometry(QtCore.QRect(390, 30, 101, 21))
        self.lbl_hora_actual.setObjectName("lbl_hora_actual")
        self.ledit_hora_actual = QtWidgets.QLineEdit(self.scrollAreaWidgetContents)
        self.ledit_hora_actual.setGeometry(QtCore.QRect(490, 20, 113, 38))
        self.ledit_hora_actual.setObjectName("ledit_hora_actual")
        self.widget.raise_()
        self.verticalScrollBar.raise_()
        self.widget_2.raise_()
        self.widget_3.raise_()
        self.widget_4.raise_()
        self.lbl_rooms.raise_()
        self.lbl_paneles.raise_()
        self.ledit_dir_paneles.raise_()
        self.lbl_hora_actual.raise_()
        self.ledit_hora_actual.raise_()
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 30))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # Botones de sensores de movimiento
        self.btn_movimiento1mas.clicked.connect(self.accion_movimiento_1mas)
        self.btn_movimiento1menos.clicked.connect(self.accion_movimiento_1menos)
        self.btn_movimiento2mas.clicked.connect(self.accion_movimiento_2mas)
        self.btn_movimiento2menos.clicked.connect(self.accion_movimiento_2menos)
        self.btn_movimiento3mas.clicked.connect(self.accion_movimiento_3mas)
        self.btn_movimiento3menos.clicked.connect(self.accion_movimiento_3menos)
        self.btn_movimiento4mas.clicked.connect(self.accion_movimiento_4mas)
        self.btn_movimiento4menos.clicked.connect(self.accion_movimiento_4menos)
        # Botones de la ventana
        self.btn_ventana1.clicked.connect(self.accion_ventana_1)
        self.btn_ventana2.clicked.connect(self.accion_ventana_2)
        self.btn_ventana3.clicked.connect(self.accion_ventana_3)
        self.btn_ventana4.clicked.connect(self.accion_ventana_4)
        # Botones de la puerta
        self.btn_puerta1.clicked.connect(self.accion_puerta_1)
        self.btn_puerta2.clicked.connect(self.accion_puerta_2)
        self.btn_puerta3.clicked.connect(self.accion_puerta_3)
        self.btn_puerta4.clicked.connect(self.accion_puerta_4)
        # Botones de la luz
        self.btn_luz1.clicked.connect(self.accion_luz_1)
        self.btn_luz2.clicked.connect(self.accion_luz_2)
        self.btn_luz3.clicked.connect(self.accion_luz_3)
        self.btn_luz4.clicked.connect(self.accion_luz_4)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ledit_movimiento1.setText(_translate("MainWindow", "False"))
        self.lbl_sensor1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sensor</span></p></body></html>"))
        self.lbl_movimiento1.setText(_translate("MainWindow", "Movimiento"))
        self.lbl_estado1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Estado</span></p></body></html>"))
        self.btn_temperatura1.setText(_translate("MainWindow", "Encender"))
        self.btn_movimiento1mas.setText(_translate("MainWindow", "+"))
        self.btn_luz1.setText(_translate("MainWindow", "Encender"))
        self.btn_ventana1.setText(_translate("MainWindow", "Abrir"))
        self.btn_puerta1.setText(_translate("MainWindow", "Abrir"))
        self.lbl_accion1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Acción</span></p></body></html>"))
        self.lbl_temp1.setText(_translate("MainWindow", "Temperatura"))
        self.lbl_luz1.setText(_translate("MainWindow", "Luz"))
        self.lbl_ventana1.setText(_translate("MainWindow", "Ventana"))
        self.lbl_puerta1.setText(_translate("MainWindow", "Puerta"))
        self.ledit_temperatura1.setText(_translate("MainWindow", "False"))
        self.ledit_luz1.setText(_translate("MainWindow", "False"))
        self.ledit_ventana1.setText(_translate("MainWindow", "False"))
        self.ledit_puerta1.setText(_translate("MainWindow", "False"))
        self.lbl_habitacion1.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Habitación 1</span></p></body></html>"))
        self.btn_movimiento1menos.setText(_translate("MainWindow", "-"))
        self.lbl_aire1.setText(_translate("MainWindow", "Aire Acond."))
        self.ledit_aire1.setText(_translate("MainWindow", "False"))
        self.btn_aire1.setText(_translate("MainWindow", "Encender"))
        self.ledit_movimiento2.setText(_translate("MainWindow", "False"))
        self.lbl_sensor2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sensor</span></p></body></html>"))
        self.lbl_movimiento2.setText(_translate("MainWindow", "Movimiento"))
        self.lbl_estado2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Estado</span></p></body></html>"))
        self.btn_temperatura2.setText(_translate("MainWindow", "Encender"))
        self.btn_movimiento2mas.setText(_translate("MainWindow", "+"))
        self.btn_luz2.setText(_translate("MainWindow", "Encender"))
        self.btn_ventana2.setText(_translate("MainWindow", "Abrir"))
        self.btn_puerta2.setText(_translate("MainWindow", "Abrir"))
        self.lbl_accion2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Acción</span></p></body></html>"))
        self.lbl_temp2.setText(_translate("MainWindow", "Temperatura"))
        self.lbl_temp2_2.setText(_translate("MainWindow", "Luz"))
        self.lbl_ventana2.setText(_translate("MainWindow", "Ventana"))
        self.lbl_puerta2.setText(_translate("MainWindow", "Puerta"))
        self.ledit_temperatura2.setText(_translate("MainWindow", "False"))
        self.ledit_luz2.setText(_translate("MainWindow", "False"))
        self.ledit_ventana2.setText(_translate("MainWindow", "False"))
        self.ledit_puerta2.setText(_translate("MainWindow", "False"))
        self.lbl_habitacion2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Habitación 2</span></p></body></html>"))
        self.btn_movimiento2menos.setText(_translate("MainWindow", "-"))
        self.lbl_aire2.setText(_translate("MainWindow", "Aire Acond."))
        self.ledit_aire2.setText(_translate("MainWindow", "False"))
        self.btn_aire2.setText(_translate("MainWindow", "Encender"))
        self.ledit_movimiento3.setText(_translate("MainWindow", "False"))
        self.lbl_sensor3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sensor</span></p></body></html>"))
        self.lbl_movimiento3.setText(_translate("MainWindow", "Movimiento"))
        self.lbl_estado3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Estado</span></p></body></html>"))
        self.btn_temperatura3.setText(_translate("MainWindow", "Encender"))
        self.btn_movimiento3mas.setText(_translate("MainWindow", "+"))
        self.btn_luz3.setText(_translate("MainWindow", "Encender"))
        self.btn_ventana3.setText(_translate("MainWindow", "Abrir"))
        self.btn_puerta3.setText(_translate("MainWindow", "Abrir"))
        self.lbl_accion3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Acción</span></p></body></html>"))
        self.lbl_temp3.setText(_translate("MainWindow", "Temperatura"))
        self.lbl_luz3.setText(_translate("MainWindow", "Luz"))
        self.lbl_ventana3.setText(_translate("MainWindow", "Ventana"))
        self.lbl_puerta3.setText(_translate("MainWindow", "Puerta"))
        self.ledit_temperatura3.setText(_translate("MainWindow", "False"))
        self.ledit_luz3.setText(_translate("MainWindow", "False"))
        self.ledit_ventana3.setText(_translate("MainWindow", "False"))
        self.ledit_puerta3.setText(_translate("MainWindow", "False"))
        self.lbl_habitacion3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Habitación 3</span></p></body></html>"))
        self.btn_movimiento3menos.setText(_translate("MainWindow", "-"))
        self.lbl_aire3.setText(_translate("MainWindow", "Aire Acond."))
        self.ledit_aire3.setText(_translate("MainWindow", "False"))
        self.btn_aire3.setText(_translate("MainWindow", "Encender"))
        self.ledit_movimiento4.setText(_translate("MainWindow", "False"))
        self.lbl_sensor4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Sensor</span></p></body></html>"))
        self.lbl_movimiento4.setText(_translate("MainWindow", "Movimiento"))
        self.lbl_estado4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Estado</span></p></body></html>"))
        self.btn_temperatura4.setText(_translate("MainWindow", "Encender"))
        self.btn_movimiento4mas.setText(_translate("MainWindow", "+"))
        self.btn_luz4.setText(_translate("MainWindow", "Encender"))
        self.btn_ventana4.setText(_translate("MainWindow", "Abrir"))
        self.btn_puerta4.setText(_translate("MainWindow", "Abrir"))
        self.lbl_accion4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Acción</span></p></body></html>"))
        self.lbl_temp4.setText(_translate("MainWindow", "Temperatura"))
        self.lbl_luz4.setText(_translate("MainWindow", "Luz"))
        self.lbl_ventana4.setText(_translate("MainWindow", "Ventana"))
        self.lbl_puerta4.setText(_translate("MainWindow", "Puerta"))
        self.ledit_temperatura4.setText(_translate("MainWindow", "False"))
        self.ledit_luz4.setText(_translate("MainWindow", "False"))
        self.ledit_ventana4.setText(_translate("MainWindow", "False"))
        self.ledit_puerta4.setText(_translate("MainWindow", "False"))
        self.lbl_habitacion4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Habitación 4</span></p></body></html>"))
        self.btn_movimiento4menos.setText(_translate("MainWindow", "-"))
        self.lbl_aire4.setText(_translate("MainWindow", "Aire Acond."))
        self.ledit_aire4.setText(_translate("MainWindow", "False"))
        self.btn_aire4.setText(_translate("MainWindow", "Encender"))
        self.lbl_rooms.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt; font-style:italic; text-decoration: underline;\">Rooms</span></p></body></html>"))
        self.lbl_paneles.setText(_translate("MainWindow", "Dirección paneles solares:"))
        self.lbl_hora_actual.setText(_translate("MainWindow", "Hora Actual:"))

#Accuines de las puertas
    def accion_puerta_1(self):
        codigo = "puerta1"
        habitacion = "cocina"
        tipo = "interior"
        if self.btn_puerta1.text() == "Abrir":
            self.ledit_puerta1.setText(self.repositorio.accionar_puerta_ventana("abrir_puerta", codigo, habitacion, tipo))
            self.btn_puerta1.setText("Cerrar")

        elif self.btn_puerta1.text() == "Cerrar":
            self.ledit_puerta1.setText(self.repositorio.accionar_puerta_ventana("cerrar_puerta", codigo, habitacion, tipo))
            self.btn_puerta1.setText("Abrir")

    def accion_puerta_2(self):
        codigo = "puerta2"
        habitacion = "habitacion"
        tipo = "interior"
        if self.btn_puerta2.text() == "Abrir":
            self.ledit_puerta2.setText(self.repositorio.accionar_puerta_ventana("abrir_puerta", codigo, habitacion, tipo))
            self.btn_puerta2.setText("Cerrar")

        elif self.btn_puerta2.text() == "Cerrar":
            self.ledit_puerta2.setText(self.repositorio.accionar_puerta_ventana("cerrar_puerta", codigo, habitacion, tipo))
            self.btn_puerta2.setText("Abrir")

    def accion_puerta_3(self):
        codigo = "puerta3"
        habitacion = "terraza"
        tipo = "exterior"
        if self.btn_puerta3.text() == "Abrir":
            self.ledit_puerta3.setText(self.repositorio.accionar_puerta_ventana("abrir_puerta", codigo, habitacion, tipo))
            self.btn_puerta3.setText("Cerrar")

        elif self.btn_puerta3.text() == "Cerrar":
            self.ledit_puerta3.setText(self.repositorio.accionar_puerta_ventana("cerrar_puerta", codigo, habitacion, tipo))
            self.btn_puerta3.setText("Abrir")

    def accion_puerta_4(self):
        codigo = "puerta4"
        habitacion = "living"
        tipo = "exterior"
        if self.btn_puerta4.text() == "Abrir":
            self.ledit_puerta4.setText(self.repositorio.accionar_puerta_ventana("abrir_puerta", codigo, habitacion, tipo))
            self.btn_puerta4.setText("Cerrar")

        elif self.btn_puerta4.text() == "Cerrar":
            self.ledit_puerta4.setText(self.repositorio.accionar_puerta_ventana("cerrar_puerta", codigo, habitacion, tipo))
            self.btn_puerta4.setText("Abrir")

    #Acciones ventanas
    def accion_ventana_1(self):
        codigo = "ventana1"
        habitacion = "habitacion"
        tipo = ""
        if self.btn_ventana1.text() == "Abrir":
            self.ledit_ventana1.setText(self.repositorio.accionar_puerta_ventana("abrir_ventana", codigo, habitacion, tipo))
            self.btn_ventana1.setText("Cerrar")

        elif self.btn_ventana1.text() == "Cerrar":
            self.ledit_ventana1.setText(self.repositorio.accionar_puerta_ventana("cerrar_ventana", codigo, habitacion, tipo))
            self.btn_ventana1.setText("Abrir")

    def accion_ventana_2(self):
        codigo = "ventana2"
        habitacion = "living"
        tipo = ""
        if self.btn_ventana2.text() == "Abrir":
            self.ledit_ventana2.setText(self.repositorio.accionar_puerta_ventana("abrir_ventana", codigo, habitacion, tipo))
            self.btn_ventana2.setText("Cerrar")

        elif self.btn_ventana2.text() == "Cerrar":
            self.ledit_ventana2.setText(self.repositorio.accionar_puerta_ventana("cerrar_ventana", codigo, habitacion, tipo))
            self.btn_ventana2.setText("Abrir")

    def accion_ventana_3(self):
        codigo = "ventana3"
        habitacion = "terraza"
        tipo = ""
        if self.btn_ventana3.text() == "Abrir":
            self.ledit_ventana3.setText(self.repositorio.accionar_puerta_ventana("abrir_ventana", codigo, habitacion, tipo))
            self.btn_ventana3.setText("Cerrar")

        elif self.btn_ventana3.text() == "Cerrar":
            self.ledit_ventana3.setText(self.repositorio.accionar_puerta_ventana("cerrar_ventana", codigo, habitacion, tipo))
            self.btn_ventana3.setText("Abrir")

    def accion_ventana_4(self):
        codigo = "ventana4"
        habitacion = "cocina"
        tipo = ""
        if self.btn_ventana4.text() == "Abrir":
            self.ledit_ventana4.setText(self.repositorio.accionar_puerta_ventana("abrir_ventana", codigo, habitacion, tipo))
            self.btn_ventana4.setText("Cerrar")

        elif self.btn_ventana4.text() == "Cerrar":
            self.ledit_ventana4.setText(self.repositorio.accionar_puerta_ventana("cerrar_ventana", codigo, habitacion, tipo))
            self.btn_ventana4.setText("Abrir")

    # Acciones luces
    def accion_luz_1(self):
        codigo = "luz_1"
        habitacion = "cocina"
        tipo = ""
        if self.btn_luz1.text() == "Encender":
            self.ledit_luz1.setText(
                self.repositorio.accionar_puerta_ventana("encender_luz", codigo, habitacion, tipo))
            self.btn_luz1.setText("Apagar")

        elif self.btn_luz1.text() == "Apagar":
            self.ledit_luz1.setText(
                self.repositorio.accionar_puerta_ventana("apagar_luz", codigo, habitacion, tipo))
            self.btn_luz1.setText("Encender")

    def accion_luz_2(self):
        codigo = "luz_2"
        habitacion = "habitacion"
        tipo = ""
        if self.btn_luz2.text() == "Encender":
            self.ledit_luz2.setText(
                self.repositorio.accionar_puerta_ventana("encender_luz", codigo, habitacion, tipo))
            self.btn_luz2.setText("Apagar")

        elif self.btn_luz2.text() == "Apagar":
            self.ledit_luz2.setText(
                self.repositorio.accionar_puerta_ventana("apagar_luz", codigo, habitacion, tipo))
            self.btn_luz2.setText("Encender")

    def accion_luz_3(self):
        codigo = "luz_3"
        habitacion = "living"
        tipo = ""
        if self.btn_luz3.text() == "Encender":
            self.ledit_luz3.setText(
                self.repositorio.accionar_puerta_ventana("encender_luz", codigo, habitacion, tipo))
            self.btn_luz3.setText("Apagar")

        elif self.btn_luz3.text() == "Apagar":
            self.ledit_luz3.setText(
                self.repositorio.accionar_puerta_ventana("apagar_luz", codigo, habitacion, tipo))
            self.btn_luz3.setText("Encender")

    def accion_luz_4(self):
        codigo = "luz_4"
        habitacion = "terraza"
        tipo = ""
        if self.btn_luz4.text() == "Encender":
            self.ledit_luz4.setText(
                self.repositorio.accionar_puerta_ventana("encender_luz", codigo, habitacion, tipo))
            self.btn_luz4.setText("Apagar")

        elif self.btn_luz4.text() == "Apagar":
            self.ledit_luz4.setText(
                self.repositorio.accionar_puerta_ventana("apagar_luz", codigo, habitacion, tipo))
            self.btn_luz4.setText("Encender")

    #Acciones de movimiento
    def accion_movimiento_1mas(self):
        habitacion = "marquesina"
        cantrand = random.randint(1,5)
        self.ledit_movimiento1.setText(self.repositorio.agregar_persona_habitacion("actualizarCantidad", habitacion, str(cantrand)))

    def accion_movimiento_1menos(self):
        habitacion = "marquesina"
        cantrand = 0
        self.ledit_movimiento1.setText(self.repositorio.agregar_persona_habitacion("actualizarCantidad", habitacion, str(cantrand)))
        self.cambiar_mensajes_a_apagado()


    def accion_movimiento_2mas(self):
        habitacion = "living_room"
        cantrand = random.randint(1,5)
        self.ledit_movimiento2.setText(self.repositorio.agregar_persona_habitacion("actualizarCantidad", habitacion, str(cantrand)))

    def accion_movimiento_2menos(self):
        habitacion = "living_room"
        cantrand = 0
        self.ledit_movimiento2.setText(self.repositorio.agregar_persona_habitacion("actualizarCantidad", habitacion, str(cantrand)))
        self.cambiar_mensajes_a_apagado()

    def accion_movimiento_3mas(self):
        habitacion = "patio"
        cantrand = random.randint(1,5)
        self.ledit_movimiento3.setText(self.repositorio.agregar_persona_habitacion("actualizarCantidad", habitacion, str(cantrand)))

    def accion_movimiento_3menos(self):
        habitacion = "patio"
        cantrand = 0
        self.ledit_movimiento3.setText(self.repositorio.agregar_persona_habitacion("actualizarCantidad", habitacion, str(cantrand)))
        self.cambiar_mensajes_a_apagado()

    def accion_movimiento_4mas(self):
        habitacion = "master_bedroom"
        cantrand = random.randint(1,5)
        self.ledit_movimiento4.setText(self.repositorio.agregar_persona_habitacion("actualizarCantidad", habitacion, str(cantrand)))

    def accion_movimiento_4menos(self):
        habitacion = "master_bedroom"
        cantrand = 0
        self.ledit_movimiento4.setText(self.repositorio.agregar_persona_habitacion("actualizarCantidad", habitacion, str(cantrand)))
        self.cambiar_mensajes_a_apagado()

    def cambiar_mensajes_a_apagado(self):
        if self.ledit_movimiento1.text() == "0" and self.ledit_movimiento2.text() == "0" and self.ledit_movimiento3.text() == "0" and self.ledit_movimiento4.text() == "0":
            self.repositorio.apagar_todo()
            if self.btn_puerta1.text() == "Cerrar":
                self.ledit_puerta1.setText("False")
                self.btn_puerta1.setText("Abrir")
            if self.btn_puerta2.text() == "Cerrar":
                self.ledit_puerta2.setText("False")
                self.btn_puerta2.setText("Abrir")
            if self.btn_puerta3.text() == "Cerrar":
                self.ledit_puerta3.setText("False")
                self.btn_puerta3.setText("Abrir")
            if self.btn_puerta4.text() == "Cerrar":
                self.ledit_puerta4.setText("False")
                self.btn_puerta4.setText("Abrir")
            if self.btn_ventana1.text() == "Cerrar":
                self.ledit_ventana1.setText("False")
                self.btn_ventana1.setText("Abrir")
            if self.btn_ventana2.text() == "Cerrar":
                self.ledit_ventana2.setText("False")
                self.btn_ventana2.setText("Abrir")
            if self.btn_ventana3.text() == "Cerrar":
                self.ledit_ventana3.setText("False")
                self.btn_ventana3.setText("Abrir")
            if self.btn_ventana4.text() == "Cerrar":
                self.ledit_ventana4.setText("False")
                self.btn_ventana4.setText("Abrir")
            if self.btn_luz1.text() == "Apagar":
                self.ledit_luz1.setText("False")
                self.btn_luz1.setText("Encender")
            if self.btn_luz2.text() == "Apagar":
                self.ledit_luz2.setText("False")
                self.btn_luz2.setText("Encender")
            if self.btn_luz3.text() == "Apagar":
                self.ledit_luz3.setText("False")
                self.btn_luz3.setText("Encender")
            if self.btn_luz4.text() == "Apagar":
                self.ledit_luz4.setText("False")
                self.btn_luz4.setText("Encender")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

