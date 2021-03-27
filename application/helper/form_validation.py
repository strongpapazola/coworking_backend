from application.config.config import *

class SetRules:
    def __init__(self, datajson = None):
        try:
            if datajson != None:
                self.data = datajson
            else:
                self.data = dict(request.json)
                if self.data == None:
                    abort(400, "JSON Required")
        except Exception as e:
            abort(400, "Invalid JSON : "+str(e)) # in case json is invalid
        self.key = []

    def struct(self, field, typedata, rules=False):
        try: #CHECKING TYPEDATA AND FORCE CHANGE TYPE
            if rules == False:
                if typedata == 'list':
                    self.data[field] = []
                elif typedata == 'dict':
                    self.data[field] = {}
                elif typedata == 'str':
                    self.data[field] = ''
                elif typedata == "int":
                    self.data[field] = 0
                elif typedata == "float":
                    self.data[field] = 0
                elif typedata == "bool":
                    self.data[field] = True
                else:
                    abort(400, 'struct typedata required')
            else:
                if typedata == 'list':
                    if isinstance(self.data[field], list) == False:
                        abort(400, 'typedata '+field+' must be list')
                    self.check(field, rules)
                elif typedata == 'dict':
                    if isinstance(self.data[field], dict) == False:
                        abort(400, 'typedata '+field+' must be dict')
                    self.check(field, rules)
                elif typedata == 'str':
                    if isinstance(self.data[field], str) == False:
                        abort(400, 'typedata '+field+' must be str')
                    self.check(field, rules)
                elif typedata == "int":
                    if isinstance(self.data[field], int) == False:
                        abort(400, 'typedata '+field+' must be int')
                    self.check(field, rules)
                elif typedata == "float":
                    if isinstance(self.data[field], float) == False:
                        abort(400, 'typedata '+field+' must be float')
                    self.check(field, rules)
                elif typedata == "bool":
                    if isinstance(self.data[field], bool) == False:
                        abort(400, 'typedata '+field+' must be bool')
                    self.check(field, rules)
                else:
                    abort(400, 'struct typedata required')
        except Exception as e:
            abort(400, "Error typedata : "+str(e))

        self.key.append(field)

    def optional(self, field, value=''):
        if self.data.get(field) is None:
            if value == 'list':
                self.data[field] = []
            elif value == 'dict':
                self.data[field] = {}
            elif value == 'str':
                self.data[field] = ''
            elif value == "int":
                self.data[field] = 0
            elif value == "float":
                self.data[field] = 0
            elif value == "bool":
                self.data[field] = True

    def validate(self, field, rules=''): #MARK IF THIS OLD CODE
        if "|" in rules:
            for i in rules.split('|'):
                self.check(field, i)
        else:
            self.check(field, rules)

    def check(self, field, rules): #field, rules
        def check_func(field, i):
            if i == "required":
                self.required(field)
            if "unique" in i: # unique[collection]
                i = i.split('[')[1].split(']')[0] #collection.key.value
                self.unique(i,field,self.data[field])
            if "optional" in i: #optional.type
                if "." in i:
                    i = i.split('.')
                    self.optional(field, i[1])
                else:
                    self.optional(field)
            if i == "valid_email":
                try:
                    (name, domain) = self.data[field].split('@')
                    (root, sub) = domain.split('.')
                except:
                    abort(400, "email not valid")

        if "|" in rules: #CHECKING RULES AND RUN RULE
            for i in rules.split('|'):
                check_func(field, i)
        else:
            check_func(field, rules)


    def set_key(self, field):
        self.key = field
    def check_key(self):
        return {key: self.data[key] for key_item in self.data for key in self.key if key == key_item}

    def validjson(self):
        try:
            self.data
        except Exception as e:
            abort(400, "Invalid JSON") # in case json is invalid

    def unique(self, collection, key, value):
        try:
            if [x for x in mongo.db[collection].find({key: value})] != []:
                abort(400, 'field %s must unique' % (key,))
        except Exception as e:
            abort(400, 'field %s must unique' % (key,))

    def required(self, field):
        if isinstance(field, tuple):
            for i in field:
                if self.data.get(i) is None:
                    abort(400, 'field %s required' % (i,))
        else:
            if self.data.get(field) is None:
                abort(400, 'field %s required' % (field,))
