from flask import Blueprint, render_template, jsonify, request, redirect, url_for, flash, request_started
from app.models import db, Bike#,#User
from flask_login import login_user, logout_user, login_required
from app.models import User
bp = Blueprint('main', __name__)
#api_bp = Blueprint('api', __name__, url_prefix='/api')
@bp.route('/')
def index():
    bikes = Bike.query.all()
    return render_template('index.html', bikes=bikes)

# @bp.route('/api/rent/<int:bike_id>')
# def bike_details(bike_id):
#     bike = Bike.query.get_or_404(bike_id)
#     return render_template('bike_details.html', bike=bike)
@bp.route('/rent')
def bike_list():
    bikes = Bike.query.all()  # Получить все велосипеды из базы данных
    return render_template('bikes.html', bikes=bikes)

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        # Проверка существующего пользователя
        if User.query.filter_by(email=email).first():
            flash('Email already registered.')
            return redirect(url_for('main.register'))

        new_user = User(username=username, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        login_user(new_user)
        return redirect(url_for('main.index'))

    return render_template('register.html')

# Вход
@bp.route('/login', methods=['GET', 'POST', 'DELETE', 'ADD'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password.')

    return render_template('login.html')

# Выход
@bp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))