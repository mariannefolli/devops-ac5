from flask import Flask, json, request
from flaskext.mysql import MySQL

import os


mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_DB'] = 'teste'
app.config['MYSQL_DATABASE_HOST'] = '172.17.0.7'
#app.config['MYSQL_DATABASE_HOST'] = '172.17.0.7'
mysql.init_app(app)
conn = None


def checkConnection():
    global conn
    if conn is None:
        conn = mysql.connect()

@app.route('/')
def main():
    return json.dumps({'teste': 'ok'})

@app.route('/insert',methods=['POST'])
def insert():
    try:
        checkConnection()
        nome = request.form['nome']
        idade = request.form['idade']
        cpf = request.form['cpf']
        cursor = conn.cursor()
        cursor.execute(f"insert into usuario(cpf, nome, idade) values ('{cpf}', '{nome}', '{idade}')")
        return json.dumps({'message': 'Usuário cadastrado!'})
    except Exception:
        return json.dumps({'message': 'Um erro inesperado aconteceu!'}), 500
    finally:
        cursor.close()

@app.route('/select',methods=['GET'])
def getUsers():
    try:
        checkConnection()
        cursor = conn.cursor()
        cursor.execute("select cpf, nome, idade from usuario")
        data = cursor.fetchall()
        print(data)
        return data
    except Exception:
        return json.dumps({'message': 'Um erro inesperado aconteceu!'}), 500
    finally:
        cursor.close()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)