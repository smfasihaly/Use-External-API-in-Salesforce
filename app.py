from flask import Flask, jsonify,request
import json
app = Flask(__name__)

class Account:
    Name = ""
    Phone = ""
    Website = "" 
    def __init__(self, Name= None, Phone=None, Website=None,jsonObject = None):
        if(jsonObject== None):
            self.Name = Name
            self.Phone = Phone
            self.Website = Website
        else:
            self.__dict__ = json.loads(json.dumps(jsonObject))          
@app.route('/', methods=['GET', 'POST'])
def hello():
    if request.method == "POST":
        _json = Account(request.json)
        return _json.Name
    else:
        lst = []
        for i in range(5):
            acc =  Account("rizwan new "+str(i),"0333","www,fasih.com")
            lst.append(acc)
        print(lst, lambda x: x.__dict__ )
        return json.dumps(lst,default = lambda x: x.__dict__)
@app.route('/test',methods = ["POST"])
def addStudent():
    '''
    if you want to deserialize complete object you must write jsonObject in paremeter
    '''
    acc =Account(jsonObject =request.json)
    return jsonify({"isSuccess":"true"}),201
if __name__ == '__main__':
    app.run(debug=True)