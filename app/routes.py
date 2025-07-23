from flask import render_template, flash, redirect, url_for
from app import app, db
from app.forms.medico_form import medicoform


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/medicos', methods=['GET’, ‘POST'])
def novo():
    formulario = medicoform()
    return render_template('medico_form.html', title='medicoform',form=formulario)


