from flask import Flask, redirect
from flask_swagger_ui import get_swaggerui_blueprint
from controllers.student_controller import student_blueprint

app = Flask(__name__)

# Configuração do Swagger UI
SWAGGER_URL = '/docs'
API_URL = '/static/doc.yml'
swaggerui_blueprint = get_swaggerui_blueprint(SWAGGER_URL, API_URL)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Registro do blueprint
app.register_blueprint(student_blueprint)

# Redireciona a rota raiz para '/docs'
@app.route('/')
def home():
    return redirect('/docs')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
