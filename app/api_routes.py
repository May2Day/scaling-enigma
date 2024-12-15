import json
from flask import Blueprint, Response, request
from .models import db, Bike
from flask_login import current_user

#api_bp = Blueprint("api", __name__, url_prefix="/api")
api_bp = Blueprint('api', __name__)
def create_json_response(data, status=200):
    #"""
    #Создает JSON-ответ с поддержкой корректного отображения кириллицы.
    #"""
    
    return Response(
        json.dumps(data, ensure_ascii=False),  # Отключаем Unicode-экранирование
        content_type="application/json",
        status=status
    )

@api_bp.route('/api/rent/<int:bike_id>', methods=['POST', 'GET', 'PUT', 'DELETE'])
def rent_bike(bike_id):
    #"""
    #API для аренды велосипеда.
    #"""
    bike = Bike.query.get(bike_id)
    if not bike:
        return create_json_response({"error": "Bike not found"}, 404)

    if bike.status == "unavailable":
        return create_json_response({"error": "Bike is already rented"}, 400)
    
    if not current_user.is_authenticated:
        return jsonify({"error": "User must be logged in"}), 401

    # Помечаем велосипед как арендованный
    bike.rent()
    bike.status = 'Unavaible'
    db.session.commit()
    response = {"success": f"Bike {bike.name} rent done"}
    return create_json_response(response, 200)
