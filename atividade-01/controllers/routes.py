from flask import app, render_template,request,redirect,url_for    

def init_app(app):
    
    listaComentarios = []
    @app.route('/')
    # def serve para criar funções no Python
    def home():
        return render_template('index.html')

    @app.route('/lista')
    def lista():
        return render_template('lista.html')

    @app.route('/formulario', methods=['GET', 'POST'])
    def formulario():
        if request.method == 'POST':
            listaComentarios.append({
                'jogo': request.form.get('jogo'),
                'nome': request.form.get('nome'),
                'email': request.form.get('email'),
                'comentario': request.form.get('comentario')
            })

            return redirect(url_for('formulario'))

        return render_template(
            'formulario.html',
            listaComentarios=listaComentarios
        )