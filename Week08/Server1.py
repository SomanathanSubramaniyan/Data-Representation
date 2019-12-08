from flask import Flask,jsonify,request,abort
from flask_cors import CORS

app = Flask(__name__,static_url_path='', static_folder='../')
CORS(app)

Accidents=[
    {"id":1, "province":"Leinster", "VehicleType":"Car", "DriverAge":"16 to 30", "DriverSex":"Male","Month-Year":"May-2019"},
    {"id":2, "province":"Ulster", "VehicleType":"Lorry", "DriverAge":"31 to 40", "DriverSex":"Female","Month-Year":"Jan-2019"},
    {"id":3, "province":"Munster", "VehicleType":"Nus", "DriverAge":"40 to 50", "DriverSex":"Male","Month-Year":"Feb-2019"}
       ]

nextID=4
#@app.route('/')
#def index():
#    return "Hello, world!"

@app.route('/Accidents')
def getAll():
    return jsonify(Accidents)

#curl -X GET "http://127.0.0.1:5000/Accidents/2"
@app.route('/Accidents/<int:id>')
def findByid(id):
    foundAccident=list(filter (lambda a: a["id"] == id, Accidents))
    if len(foundAccident) ==0:
        return jsonify({}),204
    return jsonify(foundAccident[0])

#curl -i -H "Content-Type:application/json" -X POST -d "{\"province\":\"Munster\", \"VehicleType\":\"Bus\", \"DriverAge\":\"40 to 50\", \"DriverSex\":\"Male\",\"Month-Year\":\"Feb-2019\"}" http://127.0.0.1:5000/Accidents
@app.route('/Accidents', methods=['POST'])
def create():
    if not request.json:
        abort(400)
    Accident = {
    "province":request.json['province'],
    "VehicleType":request.json['VehicleType'] ,
    "DriverAge":request.json['DriverAge'] ,
    "DriverSex":request.json['DriverSex'] ,
    "Month-Year":request.json['Month-Year'] }
    values = { Accident["province"],Accident["VehicleType"],Accident["DriverAge"],Accident["DriverSex"],Accident["Month-Year"]  }
    newId = AccidentDAO.create(values)
    Accident["id"]=newId
    return jsonify(Accident) 

#curl -i -H "Content-Type:application/json" -X PUT -d "{\"VehicleType\":\"Bus\"}" http://127.0.0.1:5000/Accidents/3
@app.route('/Accidents/<int:id>', methods=['PUT'])
def update(id):
    foundAccidents = AccidentDAO.findByID(id)
    if len(foundAccidents)==0:
        abort(404)
    foundAccident = foundAccidents[0]
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'province' in reqJson:
        foundAccident['province'] = reqJson['province']
    if 'VehicleType' in reqJson:
        foundAccident['VehicleType'] = reqJson['VehicleType']
    if 'DriverAge' in reqJson:
        foundAccident['DriverAge'] = reqJson['DriverAge']
    if 'DriverSex' in reqJson:
        foundAccident['DriverSex'] = reqJson['DriverSex']
    if 'Month-Year' in reqJson:
        foundAccident['Month-Year'] = reqJson['Month-Year']
    values = { foundAccident["province"],foundAccident["VehicleType"],foundAccident["DriverAge"],foundAccident["DriverSex"],foundAccident["Month-Year"], foundAccident["id"]  }

    return jsonify(foundAccident)
    
#curl -X DELETE "http://127.0.0.1:5000/Accidents/1"
@app.route('/Accidents/<int:id>', methods=['DELETE'])
def delete(id):
    foundAccident=list(filter (lambda a: a["id"] == id, Accidents))
    if len(foundAccident) ==0:
        return jsonify({}),204
    Accidents.remove(foundAccident[0])
    return jsonify({"done":True})

if __name__ == '__main__':
    app.run(debug=True)
