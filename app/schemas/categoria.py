from datetime import date

from app import app
from flask_marshmallow import Marshmallow

from app.models.categorias import Categorias

ma = Marshmallow(app)

class CategoriaSchema(ma.SQLAlchemySchema):
    class Meta():
        model = Categorias
        fields = ('id', 'nombre', 'desc')

categoria_schema = CategoriaSchema()
categorias_schema = CategoriaSchema(many=True)