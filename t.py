from app import create_app, db
from app.models import Bike

app = create_app()
with app.app_context():
    bike1 = Bike(name="Mountain Bike 1", type="Mountain", price_per_day = 200, status = 'aviable', image_url="/static/images/bike1.jpg")
    bike2 = Bike(name="Road Bike 1", type="Road", price_per_day = 100,status ='aviable', image_url="/static/images/bike2.jpg")
    bike3 = Bike(name="Mountain Bike 3", type="Mountain", price_per_day = 300,status ='aviable', image_url="/static/images/bike3.jpg")
    db.session.add_all([bike1, bike2, bike3])
    db.session.commit()
    print("Данные добавлены.")