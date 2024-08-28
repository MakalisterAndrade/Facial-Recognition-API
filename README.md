## Descrição da API

Esta API de reconhecimento facial foi desenvolvida para gerenciar o cadastro e reconhecimento de alunos em um sistema de controle de acesso, como a entrada de um refeitório. Utilizando a biblioteca DeepFace para processamento de imagens, a API permite:

- **Cadastro de Alunos**: Armazenar imagens faciais e dados dos alunos, como ID de matrícula e nome completo.
- **Reconhecimento Facial**: Verificar a identidade dos alunos a partir de imagens enviadas, retornando uma confirmação de acesso.

A API é construída usando o framework Flask e segue o padrão MVC (Model-View-Controller) para uma organização clara e manutenção facilitada.

## Exemplo de README

```markdown
# API de Reconhecimento Facial

Esta API foi desenvolvida para gerenciar o cadastro e reconhecimento facial de alunos, facilitando o controle de acesso em ambientes como refeitórios escolares.

## Funcionalidades

- **Cadastro de Alunos**: Permite o armazenamento de imagens faciais e dados dos alunos.
- **Reconhecimento Facial**: Verifica a identidade dos alunos a partir de imagens enviadas.

## Tecnologias Utilizadas

- **Flask**: Framework web em Python.
- **DeepFace**: Biblioteca para reconhecimento facial.
- **Swagger UI**: Documentação interativa da API.

## Estrutura do Projeto

```
face_recognition_api/
├── app.py
├── controllers/
│   └── student_controller.py
├── models/
│   └── student_model.py
├── views/
│   └── student_view.py
├── data/
├── faces/
└── static/
    └── doc.yaml
```

## Como Executar

1. **Clone o repositório**:

   ```bash
   git clone https://github.com/seu-usuario/seu-repositorio.git
   cd seu-repositorio
   ```

2. **Crie um ambiente virtual e instale as dependências**:

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # No Windows: .venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Inicie o servidor**:

   ```bash
   python app.py
   ```

4. **Acesse a documentação Swagger**:

   Abra o navegador e vá para `http://localhost:5000/docs`.

## Endpoints

### Cadastro de Aluno

- **URL**: `/register`
- **Método**: `POST`
- **Parâmetros**:
  - `id_matricula`: ID único do aluno (string)
  - `nome_completo`: Nome completo do aluno (string)
  - `image`: Arquivo de imagem (formato multipart/form-data)
- **Resposta**: Confirmação de cadastro

### Reconhecimento Facial

- **URL**: `/recognize`
- **Método**: `POST`
- **Parâmetros**:
  - `image`: Arquivo de imagem (formato multipart/form-data)
- **Resposta**: Confirmação de acesso ou erro de reconhecimento

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests.

```