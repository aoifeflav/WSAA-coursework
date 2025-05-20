from flask import Flask, jsonify, request, abort
from flask_cors import CORS, cross_origin
from countriesDAO import countryDAO

app = Flask(__name__, static_url_path='', static_folder='.')
cors = CORS(app) # allow CORS for all domains on all routes.
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/')
@cross_origin()
def index():
    return "Hello, World!"

# Get all countries
@app.route('/countries')
@cross_origin()
def getAll():
    results = countryDAO.getAll()
    return jsonify(results)

# Get a country by ID
@app.route('/countries/<int:id>')
@cross_origin()
def findById(id):
    foundCountry = countryDAO.findByID(id)
    if not foundCountry:
        abort(404)
    return jsonify(foundCountry)

# Create a new country
@app.route('/countries', methods=['POST'])
@cross_origin()
def create():
    if not request.json:
        abort(400)
    # other checking 
    country = {
        "country_name": request.json.get('country_name'),
        "visit_date": request.json.get('visit_date'),
        "rating": request.json.get('rating')
    }
    addedcountry = countryDAO.create(country)
    return jsonify(addedcountry), 201

# Update an existing country
@app.route('/countries/<int:id>', methods=['PUT'])
@cross_origin()
def update(id):
    foundCountry = countryDAO.findByID(id)
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
    countryDAO.update(id, foundCountry)
    return jsonify(foundCountry)
        
# Delete a country
@app.route('/countries/<int:id>', methods=['DELETE'])
@cross_origin()
def delete(id):
    foundCountry = countryDAO.findByID(id)
    if not foundCountry:
        abort(404)
    countryDAO.delete(id)
    return jsonify({"done": True})


if __name__ == '__main__' :
    app.run(debug= True)