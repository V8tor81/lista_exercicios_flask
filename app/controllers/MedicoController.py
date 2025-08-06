from app import db
from flask import flash
from app.models.medico import Medico


def salvar_medico(form):
    novo_medico = Medico(
        nome_completo=form.nome_completo.data,
        crm=form.crm.data,
        especialidade=form.especialidade.data
    )
    db.session.add(novo_medico)
    db.session.commit()
    flash("Médico cadastrado com sucesso!", "success")


def listar_medicos():
    return Medico.query.all()

def buscar_medico_por_id(id):
    return Medico.query.get(id)

def atualizar_medico(medico, form):
    medico.nome_completo = form.nome_completo.data
    medico.username = form.username.data
    medico.crm = form.crm.data
    medico.especialidade = form.especialidade.data
    medico.email = form.email.data
    db.session.commit()
    flash("Médico atualizado com sucesso!", "success")

def excluir_medico(medico):
    db.session.delete(medico)
    db.session.commit()
    flash("Médico excluído com sucesso!", "success")


