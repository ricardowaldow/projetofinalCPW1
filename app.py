""" Simple Web Page Server from Python with Flask """
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    """ Route to main page """
    return render_template('index.html')

@app.route("/cardapio")
def cardapio():
    """ Route to cardapio page """
    return render_template('cardapio.html')

@app.route("/contato")
def contato():
    """ Route to contato page """
    return render_template('contato.html')

@app.route("/sobre")
def sobre():
    """ Route to sobre page """
    return render_template('sobre.html')
