from application.config.config import *

class Global_var:
    def Time(str_get):
        if str_get == 'now':
            return int(str(time.time()).split('.')[0])

    def Hash(str_get):
        return hashlib.sha256(str_get.encode()).hexdigest()