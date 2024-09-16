from flask import Blueprint, request, jsonify
from models.models import db, Income

routes_income = Blueprint('routes_income', __name__)

# metodo GET que devuelve la lista de Incomes
@routes_income.route('/list', methods = ['GET'])
def find_all():
    
    incomes = Income.query.all()
    
    # si esta vacia la lista, devuelve un msj
    if not incomes:
        return jsonify({"message": "No se han registrado ingresos"}), 200
    
    # creamos un diccionario con el formato de income
    result = []
    for income in incomes:
        income_data = {
            'id': income.id,
            'description': income.description,
            'amount': income.amount,
            'date': income.date.strftime('%Y-%m-%d')
        }
        result.append(income_data)  
    
    return jsonify(result), 200
    
# metodo POST para la creacion de incomes
@routes_income.route('/create', methods=['POST'])
def create_income():
    
    # obtenemos los datos del request y a partir de esos datos, creamos un nuevo income
    data = request.get_json()
    new_income = Income(
        description = data['description'],
        amount = data['amount'],
        date = data['date']
    )
    
    db.session.add(new_income)
    db.session.commit()
    
    income_data = {
        'id': new_income.id,
        'description': new_income.description,
        'amount': new_income.amount,
        'date': new_income.dat  # Convertir la fecha a string
    }
    
    return jsonify(income_data), 200

# metodo PATCH para modificar datos del income
@routes_income.route('/update/<int:income_id>', methods=['PATCH'])
def update_income(income_id):
    
    income = Income.query.get(income_id)
    
    # si no existe el income que le pasamos por URL, avisamos con un mensaje
    if not income:
        return jsonify({"message": "Ingreso no encontrado"}), 404
    
    data = request.get_json()
    
    # valida si al menos uno de los campos está presente
    if not any(field in data for field in ['description', 'amount', 'date']):
        return jsonify({'message': 'Los datos son requeridos'}), 400
    
    # validamos si vienen datos del request y se los mapeamos al objeto que obtenemos del ID
    if 'description' in data:
        income.description = data['description']
    if 'amount' in data:
        income.amount = data['amount']
    if 'date' in data:
        income.date = data['date']
        
    db.session.commit()
    
    income_date = {
        'id': income.id,
        'description': income.description,
        'amount': income.amount,
        'date': income.date.strftime('%Y-%m-%d')  # Convertir la fecha a string
    }

    return jsonify(income_date), 200

# metodo DELETE, para eliminar un income por su id
@routes_income.route('/delete/<int:income_id>', methods = ['DELETE'])
def delete_income(income_id):
    
    income = Income.query.get(income_id)
    
    if not income:
        return jsonify({"message": "Ingreso no encontrado"}), 404
    
    db.session.delete(income)
    db.session.commit()
    
    return jsonify({'message': 'Ingreso eliminado correctamente'}), 200
    
    

