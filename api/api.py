from flask import Flask, jsonify

app = Flask(__name__)

# Lista com o nome de 10 alunos
alunos = [
    "Maria", "João", "Ana", "Pedro", "Carla", 
    "Lucas", "Fernanda", "Mateus", "Sofia", "Thiago"
]

# Rota GET que retorna a lista de alunos
@app.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify(alunos)

if __name__ == '__main__':
    app.run(debug=True)
