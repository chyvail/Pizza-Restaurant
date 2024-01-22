
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from http import HTTPStatus
from flask_cors import CORS

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

CORS(app)

api = Api(app)

class Home(Resource):
    
    def get(self):
         
        response_dict = {
            "Message": "Pizza Resturant API",
        }
        
        response = make_response(
            response_dict,
            HTTPStatus.OK,
        )

        return response

api.add_resource(Home, '/')

class Restaurants(Resource):
    def get(self):
        restaurant_dict = [r.to_dict() for r in Restaurant.query.all()]
        return make_response(jsonify(restaurant_dict), HTTPStatus.OK)
    
    def post(self):
        data = request.get_json()
        new_restaurant = Restaurant(
            name = data['name'],
            address = data['address']
        )
        db.session.add(new_restaurant)
        db.session.commit()
        return make_response(jsonify(new_restaurant.to_dict()), HTTPStatus.CREATED)
    
api.add_resource(Restaurants, '/restaurants')

class RestaurantById(Resource):
    def get(self, id):
        restaurant_dict = Restaurant.query.filter_by(id=id).first()
        if restaurant_dict:
            return make_response(jsonify(restaurant_dict.to_dict()), HTTPStatus.OK)
        else:
            return make_response({"error":"Restaurant not found"}, HTTPStatus.NOT_FOUND)
        
    def delete(self, id):
        restaurant_dict = Restaurant.query.filter_by(id=id).first()
        if restaurant_dict:
            db.session.delete(restaurant_dict)
            db.session.commit()
            return make_response({}, HTTPStatus.NO_CONTENT)
        else:
            return make_response({"error":"Restaurant not found"}, HTTPStatus.NOT_FOUND)

api.add_resource(RestaurantById, '/restaurants/<int:id>')

class Pizzas(Resource):
    def get(self):
        pizzas_dict = [p.to_dict() for p in Pizza.query.all()]
        return make_response(jsonify(pizzas_dict), HTTPStatus.OK)

api.add_resource(Pizzas, '/pizzas')

class RestaurantPizzas(Resource):
    def get(self):
        restaurant_pizzas_dict = [rp.to_dict() for rp in RestaurantPizza.query.all()]
        return make_response(jsonify(restaurant_pizzas_dict), HTTPStatus.OK)
    
    def post(self):
        data = request.get_json()
        new_restaurant_pizza = RestaurantPizza(
            restaurant_id = data['restaurant_id'],
            pizza_id = data['pizza_id'],
            price = data['price']
        )
        db.session.add(new_restaurant_pizza)
        db.session.commit()
        pizza = Pizza.query.filter_by(id=data['pizza_id']).first()
        return make_response(pizza.to_dict(), HTTPStatus.CREATED)

api.add_resource(RestaurantPizzas, '/restaurant_pizzas')


if __name__ == '__main__':
    app.run(port=5555,debug=True)