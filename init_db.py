from app import create_app, db
from app.models import Bike  # Импортируйте ваши модели

app = create_app()

with app.app_context():
    db.create_all()  # Создаёт таблицы в базе данных
    print("База данных инициализирована.")
