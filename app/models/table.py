from . import db

class Table(db.Model):
    __tablename__ = 'tables'
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, nullable=False, unique=True)
    capacity = db.Column(db.Integer, nullable=False)
    
    @property
    def number(self):
        return self._number
    
    @number.setter
    def number(self, number):
        self._number = number
        
    @property
    def capacity(self):
        return self._capacity
    
    @capacity.setter
    def capacity(self, capacity):
        self._capacity = capacity