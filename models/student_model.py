import os
import json
from deepface import DeepFace

DATA_DIR = 'data'
FACE_DIR = 'faces'

class StudentModel:
    def __init__(self, id_matricula, nome_completo):
        self.id_matricula = id_matricula
        self.nome_completo = nome_completo
        self.student_dir = os.path.join(FACE_DIR, id_matricula)
        self.data_file = os.path.join(DATA_DIR, f"{id_matricula}.json")

    def save_image(self, image_file):
        if not os.path.exists(self.student_dir):
            os.makedirs(self.student_dir)
        image_path = os.path.join(self.student_dir, 'face.jpg')
        image_file.save(image_path)

    def save_data(self):
        if not os.path.exists(DATA_DIR):
            os.makedirs(DATA_DIR)
        data = {
            'id_matricula': self.id_matricula,
            'nome_completo': self.nome_completo,
            'image_path': os.path.join(self.student_dir, 'face.jpg')
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def recognize_student(image_file):
        temp_image_path = 'temp.jpg'
        image_file.save(temp_image_path)

        for student_file in os.listdir(DATA_DIR):
            with open(os.path.join(DATA_DIR, student_file), 'r') as f:
                student_data = json.load(f)
                stored_image_path = student_data['image_path']
                try:
                    result = DeepFace.verify(temp_image_path, stored_image_path, model_name='VGG-Face', enforce_detection=False)
                    if result["verified"]:
                        return student_data
                except Exception as e:
                    print(f"Erro ao verificar a imagem: {e}")

        return None