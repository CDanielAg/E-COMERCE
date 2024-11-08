# servicio_productos.py
from flask import Flask, request, jsonify

app = Flask(__name__)

# Base de datos en memoria para los productos
productos = {
    1: {
        'nombre': 'Laptop',
        'precio': 1200,
        'stock': 10
    },
    2: {
        'nombre': 'Teclado',
        'precio': 30,
        'stock': 25
    },
    3: {
        'nombre': 'Mouse',
        'precio': 15,
        'stock': 50
    }
}

@app.route('/productos', methods=['POST'])
def agregar_producto():
    datos = request.get_json()
    producto_id = len(productos) + 1
    productos[producto_id] = {
        'nombre': datos['nombre'],
        'precio': datos['precio'],
        'stock': datos['stock']
    }
    return jsonify({'mensaje': 'Producto agregado con éxito', 'producto_id': producto_id}), 201

@app.route('/productos', methods=['GET'])
def obtener_productos():
    return jsonify(productos), 200

if __name__ == '__main__':
    app.run(port=5002)
