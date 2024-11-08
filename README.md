# Proyecto de E-commerce Basado en Microservicios

Este proyecto es una implementación de un sistema de **e-commerce** basado en una arquitectura de **microservicios**. Cada funcionalidad principal (usuarios, productos, pedidos, pagos, envíos) se desarrolla como un microservicio independiente. La comunicación entre los servicios se realiza utilizando **RabbitMQ** para implementar un enfoque **orientado a eventos**.

## Tabla de Contenidos
- [Requisitos](#requisitos)
- [Instalación](#instalación)
- [Ejecución del Proyecto](#ejecución-del-proyecto)
- [Microservicios Disponibles](#microservicios-disponibles)
- [Pruebas de los Endpoints](#pruebas-de-los-endpoints)
- [Notas Adicionales](#notas-adicionales)

## Requisitos
- **Python 3.7 o superior**
- **RabbitMQ** (preferentemente ejecutado con Docker)
- **Docker** (opcional, para correr RabbitMQ)
- Bibliotecas de Python:
  - `Flask` (para crear APIs REST)
  - `pika` (para conectarse a RabbitMQ)

## Instalación
1. **Clonar el repositorio**:
   ```sh
   git clone <URL_DEL_REPOSITORIO>
   cd ecommerce_microservicios
   ```

2. **Crear y activar un entorno virtual** (opcional pero recomendado):
   ```sh
   python -m venv venv
   # En Windows
   venv\Scripts\activate
   # En Linux/macOS
   source venv/bin/activate
   ```

3. **Instalar las dependencias**:
   ```sh
   pip install flask pika
   ```

4. **Iniciar RabbitMQ** (usando Docker):
   ```sh
   docker run -d --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:management
   ```

## Ejecución del Proyecto
Cada microservicio debe ser ejecutado en una terminal separada. Asegúrate de que **RabbitMQ** está corriendo antes de iniciar los microservicios.

1. **Ejecutar el servicio de usuarios**:
   ```sh
   python servicio_usuarios.py
   ```

2. **Ejecutar el servicio de productos**:
   ```sh
   python servicio_productos.py
   ```

3. **Ejecutar el servicio de pedidos**:
   ```sh
   python servicio_pedidos.py
   ```

4. **Ejecutar el servicio de pagos**:
   ```sh
   python servicio_pagos.py
   ```

5. **Ejecutar el servicio de envíos**:
   ```sh
   python servicio_envios.py
   ```

## Microservicios Disponibles

- **URL**: `http://localhost:5003/pedidos`

- **Obtener Detalles de un Producto**:
  - **URL**: `http://localhost:5002/productos/<producto_id>`
  - **Método**: **GET**
  - **Descripción**: Devuelve los detalles específicos de un producto mediante su ID. Ejemplo: `http://localhost:5002/productos/1`.

- **URL**: `http://localhost:5002/productos`

- **URL**: `http://localhost:5001/usuarios`

- **URL**: `http://localhost:5000/`

## Pruebas de los Endpoints
Para probar los endpoints, puedes utilizar herramientas como **Postman** o **cURL**.

- **Ejemplo de Crear un Pedido** (usando cURL):
  ```sh
  curl -X POST http://localhost:5003/pedidos -H "Content-Type: application/json" -d "{\"usuario_id\": 1, \"producto_id\": 2, \"cantidad\": 3}"
  ```

- **Ejemplo de Listar Productos** (usando navegador o cURL):
  ```sh
  curl http://localhost:5002/productos
  ```

## Notas Adicionales
- **RabbitMQ**: Accede al panel de administración de RabbitMQ en `http://localhost:15672`. El usuario y contraseña por defecto son `guest` / `guest`.
- **Orden de Ejecución**: Ejecuta primero **RabbitMQ**, luego cada microservicio en una terminal separada.
- **Aislamiento**: Es altamente recomendable usar un **entorno virtual** (`venv`) para evitar conflictos de versiones de dependencias.

Si tienes algún problema al correr el proyecto o necesitas más información, no dudes en contactarme.

