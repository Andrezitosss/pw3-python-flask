from flask import Flask, render_template

# Carregando o Flask em uma variável
app = Flask(__name__, template_folder='views')  
#__name__ é uma variável de ambiente do Python que tem o nome do módulo atual.

# Criando a rota principal do site
@app.route('/')
# def serve para criar funções no Python
def home():
    return render_template('index.html')

@app.route('/lista')
def lista():
    return render_template('lista.html')

@app.route('/formulario')
def formulario():
    return render_template('formulario.html')

# Iniciando o servidor web
if __name__ == '__main__':
    app.run(debug=True)
    # Verificando se o app.py for o aruivo principal ele inicia o sevidor 