from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import LoginManager,UserMixin


db = SQLAlchemy()
login_manager = LoginManager()

class Bike(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(50), nullable=False)  # Тип: "горный", "дорожный"
    price_per_day = db.Column(db.Float, nullable=False)  # Цена за день
    status = db.Column(db.String(20), nullable=False, default="available")  # Статус: "available", "unavailable"
    image_url = db.Column(db.String(200), nullable=True)
    rented_by = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=True)  # Связь с таблицей User
    def rent(self):
        """Арендовать велосипед (меняет статус на 'unavailable')."""
        if self.status == "available":
            self.status = "unavailable"
            return True
        return False
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(256), nullable=False)

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return f"<User {self.username}>"

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))