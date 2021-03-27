from application.config.config import *

def handle_error(app):
    @app.errorhandler(400)
    def bad_request(e):
        return make_response(jsonify(({
            'status_code': 400,
            'msg': str(e.description),
            'data': None
        }))), 400

    @app.errorhandler(403)
    def not_found(e):
        return make_response(jsonify(({
            'status_code': 403,
            'msg': str(e.description),
            'data': None
        }))), 403

    @app.errorhandler(404)
    def not_found(e):
        return make_response(jsonify(({
            'status_code': 404,
            'msg': str(e.description),
            'data': None
        }))), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return make_response(jsonify(({
            'status_code': 405,
            'msg': str(e.description),
            'data': None
        }))), 405

    @app.errorhandler(500)
    def internal_server_error(e):
        return make_response(jsonify(({
            'status_code': 500,
            'msg': str(e.description),
            'data': None
        }))), 500
    return app
