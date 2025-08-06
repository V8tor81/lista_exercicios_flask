from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length

class MedicoForm(FlaskForm):
    nome_completo = StringField('Nome Completo', validators=[DataRequired(), Length(min=5, max=100)])
    crm = StringField('CRM', validators=[DataRequired(), Length(min=8, max=8)])
    especialidade = SelectField('Especialidade',choices=[('Cardiologia', 'Cardiologia'),('Dermatologia', 'Dermatologia'),('Ginecologia', 'Ginecologia'),('Neurologia', 'Neurologia'),('Ortopedia', 'Ortopedia'),('Pediatria', 'Pediatria'),('Psiquiatria', 'Psiquiatria'),('Urologia', 'Urologia'),('Oftalmologia', 'Oftalmologia'),('Otorrinolaringologia', 'Otorrinolaringologia'),('Endocrinologia', 'Endocrinologia'),('Gastroenterologia', 'Gastroenterologia'),('Pneumologia', 'Pneumologia'),('Reumatologia', 'Reumatologia'),('Oncologia', 'Oncologia'),('Radiologia', 'Radiologia'),('Anestesiologia', 'Anestesiologia'),('Cirurgia Geral', 'Cirurgia Geral'),('Medicina Interna', 'Medicina Interna'),('Medicina de Família', 'Medicina de Família')], validators=[DataRequired()])
    submit = SubmitField('Cadastrar Médico')











