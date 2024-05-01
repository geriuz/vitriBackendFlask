from app import app, db
from flask_cors import CORS

from app.models.productos import Productos
from app.schemas.producto import productos_schema, producto_schema

from flask import request, jsonify, make_response

# Configuración CORS para todas la rutas despues de '/api/' https://flask-cors.readthedocs.io/en/latest/
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Ruta para OBTENER todas las productos
@app.route("/api/v1/productos", methods=["GET"])
def obtener_productos():

    productos = Productos.query.all()
    resultado = productos_schema.dump(productos)

    data = {
        'message': 'Todos los productos obtenidos correctamente!!',
        'status': 200,
        'data': resultado
    }
    return make_response(jsonify(data))

# Ruta para CONSULTAR productos por id
@app.route("/api/v1/productos/<int:id>", methods=["GET"])
def obtener_producto(id):

    producto = Productos.query.get(id)

    if(producto):
        resultado = producto_schema.dump(producto)
        data = {
            'message': 'Información de producto por ID!',
            'status': 200,
            'data': resultado
        }
    else:
        data = {
            'message': 'ID de producto invalido!',
            'status': 200
        }
    return make_response(jsonify(data))

# Ruta para CRAER productos por id
@app.route("/api/v1/productos", methods=["POST"])
def crear_producto():

    sku             = request.json.get('sku', '')
    nombre          = request.json.get('nombre', '')
    desc            = request.json.get('desc', '')
    imagen          = request.json.get('imagen', '')
    fichaTecnica    = request.json.get('fichaTecnica', '')
    precio          = request.json.get('precio', '')
    unidadMedida    = request.json.get('unidadMedida', '')
    valorUnidad     = request.json.get('valorUnidad', '')
    categoria_id    = request.json.get('categoria_id')

    nuevo_producto = Productos(
        sku             = sku, 
        nombre          = nombre, 
        desc            = desc, 
        imagen          = imagen, 
        fichaTecnica    = fichaTecnica, 
        precio          = precio, 
        unidadMedida    = unidadMedida,
        valorUnidad     = valorUnidad, 
        categoria_id    = categoria_id
    )

    db.session.add(nuevo_producto)
    db.session.commit()

    resultado = producto_schema.dump(nuevo_producto)

    data = {
        'message': 'Nuevo producto creado!',
        'status': 201,
        'data': resultado
    }
    return make_response(jsonify(data))

# Ruta para ACTUALIZAR productos
@app.route("/api/v1/productos/<int:id>", methods=["PATCH"])
def actualizar_producto(id):

    producto = Productos.query.get(id)

    if(producto):
        if 'sku' in request.json:
            producto.sku = request.json['sku']
        if 'nombre' in request.json:
            producto.nombre = request.json['nombre']
        if 'desc' in request.json:
            producto.desc = request.json['desc']
        if 'imagen' in request.json:
            producto.imagen = request.json['imagen']
        if 'fichaTecnica' in request.json:
            producto.fichaTecnica = request.json['fichaTecnica']
        if 'precio' in request.json:
            producto.precio = request.json['precio']
        if 'unidadMedida' in request.json:
            producto.unidadMedida = request.json['unidadMedida']
        if 'valorUnidad' in request.json:
            producto.valorUnidad = request.json['valorUnidad']
        if 'categoria_id' in request.json:
            producto.categoria_id = request.json['categoria_id']

        db.session.commit()
        resultado = producto_schema.dump(producto)
        
        data = {
            'message': 'Informacón de producto editada correctamente!',
            'status': 200,
            'data': resultado
        }

    else:
        data = {
            'message': 'ID de producto invalido!',
            'status': 200
        }
    return make_response(jsonify(data))



# Ruta para ELIMINAR productos
@app.route("/api/v1/productos/<int:id>", methods=["DELETE"])
def deliminar_producto(id):

    producto = Productos.query.get(id)

    if(producto):
        db.session.delete(producto)
        db.session.commit()

        data = {
            'message': 'Producto eliminado!',
            'status': 200
        }
    else:
        data = {
            'message': 'ID de producto invalido!',
            'status': 200
        }
    return make_response(jsonify(data))