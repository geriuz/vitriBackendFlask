from datetime import date
from app import app
from flask_marshmallow import Marshmallow

from app.models.productos import Productos

ma = Marshmallow(app)

class ProductoSchema(ma.SQLAlchemySchema):
    class Meta():
        model           = Productos
        fields = ('id', 'sku', 'nombre', 'desc', 'imagen', 'fichaTecnica', 'precio', 'unidadMedida', 'valorUnidad', 'categoria_id')

producto_schema = ProductoSchema()
productos_schema = ProductoSchema(many=True)

