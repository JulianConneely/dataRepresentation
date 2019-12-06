#!flask/bin/python
from flask import Flask
#from flask_cors import CORS

app = Flask(__name__, static_url_path='', static_folder='.')
#app = Flask(__name__)
#CORS(app)

@app.route('/')
def index():
    return 'About to test the static pages <a href="testhtml.html>here</a>'

@app.route('/book/<int:id>')
def getBook(id):
    return "you want book with "+ str(id)

@app.route('/book/<int:id>', methods=['DELETE'])
def deleteBook(id):
    return "in delete with id "+ str(id)


if __name__ == '__main__' :
    app.run(debug= True)