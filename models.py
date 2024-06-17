from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

# Initialize the SQLAlchemy object
db = SQLAlchemy()

class Fund(db.Model):
    __tablename__ = 'funds'

    # Define the columns
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False) 
    manager_name = db.Column(db.String(100), nullable=False)  
    description = db.Column(db.String(200), nullable=True)  
    nav = db.Column(db.Float, nullable=False)  
    date_of_creation = db.Column(db.DateTime, default=datetime.utcnow) 
    performance = db.Column(db.Float, nullable=False)  

    
    def __init__(self, name, manager_name, description, nav, performance):
        self.name = name
        self.manager_name = manager_name
        self.description = description
        self.nav = nav
        self.performance = performance

    # Serialize the Fund object to a dictionary
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'manager_name': self.manager_name,
            'description': self.description,
            'nav': self.nav,
            'date_of_creation': self.date_of_creation.strftime('%Y-%m-%d %H:%M:%S'), 
            'performance': self.performance,
        }
