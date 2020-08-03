from flask import Flask, render_template, url_for
from pyswip import Prolog
app = Flask(__name__)

@app.route('/')
def hello_world():
   prolog = Prolog()
   prolog.consult("C:\\Users\\jmlma\\Documents\\GitHub\\arbol-genealogico-prolog\\smart-hub-prolog\\ProyectoFinal_Alaila1.pl")
   return render_template('index.html')
