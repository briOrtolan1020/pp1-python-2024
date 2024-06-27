from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/vehiculos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import Marca, Tipo 


listado_nombres = ['Ana', 'Juan', 'Jose']

diccionario_nombres=[
    dict (
        nombre='Ana',
        edad=30,
        pais='Argentina',
        
    ),
    dict (
        nombre='Pablo',
        edad=45,
        pais='Argentina',
    ),
    dict (
        nombre='Juan',
        edad=27,
        pais='Argentina',
    ),
]

@app.route("/") 
def index():
    return render_template('index.html')


