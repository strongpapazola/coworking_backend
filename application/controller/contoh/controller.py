from application.config.config import *
from application.config.autoload import *
from application.helper import *


berita = Blueprint('berita', __name__, static_folder = 'application/upload/foto_berita', static_url_path="/media")

@berita.route("/mongodb", methods=["GET","POST"])
def home_page():
    return json_response(mongo_json(mongo_loads('berita')), 200)

# {
#     "_id": "lf7834hof8hsiduhfljkshd",
#     "judul" : "Judul Berita",
#     "isi" : "Isi berita",
#     "kategori": ["987h0887onas87dn78s"],
#     "updated" : [
#         {
#             "id_user":"09827349yh92jd9m8024md34",
#             "updated_at": "82736948762"
#         },
#         {
#             "id_user":"09827349yfg2jd9m8024md34",
#             "updated_at": "82736948763"
#         }
#     ],
#     "foto" : "berita_29830472837.png",
#     "sumber_foto" : "https://example.com/image.png",
#     "jumlah_pembaca" : 12,
#     "waktu_baca" : 5, //menit
#     "is_aktif" : 1,
#     "komentar": [
#         {
#             "komentar" : "comment",
#             "created_at": 82736948762,
#             "id_user": "09827349yh92jd9m8024md34"
#         }
#     ]
# }
