# A program that creates a RESTful API that supports data validation and error
handling.

```python

from flask import Flask, jsonify, request
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)

# Sample data
users = [
    {"id": 1, "name": "Alice", "age": 30},
    {"id": 2, "name": "Bob", "age": 25},
    {"id": 3, "name": "Charlie", "age": 35}
]

# Schema for data validation
class UserSchema(Schema):
    id = fields.Integer(required=True)
    name = fields.String(required=True)
    age = fields.Integer(required=True)

# Error handler for validation errors
@app.errorhandler(ValidationError)
def handle_validation_error(error):
    response = jsonify({"error": error.messages})
    response.status_code = 400
    return response

# GET request to fetch all users
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

# GET request to fetch a specific user
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = next((user for user in users if user['id'] == user_id), None)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# POST request to add a new user
@app.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.json
        UserSchema().load(data)
        users.append(data)
        return jsonify(data), 201
    except ValidationError as err:
        return jsonify({"error": err.messages}), 400

if __name__ == '__main__':
    app.run(debug=True)
```

```python 
python app.py

```
### Use Postman to perform other operation

### here are some example HTTP commands using curl to interact with the RESTful API

### GET All Users:
```python
curl http://127.0.0.1:5000/users
```

### GET a Specific User:


```python

curl http://127.0.0.1:5000/users/1

```
### POST a New User:

```python

curl -X POST -H "Content-Type: application/json" -d '{"id": 4, "name": "David", "age": 40}' http://127.0.0.1:5000/users
```

### for error handling try this

```python

{"id": 1, "name": "Alice", "age": 30}

```
