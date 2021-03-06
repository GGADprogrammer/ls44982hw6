from flask import Flask,render_template,send_from_directory,request, jsonify,make_response
from flask_cors import CORS, cross_origin
import boto3
import os
app = Flask(__name__, static_folder='./build', static_url_path='/')
cors = CORS(app)
@app.route('/api')
@cross_origin()
def Welcome():
    firstname = request.args.get('firstname')
    lastname='song'
    # return jsonify({'result': firstname+lastname})
    if firstname =='litong':
        return firstname+lastname
    else:
        return 'User Not Found'
@app.route('/')
def serve():
    return send_from_directory(app.static_folder, 'index.html')
if __name__ == '__main__':
    #app.run(host='0.0.0.0')
    app.run(host='0.0.0.0',debug=True, port=5000)