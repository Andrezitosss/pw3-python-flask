from flask import render_template,request,redirect,url_for, flash, session


from models.database import Game, db, Usuario
from werkzeug.security import generate_password_hash, check_password_hash
from markupsafe import Markup

def init_app(app):
    listaGames = [{"titulo": "CS-GO","ano" :2012, "Categoria" : "FPS Online"}]

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        titulo = "Silksong"
        ano = 2025
        categoria = "Metroid Van"
        
        games = {
            "titulo": "minecraft",
            "ano": 2012,
            "categoria": "Sandbox"
        }

        jogadores = ['Eduardo', 'Ana', 'Guilherme', 'Vitor', 'Antônio']
        
        return render_template('games.html',
                               titulo=titulo,
                               ano=ano,
                               categoria=categoria,
                               jogadores=jogadores,
                               games=games)

    @app.route('/consoles')
    def consoles():
        titulo = "nintendo switch"
        ano = 2017
        categoria = "híbrido"
        jogadores = 4

        return render_template('consoles.html',
                               titulo=titulo,
                               ano=ano,
                               categoria=categoria,
                               jogadores=jogadores)
        
        #ROTA DE CADASTRO DE JOGOS
    @app.route('/cadgames', methods=['GET', 'POST'])
    def cadgames():
        if request.method == 'POST' : 
            listaGames.append({'titulo' : request.form.get('titulo'),'ano' : request.form.get('ano'), 'categoria' : request.form.get('categoria')})
            return redirect(url_for('cadgames'))
        return render_template('cadgames.html',
                               listaGames=listaGames)
        
    # rota de estoque de jogo
    @app.route('/estoque-jogos', methods=['GET', 'POST'])
    @app.route('/estoque-jogos/delete/<int:id>', methods=['GET', 'POST'])
    def estoque_jogos(id=None):   
        if id:
            game = Game.query.get(id)
            if game:
                db.session.delete(game)
                db.session.commit()
                return redirect(url_for('estoque_jogos'))
            
        if request.method == 'POST':
            dados_form = request.form.to_dict()
            
            newGame = Game(
                    titulo=dados_form['titulo'],
                    ano=dados_form['ano'],
                    categoria=dados_form['categoria'],
                    plataforma=dados_form['plataforma'],
                    preco=dados_form['preco'],
                    quantidade=dados_form['quantidade']
                )
            db.session.add(newGame)
            db.session.commit()   
            
        games = Game.query.all()
        return render_template('estoque-jogos.html', games=games)
    
    @app.route('/editar-jogos/<int:id>', methods=['GET', 'POST'])
    def editar_jogos(id):
        game = Game.query.get(id)
        if request.method == 'POST':
            dados_form = request.form.to_dict()
            
            game.titulo = dados_form.get('titulo')
            game.ano = dados_form.get('ano')
            game.categoria = dados_form.get('categoria')
            game.plataforma = dados_form.get('plataforma')
            game.preco = dados_form.get('preco')
            game.quantidade = dados_form.get('quantidade')
            
            db.session.commit()
            return redirect(url_for('estoque_jogos'))
        return render_template('editar-jogos.html', game=game)

    @app.route('/cadastro', methods=['GET', 'POST'])
    def cadastro():
        if request.method == 'POST':

            email = request.form['email']
            senha = request.form['senha']
            usuario = Usuario.query.filter_by(email=email).first()
            if usuario:
                msg = Markup(f"O email {email} já está cadastrado. <a href='/login'>Faça login</a>.")
                flash(msg, 'danger')
                return redirect(url_for('cadastro'))
            senha_criptografada = generate_password_hash(senha, method='scrypt')
            novo_usuario = Usuario(email=email, senha=senha_criptografada)
            db.session.add(novo_usuario)
            db.session.commit()
            msgCad = Markup(f"Usuário {email} cadastrado com sucesso! <a href='/login'>Faça login</a>.")
            flash(msgCad, 'success')
            return redirect(url_for('login'))
        return render_template('cadastro.html')

    @app.route('/login', methods=['GET', 'POST'])
    def login():
        if request.method == 'POST':
            email = request.form['email']
            senha = request.form['senha']
            usuario = Usuario.query.filter_by(email=email).first()
            if usuario and check_password_hash(usuario.senha, senha):
                session['usuario_id'] = usuario.id
                session['usuario_email'] = usuario.email
                flash('Login bem-sucedido!', 'success')
                return redirect(url_for('home'))
            else:
                flash('Email ou senha incorretos.', 'danger')
                return redirect(url_for('login'))
        return render_template('login.html')