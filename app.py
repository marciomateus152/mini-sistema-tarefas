from flask import Flask, render_template, request, redirect, url_for
import sqlite3

aplicativo = Flask(__name__)

def conectar_banco():
    conexao = sqlite3.connect('sistema_avancado.db')
    conexao.row_factory = sqlite3.Row
    return conexao

def inicializar_banco():
    conexao = conectar_banco()
    conexao.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            descricao TEXT,
            categoria TEXT,
            prioridade TEXT,
            data_limite TEXT,
            concluida INTEGER DEFAULT 0
        )
    ''')
    conexao.commit()
    conexao.close()

@aplicativo.route('/')
def pagina_inicial():
    conexao = conectar_banco()
    tarefas_salvas = conexao.execute('SELECT * FROM tarefas ORDER BY concluida ASC, data_limite ASC').fetchall()
    conexao.close()
    return render_template('index.html', lista_tarefas=tarefas_salvas)

@aplicativo.route('/adicionar', methods=['POST'])
def adicionar_tarefa():
    titulo_recebido = request.form['titulo']
    descricao_recebida = request.form['descricao']
    categoria_recebida = request.form['categoria']
    prioridade_recebida = request.form['prioridade']
    data_recebida = request.form['data_limite']

    if titulo_recebido:
        conexao = conectar_banco()
        conexao.execute('''
            INSERT INTO tarefas (titulo, descricao, categoria, prioridade, data_limite) 
            VALUES (?, ?, ?, ?, ?)
        ''', (titulo_recebido, descricao_recebida, categoria_recebida, prioridade_recebida, data_recebida))
        conexao.commit()
        conexao.close()
    return redirect(url_for('pagina_inicial'))

@aplicativo.route('/concluir/<int:identificador>')
def concluir_tarefa(identificador):
    conexao = conectar_banco()
    conexao.execute('UPDATE tarefas SET concluida = 1 WHERE id = ?', (identificador,))
    conexao.commit()
    conexao.close()
    return redirect(url_for('pagina_inicial'))

@aplicativo.route('/excluir/<int:identificador>')
def excluir_tarefa(identificador):
    conexao = conectar_banco()
    conexao.execute('DELETE FROM tarefas WHERE id = ?', (identificador,))
    conexao.commit()
    conexao.close()
    return redirect(url_for('pagina_inicial'))

if __name__ == '__main__':
    inicializar_banco()
    aplicativo.run(debug=True)