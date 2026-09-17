from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
TXT_FILE = 'dados.txt'

@app.route('/')
def index():
    items = []
    try:
        with open(TXT_FILE, 'r', encoding='utf-8') as f:
            for line in f:
                if line.strip():
                    parts = line.strip().split('|')
                    if len(parts) == 3:
                        items.append({'id': parts[0], 'nome': parts[1], 'status': parts[2]})
    except FileNotFoundError:
        pass
    return render_template('index.html', items=items)

@app.route('/add', methods=['POST'])
def add_item():
    nome = request.form.get('nome')
    status = request.form.get('status', 'Pendente')
    if nome:
        next_id = 1
        try:
            with open(TXT_FILE, 'r', encoding='utf-8') as f:
                lines = [l for l in f.readlines() if l.strip()]
                next_id = len(lines) + 1
        except FileNotFoundError:
            pass
        
        with open(TXT_FILE, 'a', encoding='utf-8') as f:
            f.write(f"{next_id}|{nome}|{status}\n")
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
