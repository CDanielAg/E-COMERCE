# servicio_usuarios.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos en memoria para los usuarios
usuarios = {
    1: {"nombre": "Juan Perez", "email": "juan.perez@example.com"},
    2: {"nombre": "Maria Garcia", "email": "maria.garcia@example.com"}
}

# Ruta para registrar un nuevo usuario
@app.route('/usuarios', methods=['POST'])
def registrar_usuario():
    datos = request.get_json()
    usuario_id = len(usuarios) + 1
    usuarios[usuario_id] = {
        "nombre": datos['nombre'],
        "email": datos['email']
    }
    return jsonify({'mensaje': 'Usuario registrado con éxito', 'usuario_id': usuario_id}), 201

# NUEVA RUTA PARA LISTAR USUARIOS
@app.route('/usuarios', methods=['GET'])
def listar_usuarios():
    return jsonify(usuarios), 200

if __name__ == '__main__':
    app.run(port=5001)
