from app import db
from sqlalchemy import Enum

# ----------------------------------------------------------------------- #
# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Productos(db.Model):
# Campos auto-generados:
    id                  = db.Column(db.Integer, primary_key=True)
# Entrada por campos ed productos:
    sku                 = db.Column(db.String(100), nullable=False, unique=True)
    nombre              = db.Column(db.String(100), nullable=False)
    desc                = db.Column(db.String(255), nullable=False)
    imagen              = db.Column(db.String(100), nullable=False)
    fichaTecnica        = db.Column(db.String(100), nullable=False)
    precio              = db.Column(db.Float, nullable=False)
    unidadMedida        = db.Column(Enum('KG','GR', 'LT', 'ML', 'CONTEO'), nullable=False)
    valorUnidad         = db.Column(db.Integer, nullable=False)
    #stock               = db.Column(db.Integer, nullable=False)
# Campos de fechas auto-generados:
    creado              = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)  # Fecha de creación de la instancia => Se creó una vez cuando se creó la instancia
    actualizado         = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False) # Fecha de la actualización de la instancia => cambia con cada actualización
# Relaciones
    categoria_id        = db.Column(db.Integer, db.ForeignKey("categorias.id"), nullable=False)
    categorias          = db.relationship("Categorias", back_populates='productos')

def __init__(self, sku, nombre, desc, imagen, fichaTecnica, precio, unidadMedida, valorUnidad, categoria_id):
    self.sku            = sku
    self.nombre         = nombre
    self.desc           = desc
    self.imagen         = imagen
    self.fichaTecnica   = fichaTecnica
    self.unidadMedida   = unidadMedida
    self.valorMedida    = valorUnidad
    self.precio         = precio
    self.categoria_id   = categoria_id