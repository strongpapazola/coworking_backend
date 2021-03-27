from application.config.autoload import *

def json_response(dictionary, code=None):
    if code:
        return make_response(jsonify({"data":dictionary,"status_code":code}))
    else:
        return make_response(jsonify(dictionary))
