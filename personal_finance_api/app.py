from flask import Flask
from models.models import db
from config.config import Config
<<<<<<< HEAD
from routes.routes_income import routes_income
from routes.routes_expense import routes_expense

=======
from routes.routes import routes
>>>>>>> 714a412c0360bc3c07887fdb37b6f59b3530486f

app = Flask(__name__)

app.config.from_object(Config)

<<<<<<< HEAD
# registramos las rutas que vamos a utilizar
app.register_blueprint(routes_income, url_prefix='/incomes')
app.register_blueprint(routes_expense, url_prefix='/expenses')
=======
app.register_blueprint(routes)
>>>>>>> 714a412c0360bc3c07887fdb37b6f59b3530486f

# Inicializar la base de datos con la aplicación
db.init_app(app)

# Crear las tablas en la base de datos
with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)