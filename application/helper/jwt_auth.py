from application.config.config import *

# def token_required(f):
#     @wraps(f)
#     def decorated(*args, **kwargs):
#         token = request.headers.get('Authorization')
#         if not token:
#             abort(403, "Token Missing")
#         # try:
#         print(jwt.decode(token, current_app.config['SECRET_KEY']))
#         # except:
#         #     return jsonify({'message' : 'Token is invalid!'}), 403
#         return f(*args, **kwargs)
#     return decorated

class JwtAuth:
    def __init__(self):
        self.token = request.headers.get("Authorization")
        self.data = {}
        if not self.token:
            abort(403, "Token Missing")
        try:
            self.data = jwt.decode(self.token, current_app.config['SECRET_KEY'])
        except:
            abort(403, 'Token is invalid!')

    # def validate(self):
        # if not self.token:
        #     abort(403, "Token Missing")
        # try:
        #     self.data = jwt.decode(self.token, current_app.config['SECRET_KEY'])
        # except:
        #     abort(403, 'Token is invalid!')

    def role(self, role, show=True):
        if show == True:
            if role not in self.data['roles']:
                abort(403, "Permission Denied")
        else:
            if role in self.data['roles']:
                abort(403, "Permission Denied")
