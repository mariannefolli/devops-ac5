from flask import Flask, json, request, jsonify
from flaskext.mysql import MySQL

import os


mysql = MySQL()
app = Flask(__name__)

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'mudar123'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_DB'] = 'ac5'
app.config['MYSQL_DATABASE_PORT'] = 3309

mysql.init_app(app)

@app.route('/')
def main():
    return json.dumps({'teste': 'ok'})

@app.route('/insert',methods=['POST'])
def insert():
    conn = None
    cursor = None
    try:
        nome = request.form['nome']
        idade = request.form['idade']
        cpf = request.form['cpf']
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute(f"insert into usuario(cpf, nome, idade) values ('{cpf}', '{nome}', '{idade}')")
        conn.commit()
        return jsonify({'message': 'Usuário cadastrado!'})
    except Exception as e:
        print(e)
        return json.dumps({'message': 'Um erro inesperado aconteceu!'}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

@app.route('/select',methods=['GET'])
def getUsers():
    conn = None
    cursor = None
    result = []
    try:
        conn = mysql.connect()
        cursor = conn.cursor()
        print('cursor criado')
        cursor.execute("select cpf, nome, idade from usuario")
        data = cursor.fetchall()
        for item in data:
            result.append({'cpf': item[0], 'nome': item[1], 'idade': item[2]})
        return jsonify(result)
    except Exception as e:
        print(e)
        return json.dumps({'message': 'Um erro inesperado aconteceu!'}), 500
    finally:
        if cursor is not None:
            cursor.close()
        if conn is not None:
            conn.close()

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host='0.0.0.0', port=port)