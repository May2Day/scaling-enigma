from flask import Flask, render_template, redirect, url_for, request, flash
from flask_sqlalchemy import SQLAlchemy
from app.models import db, login_manager  # Импортируем db отсюда
from .routes import bp
from .api_routes import api_bp
from flask_login import LoginManager
from flask_migrate import Migrate


# login_manager = LoginManager()
# login_manager.login_view = 'login'
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_super_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    migrate.init_app(app, db)  # Подключение Flask-Migrate
    
    login_manager.init_app(app)

    from .routes import bp as routes_bp
    app.register_blueprint(routes_bp)

    # Подключение API маршрутов

    app.register_blueprint(api_bp)

    return app
