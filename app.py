feature/read
import os

main
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
DATA_FILE = 'dados.txt'

def ler_dados():
    itens = []
    if not os.path.exists(DATA_FILE):
        open(DATA_FILE, 'w', encoding='utf-8').close()
        
    with open(DATA_FILE, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.strip()
            if line:
                partes = line.split('|')
                if len(partes) == 3:
                    itens.append({
                        'id': int(partes[0]),
                        'nome': partes[1],
                        'status': partes[2]
                    })
    return itens

def salvar_todos(itens):
    with open(DATA_FILE, 'w', encoding='utf-8') as f:
        for item in itens:
            f.write(f"{item['id']}|{item['nome']}|{item['status']}\n")

@app.route('/')
def index():
    itens = ler_dados()
    return render_template('index.html', itens=itens)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form.get('nome')
    status = request.form.get('status', 'Pendente')
    itens = ler_dados()
    
    novo_id = max([i['id'] for i in itens], default=0) + 1
    itens.append({'id': novo_id, 'nome': nome, 'status': status})
    salvar_todos(itens)
    return redirect(url_for('index'))

@app.route('/edit/<int:item_id>', methods=['POST'])
def edit(item_id):
    novo_nome = request.form.get('nome')
    novo_status = request.form.get('status')
    itens = ler_dados()
    
    for item in itens:
        if item['id'] == item_id:
            item['nome'] = novo_nome
            item['status'] = novo_status
            break
            
    salvar_todos(itens)
    return redirect(url_for('index'))

@app.route('/delete/<int:item_id>')
def delete(item_id):
    itens = ler_dados()
    itens = [i for i in itens if i['id'] != item_id]
    salvar_todos(itens)
    return redirect(url_for('index'))

if __name__ == '__main__':
    feature/read
    app.run(debug=True)

    app.run(debug=True)
main
