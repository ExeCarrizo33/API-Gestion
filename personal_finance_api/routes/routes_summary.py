from flask import Blueprint, jsonify, request
from models.models import db, Expense, Income

summary = Blueprint('summary', __name__)

@summary.route('/get', methods = ['GET'])
def get_summary():
    
    try:
        # Obtener el total de ingresos
        total_income = db.session.query(db.func.sum(Income.amount)).scalar() or 0

        # Obtener el total de gastos
        total_expense = db.session.query(db.func.sum(Expense.amount)).scalar() or 0

        # Calcular el saldo
        balance = total_income - total_expense

        # Crear el resumen
        summary = {
            'total_income': total_income,
            'total_expense': total_expense,
            'balance': balance
        }

        return jsonify(summary), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
