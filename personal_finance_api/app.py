from flask import Flask
from models.models import db
from config.config import Config
from routes.routes import routes

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(routes)

# Inicializar la base de datos con la aplicación
db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)