from flask import Flask, jsonify, request

meuApp = Flask(__name__)
meuApp.config['JSON_SORT_KEYS'] = False


turmas = [  
        {"id":1, "descrição":"3A - DevOps", "professor":"Kleber", "ativo": True},
        {"id":2, "descrição":"3A - APIs", "professor":"Caio", "ativo": True},
        {"id":3, "descrição":"3A - Lógica de programação", "professor":"Beicinho", "ativo": True},
        {"id":4, "descrição":"3A - Soft Skills", "professor":"Gustavo", "ativo": True},
    ]

@meuApp.route('/turmas', methods=['GET'])
def get_turmas():
    return jsonify({'Turmas':turmas }), 404

@meuApp.route('/turmas', methods=['POST'])
def create_turma():
    data = request.json
    turma = {
        'id': len(turmas) + 1,
        'descrição': data['descrição'],
        'professor': data['idade'],
        'ativo': data[True or False],
    }

    turmas.append(turma)
    return jsonify(
        mensagem='Turma cadastrado com sucesso.',
        turma=turma
        ), 201

@meuApp.route('/turma/<int:turma_id>', methods=['GET'])
def get_turma(turma_id):
    for turma in turmas:
        print(turma)
        if turma['id'] == turma_id:
            return turma
    return jsonify({'mensagem': 'Turma não encontrada'}), 404

@meuApp.route('/turma/<int:turma_id>', methods=['PUT'])
def update_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            data = request.json
            turma['descrição'] = data.get('descrição', turma['descrição'])
            turma['professor'] = data.get('professor', turma['professor'])
            turma['ativo'] = data.get('ativo', turma['ativo'])

            return jsonify(turma)
    return jsonify({'mensagem': 'Turma não encontrada'}), 404

@meuApp.route('/turma/<int:turma_id>', methods=['DELETE'])
def delete_turma(turma_id):
    for turma in turmas:
        if turma['id'] == turma_id:
            turmas.remove(turma)
            return jsonify({'mensagem': 'Turma removida'})
    return jsonify({'mensagem': 'Turma não encontrada'}), 404

if __name__ == '__main__':
    meuApp.run(debug=True)