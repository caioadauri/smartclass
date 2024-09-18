from flask import Flask,jsonify, request, render_template
from controller.professor_controller import Professores
from model.professor_model import professores
from model.aluno_model import alunos
from model.turma_model import turmas

#professor = Professores()

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/status', methods=['GET'])
def status():
    dados = {"status":"200, ok"}
    return jsonify(dados)

@app.route('/professor', methods=['GET'])
def verifica_professor():
    dados = professores
    return jsonify(dados)

@app.route('/aluno',methods=['GET'])
def verifica_aluno():
    dados = alunos
    return jsonify(dados)

@app.route('/turma',methods=['GET'])
def verifica_turma():
    dados = turmas
    return jsonify(dados)


if __name__=='__main__':
    app.run(debug=True)
