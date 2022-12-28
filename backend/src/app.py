from flask import Flask, request, jsonify, render_template
from flask_pymongo import PyMongo, ObjectId
from flask_cors import CORS

app = Flask(__name__, template_folder='../../templates')
app.config['MONGO_URI']='mongodb://localhost/crudapp'
mongo = PyMongo(app)

CORS(app)

db = mongo.db.users


@app.route('/users', methods=['POST'])
def createUser():
    id = db.insert_one({
        'name': request.json['name'],
        'email': request.json['email'],
        'gender': request.json['gender']
    })
    return jsonify({'id': str(id.inserted_id), 'msg': "User Added Successfully"})

@app.route('/users', methods=['GET'])
def getUsers():
    users = []
    for doc in db.find():
        users.append({
            '_id': str(ObjectId(doc['_id'])),
            'name': doc['name'],
            'email': doc['email'],
            'gender': doc['gender'],
        })
    return jsonify(users)

@app.route('/user/<id>', methods=['GET'])
def getUser(id):
    user = db.find_one({'_id': ObjectId(id)})
    return jsonify({
        '_id': str(ObjectId(user['_id'])),
        'name': user['name'],
        'email': user['email'],
        'gender': user['gender'],
    })

@app.route('/users/<id>', methods=['DELETE'])
def deleteUser(id):
    db.delete_one({'_id': ObjectId(id)})
    return jsonify({'msg': "User Deleted Successfully"})

@app.route('/users/<id>', methods=['PUT'])
def updateUser(id):
    db.update_one({'_id': ObjectId(id)}, {'$set': {
        'name': request.json['name'],
        'email': request.json['email'],
        'gender': request.json['gender']
    }})
    return jsonify({'msg': "User Updated Successfully"})


if __name__ == '__main__':
    app.run(debug=True)