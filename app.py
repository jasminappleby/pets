from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import pets
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hi there! To check out the pets we have, type /pets into the URL bar!'}), 200


