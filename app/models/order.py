from . import db

class Order(db.Model):
    __tablename__ = 'orders'
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'), nullable=False)
    table_id = db.Column(db.Integer, db.ForeignKey('tables.id'), nullable=False)
    finished = db.Column(db.Boolean, default=False)
        
    @property
    def employee_id(self):
        return self._employee_id
    
    @employee_id.setter
    def employee_id(self, employee_id):
        self._employee_id = employee_id
    
    @property
    def table_id(self):
        return self._table_id
    
    @table_id.setter
    def table_id(self, table_id):
        self._table_id = table_id
    
    @property
    def finished(self):
        return self._finished
    
    @finished.setter
    def finished(self, finished):
        self._finished = finished