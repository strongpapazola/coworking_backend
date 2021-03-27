from application.config.config import *
from application.helper import *

coworking = Blueprint('coworking', __name__, static_folder = 'application/upload/foto_coworking', static_url_path="/media")

@coworking.route("/get_coworking", methods=["GET"])
def get_coworking():
    db = MongoHelper()
    if request.args:
        dataload = db.loads('coworking', 'args')
    else:
        dataload = db.loads('coworking')
        dataload = db.filterfield(dataload, ['_id','nama','lokasi'], True)
    return json_response(db.json(dataload), 200)

@coworking.route("/insert_coworking", methods=["POST"])
def insert_coworking():
    # user = JwtAuth().role("USER")
    schema = SetRules()
    schema.struct('nama','str',"required")
    schema.struct('lokasi','dict',"required")
    schema.struct('operasional','list',"required")
    schema.struct('harga','str',"required")
    schema.struct('foto','str')
    schema.struct('fasilitas','list')
    schema.struct('membership','list')
    schema.struct('reviews','list')
    schema.data['is_aktif'] = 2
    data = schema.check_key()
    lokasi = SetRules(data['lokasi'])
    lokasi.struct('kabupaten','str','required')
    lokasi.struct('kecamatan','str','required')
    insert = MongoHelper().insert('coworking', data)
    return json_response(insert, 200)

@coworking.route("/update_coworking", methods=["PUT"])
def update_coworking():
    user = JwtAuth().role("USER",show=True)
    schema = SetRules()
    schema.validate('_id',"required")
    schema.validate('judul',"required")
    schema.validate('isi',"required")
    schema.validate('waktu_baca',"required")
    schema.optional(('foto', 'sumber_foto','jumlah_pembaca'))
    schema.data['kategori'] = []
    schema.data['komentar'] = []
    schema.data['is_aktif'] = 1
    schema.set_key(("_id","judul","isi","kategori","foto","sumber_foto","jumlah_baca","waktu_baca","is_aktif","komentar"))
    data = schema.check_key()
    data['_id']
    data = {"$set":data}
    data['$push'] = {
            "updated": {
                "id_user": user.data['user_id'],
                "updated_at": Global_var.Time('now')
            }
        }
    # update = MongoHelper().update('coworking', {"_id": ObjectId(schema.check_key()["_id"])}, data)
    return json_response(data, 200)

# {
#     "judul" : "Judul coworking",
#     "isi" : "Isi coworking",
#     "kategori": [],
#     "updated" : [
#         {
#             "id_user":"09827349yfg2jd9m8024md34",
#             "updated_at": "82736948763"
#         }
#     ],
#     "foto" : "coworking_29830472837.png",
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
#     "foto" : "coworking_29830472837.png",
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
#             "id_coworking": "lf7834hof8hsiduhfljkshd",
#             "is_aktif": 1, //matiin akun
#             "created_at": 82736948762
#         }
#     ]
# }

