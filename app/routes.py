from flask import render_template, flash, redirect, url_for, flash, request
from app import app, db
from app.forms.medico_form import MedicoForm
from app.controllers.MedicoController import salvar_medico
from app.controllers.MedicoController import listar_medicos
from app.controllers.MedicoController import buscar_medico_por_id
from app.controllers.MedicoController import buscar_medico_por_id, atualizar_medico
from app.controllers.MedicoController import buscar_medico_por_id, excluir_medico


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/medicos/novo', methods=['GET’, ‘POST'])
def novo():
    form = MedicoForm()
    if form.validate_on_submit():
        salvar_medico(form)
        flash("Médico Cadastrado Com Sucesso")
        return redirect(url_for('listar_medicos'))
    return render_template('medico_form.html',form=form)

@app.route('/medicos')
def listar_medicos():
    medicos=  listar_medicos
    return render_template('medico_lista.html', medicos=medicos)


@app.route('/medicos/<int:id>')
def detalhes_medico(id):
    medico = buscar_medico_por_id(id)
    if not medico:
        flash ("Esse médico não foi encontrado")
        return redirect(url_for('listar_medicos'))
    render_template('medico_detalhes.html',medico=medico)



@app.route('/medicos/<int:id>/editar', methods=['GET', 'POST'])
def editar_medico(id):
    medico = buscar_medico_por_id(id)
    if not medico:
        flash('Médico não encontrado.', 'danger')
        return redirect(url_for('listar_medicos'))

    form = MedicoForm(obj=medico)  # Carrega os dados no formulário

    if form.validate_on_submit():
        atualizar_medico(medico, form)
        flash('Médico atualizado com sucesso!', 'success')
        return redirect(url_for('detalhes_medico', id=medico.id))

    return render_template('medico_form.html', form=form)


@app.route('/medicos/<int:id>/excluir', methods=['GET', 'POST'])
def excluir_medico_view(id):
    medico = buscar_medico_por_id(id)
    if not medico:
        flash('Médico não encontrado.')
        return redirect(url_for('listar_medicos'))

    if request.method == 'POST':
        excluir_medico(medico)
        flash('Médico excluído com sucesso.')
        return redirect(url_for('listar_medicos'))

    return render_template('medico_excluir.html', medico=medico)



