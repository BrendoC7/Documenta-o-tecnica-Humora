from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, date

db = SQLAlchemy()

class Usuario(db.Model):
    __tablename__ = "usuario"

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    senha = db.Column(db.String(200), nullable=False)
    data_nascimento = db.Column(db.Date, nullable=True)
    hobby = db.Column(db.Text, nullable=True)

    def __init__(self, nome, email, senha, data_nascimento=None, hobby=None):
        self.nome = nome
        self.email = email
        self.senha = senha
        self.data_nascimento = data_nascimento
        self.hobby = hobby


class Conversa(db.Model):
    __tablename__ = "conversa"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    mensagem_usuario = db.Column(db.Text, nullable=False)
    mensagem_bot = db.Column(db.Text, nullable=False)

    usuario = db.relationship("Usuario", backref=db.backref("conversas", lazy=True))

    def __init__(self, usuario_id, mensagem_usuario, mensagem_bot):
        self.usuario_id = usuario_id
        self.mensagem_usuario = mensagem_usuario
        self.mensagem_bot = mensagem_bot


class Emocao(db.Model):
    __tablename__ = "emocoes"
    
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuario.id'), nullable=False)
    tipo = db.Column(db.String(50), nullable=False)
    intensidade = db.Column(db.Integer, nullable=True)
    observacao = db.Column(db.Text, nullable=True)
    data_criacao = db.Column(db.DateTime, default=datetime.utcnow)

    usuario = db.relationship("Usuario", backref="emocoes")


class RegistroDiario(db.Model):
    __tablename__ = "registro_diario"

    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey("usuario.id"), nullable=False)
    data = db.Column(db.Date, nullable=False)
    emocao = db.Column(db.String(50), nullable=False)
    intensidade = db.Column(db.Integer, nullable=True)
    observacao = db.Column(db.Text, nullable=True)

    usuario = db.relationship("Usuario", backref="registros_diarios")

    def __init__(self, usuario_id, data, emocao, intensidade=None, observacao=None):
        self.usuario_id = usuario_id
        self.data = data
        self.emocao = emocao
        self.intensidade = intensidade
        self.observacao = observacao
