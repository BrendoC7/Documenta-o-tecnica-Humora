from flask import request, jsonify
from models import db, Usuario, Conversa, Emocao, RegistroDiario
import bcrypt
import re
from datetime import datetime, date
import pytz

def initialize_routes(app):

    # ===============================
    #       REGISTRO DE USUÁRIO
    # ===============================
    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()

        # Validação de email
        email_regex = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_regex, data.get('email', '')):
            return jsonify({"message": "E-mail inválido!"}), 400

        # Verifica duplicado
        if Usuario.query.filter_by(email=data['email']).first():
            return jsonify({"message": "E-mail já cadastrado!"}), 400

        # Criptografar senha
        senha_hash = bcrypt.hashpw(data['senha'].encode('utf-8'), bcrypt.gensalt())

        usuario = Usuario(
            nome=data['nome'],
            email=data['email'],
            senha=senha_hash.decode('utf-8'),
            hobby=data.get("hobby"),
            data_nascimento=None
        )

        # Converter data se enviada
        if data.get("data_nascimento"):
            try:
                usuario.data_nascimento = datetime.strptime(
                    data["data_nascimento"], "%Y-%m-%d"
                ).date()
            except:
                return jsonify({"message": "Formato de data inválido. Use YYYY-MM-DD"}), 400

        db.session.add(usuario)
        db.session.commit()

        return jsonify({"message": "Usuário registrado com sucesso!"}), 201

    # ===============================
    #             LOGIN
    # ===============================
    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        usuario = Usuario.query.filter_by(email=data['email']).first()

        if not usuario:
            return jsonify({"message": "E-mail não encontrado!"}), 404

        if not bcrypt.checkpw(
            data['senha'].encode('utf-8'),
            usuario.senha.encode('utf-8')
        ):
            return jsonify({"message": "Senha incorreta!"}), 401

        return jsonify({
            "message": "Login bem-sucedido!",
            "usuario_id": usuario.id,
            "nome": usuario.nome
        }), 200

    # ===============================
    #           PERFIL (GET)
    # ===============================
    @app.route('/usuario/<int:usuario_id>', methods=['GET'])
    def obter_usuario(usuario_id):
        usuario = Usuario.query.get(usuario_id)

        if not usuario:
            return jsonify({"error": "Usuário não encontrado"}), 404

        return jsonify({
            "id": usuario.id,
            "nome": usuario.nome,
            "email": usuario.email,
            "hobby": usuario.hobby,
            "data_nascimento": usuario.data_nascimento.strftime("%Y-%m-%d")
                if usuario.data_nascimento else None
        }), 200

    # ===============================
    #        ATUALIZAR PERFIL
    # ===============================
    @app.route('/usuario/<int:usuario_id>/atualizar', methods=['PUT'])
    def atualizar_usuario(usuario_id):
        data = request.get_json()

        usuario = Usuario.query.get(usuario_id)
        if not usuario:
            return jsonify({"message": "Usuário não encontrado"}), 404

        usuario.hobby = data.get("hobby", usuario.hobby)

        if data.get("data_nascimento"):
            try:
                usuario.data_nascimento = datetime.strptime(
                    data["data_nascimento"], "%Y-%m-%d"
                ).date()
            except ValueError:
                return jsonify({"message": "Formato de data inválido. Use YYYY-MM-DD"}), 400

        db.session.commit()

        return jsonify({"message": "Informações atualizadas com sucesso!"}), 200

    # ===============================
    #               CHAT
    # ===============================
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

    # ===============================
    #       REGISTRO DE EMOÇÃO
    # ===============================
    @app.route('/emocao', methods=['POST'])
    def registrar_emocao():
        data = request.get_json()

        if 'usuario_id' not in data or 'tipo' not in data:
            return jsonify({"message": "Campos obrigatórios faltando!"}), 400

        usuario_id = data['usuario_id']
        usuario = Usuario.query.get(usuario_id)

        if not usuario:
            return jsonify({"message": "Usuário não encontrado!"}), 404

        # Horário de SP
        brt = pytz.timezone('America/Sao_Paulo')
        hoje_brt = datetime.now(brt).date()

        # Evitar múltiplos registros
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

    # ===============================
    #   REGISTRO DIÁRIO DO CALENDÁRIO
    # ===============================
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

    # ===============================
    #       BUSCAR MÊS NO CALENDÁRIO
    # ===============================
    @app.route('/calendario/<int:usuario_id>/<int:ano>/<int:mes>', methods=['GET'])
    def calendario_mes(usuario_id, ano, mes):

        registros = RegistroDiario.query.filter(
            RegistroDiario.usuario_id == usuario_id,
            db.extract('year', RegistroDiario.data) == ano,
            db.extract('month', RegistroDiario.data) == mes
        ).all()

        dias = [{
            "dia": r.data.day,
            "emocao": r.emocao,
            "intensidade": r.intensidade,
            "observacao": r.observacao
        } for r in registros]

        return jsonify({
            "usuario_id": usuario_id,
            "ano": ano,
            "mes": mes,
            "registros": dias
        }), 200
