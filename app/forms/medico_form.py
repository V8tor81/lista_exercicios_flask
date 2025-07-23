from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField, SelectField, EmailField
from wtforms.validators import DataRequired, Length, Email

class CadastrarForm(FlaskForm):
    nome_completo= StringField('Usuário', validators=[DataRequired()])
    username = StringField('Usuário', validators=[DataRequired()])
    crm =StringField('crm', validators=[DataRequired(), Length(min=8, max=8)])
    especialidade= SelectField('Especialidade', validators=[DataRequired()],choices=[( 'Cardiologia', 'Dermatologia', 'Ginecologia', 'Neurologia', 'Ortopedia', 'Pediatria', 'Psiquiatria', 'Urologia', 'Oftalmologia', 'Otorrinolaringologia', 'Endocrinologia', 'Gastroenterologia', 'Pneumologia', 'Reumatologia', 'Oncologia', 'Radiologia', 'Anestesiologia', 'Cirurgia  Geral', 'Medicina Interna', 'Medicina de Família' )])
    email= EmailField ('eMAIL', validators=[DataRequired(), Email()])
    submit = SubmitField('Cadastrar Médico')











