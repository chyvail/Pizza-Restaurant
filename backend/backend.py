
from flask import Flask, request, make_response, jsonify
from flask_migrate import Migrate
from flask_restful import Api, Resource
from http import HTTPStatus

from models import db

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

if __name__ == '__main__':
    app.run(port=5555,debug=True)