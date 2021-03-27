from application.config.config import *

def model_insert_berita(data):
	try:
		schema = {
			"judul" : data['judul'],
			"isi" : data['isi'],
			"kategori": data['kategori'],
			"updated" : [],
			"foto" : data['foto'],
			"sumber_foto" : data['sumber_foto'],
			"jumlah_pembaca" : data["jumlah_pembaca"],
			"waktu_baca" : data["waktu_baca"],
			"is_aktif" : 2,
			"komentar": []
		}
	except Exception as e:
		abort(400)
		