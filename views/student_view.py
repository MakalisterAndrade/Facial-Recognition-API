from flask import jsonify

class StudentView:
    @staticmethod
    def registration_success():
        return jsonify({"message": "Aluno cadastrado com sucesso!"})

    @staticmethod
    def recognition_success(student):
        return jsonify({"message": "pass", "id_matricula": student['id_matricula'], "nome_completo": student['nome_completo']})

    @staticmethod
    def recognition_failure():
        return jsonify({"message": "Aluno não reconhecido"}), 401