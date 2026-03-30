from flask import render_template,request,redirect,url_for

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