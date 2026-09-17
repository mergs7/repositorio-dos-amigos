from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Função auxiliar para ler e formatar o arquivo .txt
def ler_dados():
    tarefas = []
    try:
        with open('dados.txt', 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                if line:
                    partes = line.split('|')
                    if len(partes) == 3:
                        tarefas.append({
                            'id': partes[0],
                            'titulo': partes[1],
                            'status': partes[2]
                        })
    except FileNotFoundError:
        open('dados.txt', 'w', encoding='utf-8').close()
    return tarefas

# Rota principal [READ] - Desenvolvida pelo Integrante 2
@app.route('/')
def index():
    tarefas = ler_dados()
    return render_template('index.html', tarefas=tarefas)

if __name__ == '__main__':
    app.run(debug=True)