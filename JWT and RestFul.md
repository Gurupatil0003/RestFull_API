```python
from flask import Flask
from flask import jsonify
from flask import request

from flask_jwt_extended import create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_jwt_extended import jwt_required
from flask_jwt_extended import JWTManager

app = Flask(__name__)

# Setup the Flask-JWT-Extended extension
app.config["JWT_SECRET_KEY"] = "super-secret"  # Change this!
jwt = JWTManager(app)


# Create a route to authenticate your users and return JWTs. The
# create_access_token() function is used to actually generate the JWT.
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username", None)
    password = request.json.get("password", None)
    if username != "test" or password != "test":
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=username)
    return jsonify(access_token=access_token)


# Protect a route with jwt_required, which will kick out requests
# without a valid JWT present.
@app.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    # Access the identity of the current user with get_jwt_identity
    current_user = get_jwt_identity()
    return jsonify(logged_in_as=current_user), 200


if __name__ == "__main__":
    app.run()


### Run your application
```python
python app.py

```
## Here We are Http commands [HTTPie](https://httpie.io/)

```python
We can see this in action using HTTPi


```


```python
### http method for Get method
```python
http GET :5000/protected
```

### Output After Executing the above Code
```python
HTTP/1.0 401 UNAUTHORIZED
Content-Length: 39
Content-Type: application/json
Date: Sun, 24 Jan 2021 18:09:17 GMT
Server: Werkzeug/1.0.1 Python/3.8.6

{
    "msg": "Missing Authorization Header"
}
```

### Post methos using http 
```python 
http POST :5000/login username=test password=test
```

### After Excecution output
```python
HTTP/1.0 200 OK
Content-Length: 288
Content-Type: application/json
Date: Sun, 24 Jan 2021 18:10:39 GMT
Server: Werkzeug/1.0.1 Python/3.8.6

{
    "access_token": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTYxMTUxMTgzOSwianRpIjoiMmI0NzliNTQtYTI0OS00ZDNjLWE4NjItZGVkZGIzODljNmVlIiwibmJmIjoxNjExNTExODM5LCJ0eXBlIjoiYWNjZXNzIiwic3ViIjoidGVzdCIsImV4cCI6MTYxNDEwMzgzOX0.UpTueBRwNLK8e-06-oo5Y_9eWbaN5T3IHwKsy6Jauaw"
}

```python
$JWT=yours Generated token
```
### Testing 
```python
http GET :5000/protected Authorization:"Bearer $JWT"

```

### output
```pyhon 
HTTP/1.0 200 OK
Content-Length: 24
Content-Type: application/json
Date: Sun, 24 Jan 2021 18:12:02 GMT
Server: Werkzeug/1.0.1 Python/3.8.6

{
    "logged_in_as": "test"
}
```
