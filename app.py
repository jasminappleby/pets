from flask import Flask, jsonify, request
from flask_cors import CORS
from controllers import pets
from werkzeug import exceptions

app = Flask(__name__)
CORS(app)

@app.route('/')
def home():
    return jsonify({'message': 'Hi there! To check out the pets we have, type /pets into the URL bar!'}), 200


@app.route('/pets', methods=['GET', 'POST'])
def pets_handler():
    fns = {
        'GET': pets.index,
        'POST': pets.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/pets/<int:pet_id>', methods=['GET', 'PATCH', 'PUT', 'DELETE'])
def pet_handler(pet_id):
    fns = {
        'GET': pets.show,
        'PATCH': pets.update,
        'PUT': pets.update,
        'DELETE': pets.destroy
    }
    resp, code = fns[request.method](request, pet_id)
    return jsonify(resp), code

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return {'message': f'Uh oh! You ran into an error! The error is: {err}'}, 404

@app.errorhandler(exceptions.BadRequest)
def handle_400(err):
    return {'message': f'Uh oh! You ran into an error! The error is: {err}'}, 400

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return {'message': f"This is a server error, so nothing is wrong on your end! Try our site again later."}, 500

if __name__ == "__main__":
    app.run(debug=True)