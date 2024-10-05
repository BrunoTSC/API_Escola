from flask import Flask, jsonify, request

meuApp = Flask(__name__)
meuApp.config['JSON_SORT_KEYS'] = False


professores = [  
        {"id":1, "nome":"Kleber", "idade":26, "matéria":"DevOps", "observações": None},
        {"id":2, "nome":"Caio", "idade":24, "matéria":"APIs", "observações": None},
        {"id":3, "nome":"Beicinho", "idade":28, "matéria":"Lógica de programação", "observações": None},
        {"id":4, "nome":"Larissa", "idade":25, "matéria":"Soft Skills", "observações": None},
    ]

@meuApp.route('/professores', methods=['GET'])
def get_profs():
    return jsonify({'Professores':professores }), 404

@meuApp.route('/professores', methods=['POST'])
def create_prof():
    data = request.json
    professor = {
        'id': len(professores) + 1,
        'nome': data['nome'],
        'idade': data['idade'],
        'matéria': data['matéria'],
        'observações': data['observações'],
    }
    professores.append(professor)
    return jsonify(
        mensagem='Professor cadastrado com sucesso.',
        professor=professor
        ), 201

@meuApp.route('/profs/<int:prof_id>', methods=['GET'])
def get_prof(prof_id):
    for professor in professores:
        print(professor)
        if professor['id'] == prof_id:
            return professor
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

@meuApp.route('/profs/<int:prof_id>', methods=['PUT'])
def update_prof(prof_id):
    for professor in professores:
        if professor['id'] == prof_id:
            data = request.json
            professor['nome'] = data.get('nome', professor['nome'])
            professor['idade'] = data.get('idade', professor['idade'])
            professor['matéria'] = data.get('matéria', professor['matéria'])
            professor['observações'] = data.get('observações', professor['observações'])
            return jsonify(professor)
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

@meuApp.route('/profs/<int:prof_id>', methods=['DELETE'])
def delete_prof(prof_id):
    for professor in professores:
        if professor['id'] == prof_id:
            professores.remove(professor)
            return jsonify({'mensagem': 'Professor removido'})
    return jsonify({'mensagem': 'Professor não encontrado'}), 404

if __name__ == '__main__':
    meuApp.run(debug=True)