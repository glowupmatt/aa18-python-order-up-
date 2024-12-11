from . import db

class MenuItem(db.Model):
    __tablename__ = 'menu_items'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    price = db.Column(db.Float, nullable=False)
    menu_id = db.Column(db.Integer, db.ForeignKey('menus.id'), nullable=False)
    menu_type_id = db.Column(db.Integer, db.ForeignKey('menu_item_types.id'), nullable=False)
    
    menu = db.relationship('Menu', back_populates='items')
    menu_type = db.relationship('MenuItemType', back_populates='items')
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name
        
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, price):
        self._price = price