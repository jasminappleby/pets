from werkzeug.exceptions import BadRequest

pets = [
    {'id': 1, 'name': 'Spike', 'age': 11, 'animal': 'dog', 'breed': 'shih tzu'},
    {'id': 2, 'name': 'Tigerlily', 'age': 9, 'animal': 'cat', 'breed': 'british shorthair'},
    {'id': 3, 'name': 'Salem', 'age': 500, 'animal': 'tortoise', 'breed': 'royal tortoise'}
]


def index(req):
    return [p for p in pets], 200

def show(req, uid):
    return find_by_uid(uid), 200

def create(req):
    new_pet = req.get_json()
    new_pet['id'] = sorted([p['id'] for p in pets])[-1] + 1
    cets.append(new_pet)
    return new_pet, 201

def update(req, uid):
    pet = find_by_uid(uid)
    data = req.get_json()
    print(data)
    for key, val in data.items():
        pet[key] = val
    return pet, 200

def destroy(req, uid):
    pet = find_by_uid(uid)
    pets.remove(pet)
    return pet, 204

def find_by_uid(uid):
    try:
        return next(pet for pet in pets if pet['id'] == uid)
    except:
        raise BadRequest(f"We don't have that pet with the id {uid}!")