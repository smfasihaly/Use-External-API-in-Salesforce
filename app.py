from flask import Flask, jsonify
import json
app = Flask(__name__)

class Account:
    def __init__(self, Name, Phone, Website):
        self.Name = Name
        self.Phone = Phone
        self.Website = Website          
@app.route('/')
def hello():
    lst = []
    for i in range(5):
        acc =  Account("rizwan new "+str(i),"0333","www,fasih.com")
        lst.append(acc)
    print(lst, lambda x: x.__dict__ )
    return json.dumps(lst,default = lambda x: x.__dict__)

if __name__ == '__main__':
    app.run(debug=True)