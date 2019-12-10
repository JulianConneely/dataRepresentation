from flask import Flask, jsonify, request, abort

app = Flask(__name__, static_url_path='', static_folder='.')

poems=[
    { "id":1, "Title":"Daffodils", "Author":"William Wordsworth", "Price":1000},
    { "id":2, "Title":"The Listeners", "Author":"Walter De La Mere", "Price":800},
    { "id":3, "Title":"Mirror in February", "Author":"Patrick Kavanagh", "Price":1100}
]
nextId=4
#app = Flask(__name__)

#@app.route('/')
#def index():
#    return "Hello, World!"

#curl "http://127.0.0.1:5000/poems"
@app.route('/poems')
def getAll():
    return jsonify(poems)

#curl "http://127.0.0.1:5000/poems/2"
@app.route('/poems/<int:id>')
def findById(id):
    foundpoems = list(filter(lambda t: t['id'] == id, poems))
    if len(foundpoems) == 0:
        return jsonify ({}) , 204

    return jsonify(foundpoems[0])

#curl  -i -H "Content-Type:application/json" -X POST -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/poems
@app.route('/poems', methods=['POST'])
def create():
    global nextId
    if not request.json:
        abort(400)
    # other checking 
    book = {
        "id": nextId,
        "Title": request.json['Title'],
        "Author": request.json['Author'],
        "Price": request.json['Price'],
    }
    nextId += 1
    poems.append(book)
    return jsonify(book)

#curl  -i -H "Content-Type:application/json" -X PUT -d "{\"Title\":\"hello\",\"Author\":\"someone\",\"Price\":123}" http://127.0.0.1:5000/poems/1
@app.route('/poems/<int:id>', methods=['PUT'])
def update(id):
    foundpoems = list(filter(lambda t: t['id']== id, poems))
    if (len(foundpoems) == 0):
        abort(404)
    foundBook = foundpoems[0]
    if not request.json:
        abort(400)
    reqJson = request.json
    if 'Price' in reqJson and type(reqJson['Price']) is not int:
        abort(400)

    if 'Title' in reqJson:
        foundBook['Title'] = reqJson['Title']
    if 'Author' in reqJson:
        foundBook['Author'] = reqJson['Author']
    if 'Price' in reqJson:
        foundBook['Price'] = reqJson['Price']
    
    return jsonify(foundBook)
        

    return "in update for id "+str(id)

@app.route('/poems/<int:id>' , methods=['DELETE'])
def delete(id):
    foundpoems = list(filter(lambda t: t['id']== id, poems))
    if (len(foundpoems) == 0):
        abort(404)
    poems.remove(foundpoems[0])
    return jsonify({"done":True})




if __name__ == '__main__' :
    app.run(debug= True)