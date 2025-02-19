from flask import Flask, jsonify, request, abort
from poemsDAO import poemsDAO

app = Flask(__name__, static_url_path='', static_folder='.')

#curl "http://127.0.0.1:5000/poems"
@app.route('/poems')
def getAll():
    #print("in getall")
    results = poemsDAO.getAll()
    return jsonify(results)

#curl "http://127.0.0.1:5000/poems/2"
@app.route('/poems/<int:id>')
def findById(id):
    foundpoems = poemsDAO.findByID(id)

    return jsonify(foundpoems)

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/poems
@app.route('/poems', methods=['POST'])
def create():
    
    if not request.json:
        abort(400)
    # other checking 
    poems = {
        "Title": request.json['Title'],
        "Author": request.json['Author'],
        "Price": request.json['Price'],
    }
    values =(poems['Title'],poems['Author'],poems['Price'])
    newId = poemsDAO.create(values)
    poems['id'] = newId
    return jsonify(poems)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/poems/1
@app.route('/poems/<int:id>', methods=['PUT'])
def update(id):
    foundpoems = poemsDAO.findByID(id)
    if not foundpoems:
        abort(404)
    
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    if 'Title' in reqJson:
        foundpoems['Title'] = reqJson['Title']
    if 'Author' in reqJson:
        foundpoems['Author'] = reqJson['Author']
    if 'Price' in reqJson:
        foundpoems['Price'] = reqJson['Price']
    values = (foundpoems['Title'],foundpoems['Author'],foundpoems['Price'],foundpoems['id'])
    poemsDAO.update(values)
    return jsonify(foundpoems)
        

    

@app.route('/poems/<int:id>' , methods=['DELETE'])
def delete(id):
    poemsDAO.delete(id)
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)