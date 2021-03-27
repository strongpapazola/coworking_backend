from application.config.config import *

class MongoHelper:
    def __init__(self):
        self.null = 'nil'

    def loads(self, collection, method=False):
        if method == 'json':
            query = request.json
        elif method == 'args':
            query = request.args
        else:
            query = {}

        if query.get('_id'):
            query["_id"] = ObjectId(query['_id'])
            return mongo.db[collection].find(query)
        elif query != {}:
            return mongo.db[collection].find(query)
        else:
            return mongo.db[collection].find()

    def insert(self, collection, data):
        response = mongo.db[collection].insert_one(data)
        return {"id": str(response.inserted_id),"msg":"Data Inserted"}

    def update(self, collection, filterjson, data):
        response = mongo.db[collection].update_one(filterjson, data)
        return {"msg":"Data Updated" if response.modified_count > 0 else "Nothing was updated."}

    def filterfield(self, documents, fields=[], rule=False):
            if rule == True:
                result = []
                for data in documents:
                    data_result = {}
                    for field in fields:
                        for item in data:
                            if field == item:
                                data_result[field] = data[item]
                            pass
                    result.append(data_result)
                return result
            else:
                result = []
                for data in documents:
                    for i in fields:
                        data.pop(i, None)
                    result.append(data)
                return result

    def json(self, document): # Change ObjectId To STR
        result = []
        for data in [x for x in document]:
            if type(data['_id']) == ObjectId:
                data['_id'] = str(data['_id'])
                # print('ini objek')
            result.append(data)
        return result

    def paginate(self, collection, page_size, page_num, query={}):
            page_size = int(page_size)
            page_num = int(page_num)
            skips = page_size * (page_num - 1)
            result = mongo.db[collection].find(query).skip(skips).limit(page_size)
            count = result.count()
            data = [x for x in result]
            return {'data': self.json(data), 'page': page_num, 'offset': page_size, 'row_count': count}

