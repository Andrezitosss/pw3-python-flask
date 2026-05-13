from flask import Flask, render_template
from controllers import routes
import pymysql
from models.database import db, Game
# Carregando o Flask em uma variável
app = Flask(__name__, template_folder='views')  
#__name__ é uma variável de ambiente do Python que tem o nome do módulo atual.
#enviando a variavel app para as rotas
routes.init_app(app)

#definindo o nome do banco de dados
DB_NAME = 'thegames'
#passando o nome do banco para o flask
app.config['DATABASE_NAME'] = DB_NAME
#passando o endereço do banco de dados para o flask
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql://root:@localhost/{DB_NAME}'


# Iniciando o servidor web
if __name__ == '__main__':
    #passando os dados e criando a conexao com o banco
    
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='',
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
    #tentando a conexao
    try:
        with connection.cursor() as cursor:
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME}")
    except Exception as e:
        print(f"Erro ao criar o banco de dados: {error}")
    finally:
        connection.close()
        
        db.init_app(app)
        with app.test_request_context():
            db.create_all()
    app.run(debug=True)
    # Verificando se o app.py for o aruivo principal ele inicia o sevidor 