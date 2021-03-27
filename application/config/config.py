from application.config.autoload import *

mongo = PyMongo()

def config_app(app):
    app.config['MONGO_URI'] = 'mongodb://coworking:admin@117.53.44.15:30001,117.53.44.15:30002,117.53.44.15:30003/coworking?replicaSet=my-mongo-set'
    mongo.init_app(app)
    return app

def config_jwt(app):
    app.config['SECRET_KEY'] = 'thisisthesecretkey'
    return app
