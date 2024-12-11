from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .employee import Employee
from .menu import Menu
from .menu_item import MenuItem
from .menu_item_type import MenuItemType
from .table import Table
from .order import Order