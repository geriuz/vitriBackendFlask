from config import Config
from app import app, db

def create_tables():
    print("Creando tablas de la base de datos...")
    db.create_all()
    print("Proceso terminado!")

if __name__ == '__main__':
    #app.run(debug=Config.DEBUG)
    app.run(debug=True, port=8087)