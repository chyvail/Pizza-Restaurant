
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from http import HTTPStatus

from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact = False

migrate = Migrate(app, db)

db.init_app(app)

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

if __name__ == '__main__':
    app.run(port=5555,debug=True)