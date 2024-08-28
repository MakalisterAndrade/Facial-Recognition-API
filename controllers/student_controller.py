from flask import Blueprint, request, jsonify
from models.student_model import StudentModel
from views.student_view import StudentView

student_blueprint = Blueprint('student', __name__)

@student_blueprint.route('/register', methods=['POST'])
def register():
    id_matricula = request.form['id_matricula']
    nome_completo = request.form['nome_completo']
    image_file = request.files['image']

    student = StudentModel(id_matricula, nome_completo)
    student.save_image(image_file)
    student.save_data()

    return StudentView.registration_success()

@student_blueprint.route('/recognize', methods=['POST'])
def recognize():
    image_file = request.files['image']
    student = StudentModel.recognize_student(image_file)

    if student:
        return StudentView.recognition_success(student)
    else:
        return StudentView.recognition_failure()