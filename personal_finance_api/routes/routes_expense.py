from flask import Blueprint, jsonify, request
from models.models import db, Expense

routes_expense = Blueprint('routes_expense', __name__)

# metodo GET para devolver la lista de gastos que se registraron
@routes_expense.route('/list', methods = ['GET'])
def find_all():
    
    expenses = Expense.query.all()
    
    if not expenses:
        return jsonify({'message': 'No hay registro de gastos'}), 200
    
    result = []
    for expense in expenses:
        expense_data = {
            'id': expense.id,
            'description': expense.description,
            'amount': expense.amount,
            'date': expense.date.strftime('%Y-%m-%d')
        }
        result.append(expense_data)
        
    return jsonify(result), 200

# metodo POST para registrar los gastos que se van haciendo
@routes_expense.route('/create', methods = ['POST'])
def create_expense():
    
    data = request.get_json()
    new_expense = Expense(
        description = data['description'],
        amount = data['amount'],
        date = data['date']
    )
    
    db.session.add(new_expense)
    db.session.commit()
    
    expense_data = {
        'id': new_expense.id,
        'description': new_expense.description,
        'amount': new_expense.amount,
        'date': new_expense.date.strftime('%Y-%m-%d')
    }
    
    return jsonify(expense_data), 200

# metodo PATCH para modificar valores que se necesite dep expense
@routes_expense.route('/update/<int:expense_id>', methods = ['PATCH'])
def update_expense(expense_id):
    
    expense = Expense.query.get(expense_id)
    
    if not expense:
        return jsonify({'message': 'Gasto no encontrado'}), 404
    
    data = request.get_json()
    
    if not any(field in data for field in ['description', 'amount', 'date']):
        return jsonify({'message': 'Los datos son requeridos'}), 400
    
    if 'description' in data:
        expense.description = data['description']
    if 'amount' in data:
        expense.amount = data['amount']
    if 'date' in data:
        expense.date = data['date']
        
    db.session.commit()
    
    expense_data = {
        'id': expense.id,
        'description': expense.description,
        'amount': expense.amount,
        'date': expense.date.strftime('%Y-%m-%d')
    }
    
    return jsonify(expense_data), 200

# metodo DELETE para eliminar un expense por su id
@routes_expense.route('/delete/<int:expense_id>', methods = ['DELETE'])
def delete_expense(expense_id):
    
    expense = Expense.query.get(expense_id)
    
    if not expense:
        return jsonify({'message': 'Gasto no encontrado'}), 404
    
    db.session.delete(expense)
    db.session.commit()
    
    return jsonify({'message': 'Gasto eliminado correctamente'})