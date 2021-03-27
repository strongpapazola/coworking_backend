from application.config.config import *
from application.helper import *
from application.controller.komentar.models import *


komentar = Blueprint('komentar', __name__, static_folder = 'application/upload/foto_komentar', static_url_path="/media")

@komentar.route("/get_komentar", methods=["GET"])
def get_komentar():
    db = MongoHelper()
    if request.args:
        dataload = db.loads('komentar', dict(request.args))
    else:
        dataload = db.loads('komentar')
        dataload = db.filterfield(dataload, ['_id','judul'], True)
    return json_response(db.json(dataload), 200)

@komentar.route("/insert_komentar", methods=["POST"])
def insert_komentar():
    # user = JwtAuth(request.headers.get("Authorization"))
    # user.validate()
    # return json_response(user.data)

    schema = SetRules(dict(request.json))
    schema.validate()
    schema.required(('judul','isi','waktu_baca'))
    schema.optional(('foto', 'sumber_foto','jumlah_pembaca'))
    schema.optional('kategori', 'list')
    schema.optional('komentar', 'list')
    schema.data['updated'] = {
        "id_user": "user.data['id_user_fromjwt']",
        "updated_at": str(time.time()).split('.')[0]
    }
    schema.data['is_aktif'] = 2
    insert = MongoHelper().insert('komentar', schema.data)
    return json_response(insert, 200)

@komentar.route("/update_komentar", methods=["POST"])
def update_komentar():
    # user = JwtAuth(request.headers.get("Authorization"))
    # user.validate()
    # return json_response(user.data)

    schema = SetRules(dict(request.json))
    schema.validate()
    schema.required(('judul','isi','waktu_baca'))
    schema.optional(('foto', 'sumber_foto','jumlah_pembaca'))
    schema.optional('kategori', 'list')
    schema.optional('komentar', 'list')
    schema.data['updated'] = {
        "id_user": "user.data['id_user_fromjwt']",
        "updated_at": str(time.time()).split('.')[0]
    }
    schema.data['is_aktif'] = 2
    insert = MongoHelper().insert('komentar', schema.data)
    return json_response(insert, 200)


@komentar.route('/login', methods=["POST"])
def login():
    token = jwt.encode({'user' : "strongpapazola", 'exp' : datetime.datetime.utcnow() + datetime.timedelta(minutes=15)}, current_app.config['SECRET_KEY'])
    return json_response({'token' : token.decode('UTF-8')}, 200)


# {
#     "judul" : "Judul Berita",
#     "isi" : "Isi komentar",
#     "kategori": [],
#     "updated" : [
#         {
#             "id_user":"09827349yfg2jd9m8024md34",
#             "updated_at": "82736948763"
#         }
#     ],
#     "foto" : "komentar_29830472837.png",
#     "sumber_foto" : "https://example.com/image.png",
#     "jumlah_pembaca" : 12,
#     "waktu_baca" : 5,
#     "is_aktif" : 1,
#     "komentar": [
#         {
#             "id_user": 
#             "komentar" : "comment",
#             "created_at": 82736948762,
#             "id_user": "09827349yh92jd9m8024md34"
#         }
#     ]
# }


# //kategori
# {
#     "_id": "987h0887onas87dn78s",
#     "nama": "AI",
#     "foto" : "komentar_29830472837.png",
#     "is_aktif": 1
# }

# // user :
# {
#     "_id": "09827349yh92jd9m8024md34",
#     "email": "strongpapazola@gmai.com", //wajib
#     "password": "o97d2ho3hdpo72no3duwefsd", //wajib
#     "nama": "strongpapazola",
#     "phone": "+62822123123123",
#     "jenis_kelamin": 1, //1 = laki, 2 = pr
#     "foto": "users_29830472837.png",
#     "alamat": "jalan asdasd",
#     "registered_at": 82736948762,
#     "is_register": 1, //1 sudah, 2 belum
#     "is_aktif": 1, //matiin akun
#     "forget_token": "032uyihe2duinoulwjenjd",
#     "token_fcm": null,
#     "roles": [1,2,3], //1 = customer, 2 = penulis, 3 = admin
#     "bookmark": [
#         {
#             "id_komentar": "lf7834hof8hsiduhfljkshd",
#             "is_aktif": 1, //matiin akun
#             "created_at": 82736948762
#         }
#     ]
# }

