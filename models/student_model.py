import os
import json
from deepface import DeepFace

# Diretórios necessários
DATA_DIR = 'data'
FACE_DIR = 'faces'
TEMP_DIR = 'temp'

# Crie as pastas se não existirem
os.makedirs(DATA_DIR, exist_ok=True)
os.makedirs(FACE_DIR, exist_ok=True)
os.makedirs(TEMP_DIR, exist_ok=True)

class StudentModel:
    def __init__(self, id_matricula, nome_completo):
        self.id_matricula = id_matricula
        self.nome_completo = nome_completo
        self.student_dir = os.path.join(FACE_DIR, id_matricula)
        os.makedirs(self.student_dir, exist_ok=True)
        self.data_file = os.path.join(DATA_DIR, f"{id_matricula}.json")

    def save_image(self, image_file):
        image_path = os.path.join(self.student_dir, 'face.jpg')
        image_file.save(image_path)

    def save_data(self):
        data = {
            'id_matricula': self.id_matricula,
            'nome_completo': self.nome_completo,
            'image_path': os.path.join(self.student_dir, 'face.jpg')
        }
        with open(self.data_file, 'w') as f:
            json.dump(data, f)

    @staticmethod
    def recognize_student(image_file):
        temp_image_path = os.path.join(TEMP_DIR, 'temp.jpg')
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
