from flask import Flask, jsonify, request

meuApp = Flask(__name__)
meuApp.config['JSON_SORT_KEYS'] = False


alunos = [  
        {"id":1, "nome":"Marlon", "idade":21, "turma":"3ºA", "data de nascimento": "18/06/2003", "nota do primeiro semestre":8.0,"nota do segundo semestre":9.0, "média final":8.5},
        {"id":2, "nome":"Bianca", "idade":18, "turma":"3ºB", "data de nascimento": "08/02/2006", "nota do primeiro semestre":7.0,"nota do segundo semestre":8.0, "média final":7.5},
        {"id":3, "nome":"Lucas", "idade":20, "turma":"3ºB", "data de nascimento": "14/11/2004", "nota do primeiro semestre":7.5,"nota do segundo semestre":7.0, "média final":7.25},
        {"id":4, "nome":"João", "idade":22, "turma":"3ºA", "data de nascimento": "23/07/2002", "nota do primeiro semestre":6.0,"nota do segundo semestre":8.0, "média final":7.0},
        {"id":5, "nome":"Katarina", "idade":25, "turma":"3ºA", "data de nascimento": "10/08/1999", "nota do primeiro semestre":5.0,"nota do segundo semestre":9.0, "média final":7.0},
        {"id":6, "nome":"Luiza", "idade":23, "turma":"3ºB", "data de nascimento": "19/12/2001", "nota do primeiro semestre":10.0,"nota do segundo semestre":7.0, "média final":8.5},
    ]

@meuApp.route('/alunos', methods=['GET'])
def get_alunos():
    return jsonify({'Alunos':alunos }), 404

@meuApp.route('/alunos', methods=['POST'])
def create_aluno():
    data = request.json
    aluno = {
        'id': len(alunos) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'turma': data['turma'],
        'data de nascimento': data['data de nascimento'],
        'nota do primeiro semestre': data['nota do primeiro semestre'],
        'nota do segundo semestre': data['nota do segundo semestre'],
        'média final': data['média final'],
    }
    alunos.append(aluno)
    return jsonify(
        mensagem='Aluno cadastrado com sucesso.',
        aluno=aluno
        ), 201

@meuApp.route('/alunos/<int:aluno_id>', methods=['GET'])
def get_aluno(aluno_id):
    for aluno in alunos:
        print(aluno)
        if aluno['id'] == aluno_id:
            return aluno
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

@meuApp.route('/alunos/<int:aluno_id>', methods=['PUT'])
def update_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            data = request.json
            aluno['nome'] = data.get('nome', aluno['nome'])
            aluno['idade'] = data.get('idade', aluno['idade'])
            aluno['turma'] = data.get('turma', aluno['turma'])
            aluno['data de nascimento'] = data.get('data de nascimento', aluno['data de nascimento'])
            aluno['nota do primeiro semestre'] = data.get('nota do primeiro semestre', aluno['nota do primeiro semestre'])
            aluno['nota do segundo semestre'] = data.get('nota do segundo semestre', aluno['nota do segundo semestre'])
            aluno['média final'] = data.get('média final', aluno['média final'])
            return jsonify(aluno)
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

@meuApp.route('/alunos/<int:aluno_id>', methods=['DELETE'])
def delete_aluno(aluno_id):
    for aluno in alunos:
        if aluno['id'] == aluno_id:
            alunos.remove(aluno)
            return jsonify({'mensagem': 'Aluno removido'})
    return jsonify({'mensagem': 'Aluno não encontrado'}), 404

if __name__ == '__main__':
    meuApp.run(debug=True)