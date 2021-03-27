from application.config.config import *
from application.helper import *
from application.controller.users.models import *


users = Blueprint('users', __name__, static_folder = 'application/upload/foto_users', static_url_path="/media")

@users.route("/register", methods=["POST"])
def insert_users():
    schema = SetRules()
    schema.struct("email","str","required|unique[users]|valid_email")
    schema.struct("password","str","required")
    schema.struct("name","str","required")
    schema.struct("phone","str","optional")
    schema.struct("jenis_kelamin","str","optional")
    schema.struct("foto","str","optional")
    schema.struct("alamat","str","optional")
    schema.struct("registered_at","int")
    schema.struct("is_register","int")
    schema.struct("is_aktif","int")
    schema.struct("token_fcm","str")
    schema.struct("roles","list")
    schema.struct("bookmark","list")
    rawdata = schema.data
    rawdata['password'] = hashlib.sha256(rawdata['password'].encode()).hexdigest()
    rawdata["registered_at"] = Global_var.Time('now')
    rawdata["is_register"] = 1 #2 = belum verify
    rawdata["is_aktif"] = 1 #1 = Akun aktif
    rawdata["token_fcm"] = hashlib.sha256('{} {} {}'.format('token_fcm', rawdata['email'], str(Global_var.Time('now'))).encode()).hexdigest()
    rawdata["roles"] = ['USER'] #USER, PENULIS, ADMIN
    rawdata["bookmark"] = []
    data = schema.check_key()
    insert = MongoHelper().insert('users', data)
    return json_response(insert, 200)

@users.route('/login', methods=["POST"])
def login():
    schema = SetRules()
    schema.struct('email',"str",'valid_email|required')
    schema.struct('password',"str",'required')
    data = schema.check_key()
    db = MongoHelper()
    user = [x for x in db.loads("users",{"email": data['email']})]
    if user != []:
        if Global_var.Hash(data['password']) == user[0]['password']:
            user_data = {'user_id' : str(user[0]['_id']), "roles": user[0]['roles'],'exp' : datetime.datetime.utcnow() + datetime.timedelta(hours=3)}
            token = jwt.encode(user_data, current_app.config['SECRET_KEY']).decode('utf-8')
            return json_response(token,200)
        else:
            abort(403, "wrong password")
    else:
        abort(403, "email not found")


