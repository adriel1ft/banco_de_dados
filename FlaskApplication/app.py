from flask import Flask, render_template, request, redirect, url_for,jsonify
import pymysql
#from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '39*72p16lf'
app.config['MYSQL_DB'] = 'biblioteca'


conexao = pymysql.connect(host=app.config['MYSQL_HOST'], user=app.config['MYSQL_USER'],
                password=app.config['MYSQL_PASSWORD'], db=app.config['MYSQL_DB'])
cursor = conexao.cursor()

@app.route('/adicionar_livro',methods=['POST'])
def add_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        genero = request.form['genero']
        cursor.execute("SELECT * FROM livros WHERE titulo = %s",titulo) 
        livro_existente = cursor.fetchone()

        if livro_existente:
            return jsonify({'mensagem':'Livro já existente'})
        
        cursor.execute("INSERT INTO livros(titulo,autor,genero) VALUES (%s,%s,%s)",(titulo,autor,genero)) 
        conexao.commit()
        return jsonify({'redirect':url_for('exibir'),'mensagem':'Livro cadastrado com sucesso'})

@app.route('/')
def exibir():
    cursor.execute("SELECT * FROM livros")
    rows = cursor.fetchall()
    return render_template('index2.html', data=rows)



    
if __name__ == '__main__':
    app.run(debug=True)
