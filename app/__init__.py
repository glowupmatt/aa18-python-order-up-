from flask import Flask
from .config import Configuration
from .models import db, Employee, Menu, MenuItem, MenuItemType
from .routes.orders import bp as orders_bp
from .routes.session import bp as session_bp
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Configuration)
app.register_blueprint(orders_bp)
app.register_blueprint(session_bp)

login = LoginManager(app)
login.login_view = "session.login"
db.init_app(app)

@login.user_loader
def load_user(id):
    return Employee.query.get(int(id))


# Ensure the app context is pushed when running the app
with app.app_context():
    db.create_all()