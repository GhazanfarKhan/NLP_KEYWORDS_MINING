from flask import Flask,jsonify,abort,make_response,request
import re
from KeywordSearcher import KeywordSearcher

app = Flask(__name__)
keyword_searcher = KeywordSearcher()
 
@app.route('/')
def index():
    return "Hello World!"

@app.route('/nlp/api/textminer/keywords', methods=['POST'])
def get_keywords():
    if not request.json or not 'title' in request.json:
        abort(400)
    if not request.json or not 'body' in request.json:
        abort(400)    

    keyword_count = 10

    if 'keywords' in request.json:
        keyword_count = int(request.json['keywords'])
    keys =  keyword_searcher.getKeywords(request.json['title'],request.json['body'],keyword_count)
    return jsonify({'keywords': list(keys)})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.errorhandler(400)
def not_found(error):
    return make_response(jsonify({'error': 'parameters not found'}), 400)

if __name__ == '__main__':
    app.run(debug=True)   