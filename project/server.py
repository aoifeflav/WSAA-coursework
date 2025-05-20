from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'

from countriesDAO import CountryDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#app = Flask(__name__)

@app.route('/')
@cross_origin()
def index():
    return "Hello, World!"

#curl "http://127.0.0.1:5000/countries"
@app.route('/countries')
@cross_origin()
def getAll():
    #print("in getall")
    results = CountryDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/countries/2"
@app.route('/books/<int:id>')
@cross_origin()
def findById(id):
    foundBook = CountryDAO.findByID(id)

    return jsonify(foundBook)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"country_name\":\"France\",\"visit_date\":\"2017-06-01\",\"rating\":7}" http://127.0.0.1:5000/countries
@app.route('/countries', methods=['POST'])
@cross_origin()
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    country = {
        "country_name": request.json['country_name'],
        "visit_date": request.json['visit_date'],
        "rating": request.json['rating'],
    }
    addedcountry = CountryDAO.create(country)
    
    return jsonify(addedcountry)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"title\":\"hello\",\"author\":\"someone\",\"price\":123}" http://127.0.0.1:5000/books/1
@app.route('/countries/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundCountry = CountryDAO.findByID(id)
    if not foundCountry:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'rating' in reqJson and type(reqJson['rating']) is not int:
        abort(400)

    if 'country_name' in reqJson:
        foundCountry['country_name'] = reqJson['country_name']
    if 'visit_date' in reqJson:
        foundCountry['visit_date'] = reqJson['visit_date']
    if 'rating' in reqJson:
        foundCountry['rating'] = reqJson['rating']
    CountryDAO.update(id,foundCountry)
    return jsonify(foundCountry)
        

    

@app.route('/countries/<int:id>' , methods=['DELETE'])
@cross_origin()
def delete(id):
    CountryDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)