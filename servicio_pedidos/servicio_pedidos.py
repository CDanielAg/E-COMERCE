# servicio_pedidos.py
from flask import Flask, request, jsonify
import pika
import json

app = Flask(__name__)

# Base de datos en memoria para los pedidos
pedidos = {}

def emitir_evento_pedido_creado(pedido):
    # Conectar con RabbitMQ
    conexion = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    canal = conexion.channel()
    # Declarar la cola donde se enviarán los eventos
    canal.queue_declare(queue='pedidos')
    # Enviar el evento con la información del pedido
    canal.basic_publish(
        exchange='',
        routing_key='pedidos',
        body=json.dumps(pedido)
    )
    print(f" [x] Evento enviado: {pedido}")
    conexion.close()

@app.route('/pedidos', methods=['POST'])
def crear_pedido():
    datos = request.get_json()
    pedido_id = len(pedidos) + 1

    # Almacenar el pedido
    pedidos[pedido_id] = {
        'usuario_id': datos['usuario_id'],
        'producto_id': datos['producto_id'],
        'cantidad': datos['cantidad'],
        'estado': 'Pendiente'
    }

    # Emitir el evento de pedido creado
    emitir_evento_pedido_creado(pedidos[pedido_id])

    return jsonify({'mensaje': 'Pedido creado con éxito', 'pedido_id': pedido_id}), 201

# NUEVA RUTA PARA LISTAR PEDIDOS
@app.route('/pedidos', methods=['GET'])
def listar_pedidos():
    return jsonify(pedidos), 200

if __name__ == '__main__':
    app.run(port=5003)
