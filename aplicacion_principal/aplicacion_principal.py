# aplicacion_principal.py
from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

URL_SERVICIO_USUARIOS = "http://localhost:5001"
URL_SERVICIO_PRODUCTOS = "http://localhost:5002"
URL_SERVICIO_PEDIDOS = "http://localhost:5003"
URL_SERVICIO_PAGOS = "http://localhost:5004"
URL_SERVICIO_ENVIOS = "http://localhost:5005"

@app.route('/')
def inicio():
    # Obtener todos los productos
    respuesta_productos = requests.get(f"{URL_SERVICIO_PRODUCTOS}/productos")
    productos = respuesta_productos.json()

    return render_template('index.html', productos=productos)

@app.route('/crear_pedido', methods=['POST'])
def crear_pedido():
    usuario_id = request.form['usuario_id']
    producto_id = request.form['producto_id']
    cantidad = int(request.form['cantidad'])

    # Crear un pedido
    datos_pedido = {
        'usuario_id': usuario_id,
        'producto_id': producto_id,
        'cantidad': cantidad
    }
    respuesta_pedido = requests.post(f"{URL_SERVICIO_PEDIDOS}/pedidos", json=datos_pedido)
    return jsonify(respuesta_pedido.json()), respuesta_pedido.status_code

if __name__ == '__main__':
    app.run(port=5000)
