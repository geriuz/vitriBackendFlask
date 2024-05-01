from app import db
import datetime

# ----------------------------------------------------------------------- #

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class Categorias(db.Model):
# Campos auto-generados:
    id                  = db.Column(db.Integer, primary_key=True)
# Entrada por campos ed productos:
    nombre              = db.Column(db.String(100), nullable=False)
    desc                = db.Column(db.String(255), nullable=False)

# Campos de fechas auto-generados:
    creado              = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), nullable=False)  # Fecha de creación de la instancia => Se creó una vez cuando se creó la instancia
    actualizado         = db.Column(db.DateTime(timezone=True), default=db.func.current_timestamp(), onupdate=db.func.current_timestamp(), nullable=False) # Fecha de la actualización de la instancia => cambia con cada actualización
# Relaciones
    productos = db.relationship("Productos", back_populates='categorias')


def __init__(self, nombre, desc):
    self.nombre         = nombre
    self.desc           = desc
