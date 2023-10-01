import os
from flask import Flask, jsonify, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, Bird

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate = Migrate(app, db)
    api = Api(app)

    class Birds(Resource):
        def get(self):
            birds = [bird.to_dict() for bird in Bird.query.all()]
            return make_response(jsonify(birds), 200)

    api.add_resource(Birds, '/birds')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(port=5001)
