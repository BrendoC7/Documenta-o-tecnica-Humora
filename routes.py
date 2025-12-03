from flask import request, jsonify
from models import db, Usuario, Conversa, Emocao, RegistroDiario
import bcrypt
import re 
from datetime import datetime, date
import pytz

def initialize_routes(app):

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()

        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, data.get('email', '')):
            return jsonify({"message": "E-mail inválido!"}), 400

        usuario_existente = Usuario.query.filter_by(email=data['email']).first()
        if usuario_existente:
            return jsonify({"message": "E-mail já cadastrado!"}), 400

        senha_hash = bcrypt.hashpw(data['senha'].encode('utf-8'), bcrypt.gensalt())
        usuario = Usuario(
            nome=data['nome'],
            email=data['email'],
            senha=senha_hash.decode('utf-8')
        )

        db.session.add(usuario)
        db.session.commit()

        return jsonify({"message": "Usuário registrado com sucesso!"}), 201

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        usuario = Usuario.query.filter_by(email=data['email']).first()

        if not usuario:
            return jsonify({"message": "E-mail não encontrado!"}), 404

        if not bcrypt.checkpw(data['senha'].encode('utf-8'), usuario.senha.encode('utf-8')):
            return jsonify({"message": "Senha incorreta!"}), 401

        return jsonify({
            "message": "Login bem-sucedido!",
            "usuario_id": usuario.id,
            "nome": usuario.nome
        }), 200

    @app.route('/chat', methods=['POST'])
    def chat():
        data = request.get_json()
        usuario_id = data['usuario_id']
        mensagem = data['mensagem']
        resposta_bot = "Olá! Esta é uma mensagem automática de resposta."

        conversa = Conversa(
            usuario_id=usuario_id,
            mensagem_usuario=mensagem,
            mensagem_bot=resposta_bot
        )

        db.session.add(conversa)
        db.session.commit()

        return jsonify({"resposta": resposta_bot}), 200

    @app.route('/emocao', methods=['POST'])
    def registrar_emocao():
        data = request.get_json()

        if 'usuario_id' not in data or 'tipo' not in data:
            return jsonify({"message": "Campos obrigatórios faltando!"}), 400

        usuario_id = data['usuario_id']

        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return jsonify({"message": "Usuário não encontrado!"}), 404

        brt = pytz.timezone('America/Sao_Paulo')
        hoje_brt = datetime.now(brt).date()

        emocao_existente = Emocao.query.filter(
            Emocao.usuario_id == usuario_id,
            db.func.date(Emocao.data_criacao) == hoje_brt
        ).first()

        if emocao_existente:
            return jsonify({"message": "Você já registrou uma emoção hoje!"}), 400

        emocao = Emocao(
            usuario_id=usuario_id,
            tipo=data['tipo'],
            intensidade=data.get('intensidade'),
            observacao=data.get('observacao'),
            data_criacao=datetime.now(brt)
        )

        db.session.add(emocao)
        db.session.commit()

        return jsonify({
            "message": "Emoção registrada com sucesso!",
            "data_criacao": emocao.data_criacao.isoformat()
        }), 201

    @app.route('/calendario/registrar', methods=['POST'])
    def registrar_calendario():
        data = request.get_json()

        usuario_id = data.get("usuario_id")
        emocao = data.get("emocao")
        intensidade = data.get("intensidade")
        observacao = data.get("observacao")

        if not usuario_id or not emocao:
            return jsonify({"message": "Campos obrigatórios faltando!"}), 400

        brt = pytz.timezone("America/Sao_Paulo")
        hoje = datetime.now(brt).date()

        registro_existente = RegistroDiario.query.filter_by(
            usuario_id=usuario_id,
            data=hoje
        ).first()

        if registro_existente:
            return jsonify({"message": "Você já registrou sua emoção hoje!"}), 400

        registro = RegistroDiario(
            usuario_id=usuario_id,
            data=hoje,
            emocao=emocao,
            intensidade=intensidade,
            observacao=observacao
        )

        db.session.add(registro)
        db.session.commit()

        return jsonify({"message": "Registro salvo!", "data": str(hoje)}), 201

    @app.route('/calendario/<int:usuario_id>/<int:ano>/<int:mes>', methods=['GET'])
    def calendario_mes(usuario_id, ano, mes):

        registros = RegistroDiario.query.filter(
            RegistroDiario.usuario_id == usuario_id,
            db.extract('year', RegistroDiario.data) == ano,
            db.extract('month', RegistroDiario.data) == mes
        ).all()

        dias = []
        for r in registros:
            dias.append({
                "dia": r.data.day,
                "emocao": r.emocao,
                "intensidade": r.intensidade,
                "observacao": r.observacao
            })

        return jsonify({
            "usuario_id": usuario_id,
            "ano": ano,
            "mes": mes,
            "registros": dias
        }), 200
