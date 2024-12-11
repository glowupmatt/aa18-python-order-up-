from . import db

class MenuItemType(db.Model):
    __tablename__ = 'menu_item_types'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    
    items = db.relationship('MenuItem', back_populates='menu_type')
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name