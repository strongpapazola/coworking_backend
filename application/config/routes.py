from application.config.config import *
from application.helper import * #error root
from application.controller.coworking.controller import coworking
from application.controller.users.controller import users

app = Flask(__name__)
app = config_app(app)
app = config_jwt(app)
app = handle_error(app)

app.register_blueprint(coworking,url_prefix='/coworking')
app.register_blueprint(users,url_prefix='/users')

