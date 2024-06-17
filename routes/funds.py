from flask import Blueprint, request, jsonify, abort
from models import db, Fund

# Create a blueprint for the funds routes
funds = Blueprint('funds', __name__)

# Get all funds
@funds.route('/', methods=['GET'])
def get_all_funds():
    all_funds = Fund.query.all()  
    return jsonify([fund.serialize() for fund in all_funds]), 200  

# Create a new fund
@funds.route('/', methods=['POST'])
def create_fund():
    data = request.get_json()  
    if not data:
        abort(400, description="No input data provided")  
    
    name = data.get('name')
    manager_name = data.get('manager_name')
    description = data.get('description')
    nav = data.get('nav')
    performance = data.get('performance')

    if not name or not manager_name or nav is None or performance is None:
        abort(400, description="Missing required fields: name, manager_name, nav, performance")

    new_fund = Fund(
        name=name,
        manager_name=manager_name,
        description=description,
        nav=nav,
        performance=performance
    )
    db.session.add(new_fund)  
    db.session.commit()  
    return jsonify(new_fund.serialize()), 201  


@funds.route('/<int:id>', methods=['GET'])
def get_fund(id):
    fund = db.session.get(Fund, id)  
    if fund is None:
        abort(404) 
    return jsonify(fund.serialize()), 200  


@funds.route('/<int:id>', methods=['PUT'])
def update_fund_performance(id):
    data = request.get_json()  
    if not data:
        abort(400, description="No input data provided")  

    performance = data.get('performance')  # Get the performance field
    if performance is None:
        abort(400, description="Missing required field: performance")  # Abort if performance is not provided

    fund = db.session.get(Fund, id)  # Get the fund by ID
    if fund is None:
        abort(404)  # Abort if the fund is not found
    fund.performance = performance  # Update the performance
    db.session.commit()  
    return jsonify(fund.serialize()), 200  


@funds.route('/<int:id>', methods=['DELETE'])
def delete_fund(id):
    fund = db.session.get(Fund, id)  # Get the fund by ID
    if fund is None:
        abort(404)  # Abort if the fund is not found
    db.session.delete(fund)  # Delete the fund from the session
    db.session.commit()  # Commit the session to delete the fund
    return jsonify({'message': 'Fund deleted successfully'}), 200  
