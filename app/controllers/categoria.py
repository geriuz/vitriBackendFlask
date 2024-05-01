from app import app, db
from flask_cors import CORS

from app.models.categorias import Categorias
from app.schemas.categoria import categorias_schema, categoria_schema

from flask import request, jsonify, make_response

cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

# Ruta para CONSULTAR todas las categorias
@app.route("/api/v1/categorias", methods=["GET"])
def obtener_categorias():

    categorias = Categorias.query.all()
    resultado = categorias_schema.dump(categorias)

    data = {
        'message': 'Todas las categorias obtenidas correctamente!',
        'status': 200,
        'data': resultado
    }
    return make_response(jsonify(data))

# Ruta para CONSULTAR categorias por id
@app.route("/api/v1/categorias/<int:id>", methods=["GET"])
def obtener_categoria(id):

    categoria = Categorias.query.get(id)

    if(categoria):
        resultado = categoria_schema.dump(categoria)
        data = {
            'message': 'Información de categoria por ID!!',
            'status': 200,
            'data': resultado
        }
    else:
        data = {
            'message': 'ID de categoria invalido!',
            'status': 200
        }
    return make_response(jsonify(data))

# Ruta para CRAER categorias por id
@app.route("/api/v1/categorias", methods=["POST"])
def crear_categoria():

    nombre  = request.json.get('nombre', '')
    desc    = request.json.get('desc', '')

    nueva_categoria = Categorias(
        nombre  = nombre, 
        desc    = desc
    )
    
    db.session.add(nueva_categoria)
    db.session.commit()

    resultado = categoria_schema.dump(nueva_categoria)

    data = {
        'message': 'Nueva categoria creada!',
        'status': 201,
        'data': resultado
    }
    return make_response(jsonify(data))

# Ruta para ACTUALIZAR categorias
@app.route("/api/v1/categorias/<int:id>", methods=["PATCH"])
def actualizar_categoria(id):

    categoria = Categorias.query.get(id)

    if(categoria):
        if 'nombre' in request.json:
            categoria.nombre = request.json['nombre']
        if 'desc' in request.json:
            categoria.descripcion = request.json['desc']

        db.session.commit()
        resultado = categoria_schema.dump(categoria)
        
        data = {
            'message': 'Informacón de la categoria editada correctamente!',
            'status': 200,
            'data': resultado
        }

    else:
        data = {
            'message': 'ID de categoria invalido!',
            'status': 200
        }
    return make_response(jsonify(data))

# Ruta para ELIMINAR categorias
@app.route("/api/v1/categorias/<int:id>", methods=["DELETE"])
def eliminar_categoria(id):

    categoria = Categorias.query.get(id)

    if(categoria):
        db.session.delete(categoria)
        db.session.commit()

        data = {
            'message': 'Categoria eliminada!',
            'status': 200
        }
    else:
        data = {
            'message': 'ID de categoria invalido!',
            'status': 200
        }
    return make_response(jsonify(data))