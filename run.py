from app import create_app, db
from app.models import Bike

app = create_app()

def add_sample_data():
    with app.app_context():
        # Добавление тестовых данных
        if Bike.query.count() == 0:  # Проверяем, есть ли уже велосипеды
            sample_bikes = [
                Bike(name="Горный велосипед 1", type="горный", price_per_day=500, status="available"),
                Bike(name="Дорожный велосипед 1", type="дорожный", price_per_day=300, status="available"),
                Bike(name="Горный велосипед 2", type="горный", price_per_day=700, status="unavailable"),
            ]
            db.session.add_all(sample_bikes)
            db.session.commit()
            print("Тестовые данные добавлены.")

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # Создание таблиц в базе данных
        #add_sample_data()  # Добавление тестовых данных
    app.run(debug=True)
