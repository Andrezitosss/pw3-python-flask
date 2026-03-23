from flask import render_template

def init_app(app):

    @app.route('/')
    def home():
        return render_template('index.html')

    @app.route('/games')
    def games():
        titulo = "Silksong"
        ano = 2025
        categoria = "Metroid Van"
        
        game = {
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
                               game=game)

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