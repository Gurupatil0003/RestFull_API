# RestFull_API 
Rest stands for Representational State Transfer.

Let's understand the meaning of each word in the REST acronym.

 State means data
 Representational means formats (such as XML, JSON, YAML, HTML, etc)
 Transfer means carry data between consumer and provider using the HTTP protocol
 
![Example Image](https://github.com/Gurupatil0003/RestFull_API/blob/master/rest-api.png/)

## What is REST API?
- To understand what is a REST API, let’s, first of all, understand what is an API. An API stands for an application programming interface. It defines how applications or devices can connect to and communicate 
 with each other.

- A REST (Representational State Transfer) API is an architectural style for an API that uses HTTP (Hypertext Transfer Protocol) request methods to access and manipulate data over the Internet. The most popular 
 HTTP request methods (which are explained below) are GET, POST, PUT, DELETE, PATCH, HEAD, TRACE, CONNECT and OPTIONS.

- One of the examples of when REST APIs are used is when we need to expose back-end systems and data to front-end developers in a standardized format. That's why REST APIs architecture is vital when it comes to 
 building web services that are consumed by a wide range of clients such as browsers, desktop applications and mobile devices.


## REST API Model

## 2. HTTP Methods
- HTTP (Hypertext Transfer Protocol) is a protocol that allows communication between clients and servers on the World Wide Web. There exist several dozen different HTTP Methods that can be used for different 
 purposes. The main 9 most popular HTTP Methods are explained below.



## 2.1. GET Request
- The GET request is one of the HTTP methods which in simple words is in charge of grabbing data from a data source. The response from a GET request can contain data such as a list of items, a single item, or 
 even just a status message.

- A GET request is a safe and idempotent method, meaning that it can be repeated multiple times without having any side effects because it should only retrieve data, not modify it.



## 2.2. POST Request
- The POST request is used to send data to the server from a client to create a new resource. The data which is sent as part of a POST request is encoded in the body of the request and is not visible in the URL, 
 unlike with a GET request.



## 2.3. PUT Request
- With help of the PUT request, you can update an existing resource. One important thing to keep in mind when you are updating an existing resource via PUT request is that the request body of a PUT request - - -- should contain a complete representation of the resource. Even if you want to update one of the several fields of an existing resource, you need to provide a complete representation of the resource and pass it 
  as a request body. Otherwise, the missing fields will be set to NULL, or in some other cases, the request just would fail. If you want to do a partial update of a resource, look at the PATCH HTTP method.



## 2.4. DELETE Request
- The DELETE request can be used when you want to delete an existing resource from the server. Usually, you specify a resource that you want to delete by providing an ID of a resource as part of the URL 
 parameter.



## 2.5. PATCH Request
- Similar to a PUT HTTP request, a PATCH request can be used to update an existing resource. However, the difference between PUT and PATCH is that when sending a PUT request, the body of a request should contain 
 a complete representation of the resource but with a PATCH request you can provide a partial representation of the resource.



## 2.6. HEAD Request
- HTTP HEAD method is used to fetch the request headers that would be returned if a corresponding GET request was made. In other words, the HEAD method is the same as the GET method with the only difference 
 being that it doesn't return the response body when the request was made.

- The HEAD method can be very useful because it can save you some bandwidth in situations when you only need to retrieve some metadata about the resource without retrieving the actual resource as part of the 
 response body. The metadata returned by a HEAD request can be used to validate the information about the resource such as Content-Length of the resource, Content-Type, Last-Modified date, etc.

- This metadata from the headers can be very handy in situations when you for example just want to check whether the resource actually exists before fetching it or maybe when you just want to see when the 
 resource was modified last time (P.S. imagine if a resource is a big file and you just need to check the date but you don't want to download it).



## 2.7. TRACE Request
- HTTP TRACE request can be used for debugging purposes when you want to determine what is exactly happening with your HTTP requests. When the TRACE request is sent, the web server would normally echo the exact 
 content of an HTTP request back to the client.

- However, the TRACE requests should not be enabled in a production environment because in some scenarios they potentially can reveal some sensitive information about the server.



## 2.8. CONNECT Request
- HTTP CONNECT request method can be used in order to establish a network connection between a client and a server to create a secure tunnel. Once the connection is established, the client and server can - 
  communicate with each other directly and forward data packets to each other.



## 2.9. OPTIONS Request
-  HTTP OPTIONS request method can be used to request the available communication options from the server for the target resource.

- When a client sends an OPTIONS request to a server, the server would normally include the list of the allowed HTTP methods for the target resource as part of the "Allow" header in the response.


![Example Image](https://github.com/Gurupatil0003/RestFull_API/blob/master/1622930986964.png)
![Example Image](https://github.com/Gurupatil0003/RestFull_API/blob/master/api_types.png)



## Features of REST Overview

- Uniform Interface
-Representations
- Messages
- Links between resources
- Caching
- Stateless

## Uniform Interface
- A logical URI system with uniform ways to fetch and manipulate data is what makes REST easy to work with.
- In REST architecture, there is the concept of safe and idempotent methods.
- Safe methods are the ones that do not modify resources. An example include GET and HEAD.
- An idempotent method is a method that produces the same results no matter how many times is executed. These are GET, PUT and DELETE.


## 2 . Representations

- Restful services focus on resources and providing access to the resources.
- A resource can be easily thought of as an object in OOP.
- This is the first thing to do while designing RESTful services is identifying different resources and determining the relation between them.
- Once the resources are identified, the representation is the next course of action
- Unlike SOAP which restricts us to use XML to represent the data, with REST we can use JSON or XML.
- Usually, JSON is the preferred method for representing the resources to be called by mobile or web clients, But XML can be used to represent more complex resources.


## 3. Messages

- The client and the server talk to each other via messages in which the cleint sends a message to the server which is often called a request and the server sends back a response
- Apart from the actual data exchanged between the client and the server in the form of request and response body, there are some metadata exchanged by the client and the server in the form of request and response headers.


## 4. Links between resources

- A resource is a fundamental concept in the world of REST architecture.
- A resource is an object with a type, associated data, and relationships to other resources alongside a set of methods that can be executed on it.
- This resource in a REST API can contain a link to other resources which should drive the process flow.


## 5. Caching

- Caching is a technique that stores a copy of a given resource, and serves it back when requested saving database calls and processing time. Caching can be configured to cache data in minutes, hours, and days, whereby after the configured time expires the cached data gets deleted.
- It can be done at different levels, like the client, the server, or a middleware proxy server.
- Caching in REST API is controlled using HTTP headers.
## 6. Stateless

- Each request from the client to the server must contain all the information necessary for the server to understand the request and cannot take advantage of any stored context on the server.
Session state is therefore kept entirely on the client
- Statelessness here means that every HTTP response is a complete entity in itself and enough to serve the purpose of providing information to be executed without any need for another HTTP request.


## API DESIGN

- 1.Long-term Implementation
This helps you analyze the flaws in design before actual implementation.
This helps the developers to choose the right kind of platforms and tools to build upon making sure the same system can be scaled for more users later.

## 2. Spec-Driven Development

This enforces API design using definition, and not just the code, which ensures that the changes are made to the codebase while API design is intact.

## 3. Prototyping

Once the API specs are put in place, prototyping helps you visualize the API before actual development by letting the developers create mock API to help them understand every potential aspect of the API
## 5. Authentication and Authorization

Authentication involves the verification process to know who the person is while authorization involves authoring an authenticated user to keep a check on resources allowed to access using Access Control List(ACL)
## 6. SQL Databases

- SQL databases use SQL for data manipulation and definition.
- SQL systems work great when the data in use needs to be relational and the schema is predefined.
- SQL databases store data in forms of the tables made up of rows and columns and vertically scalable.
## 7. NoSQL Databases

- have a dynamic schema for unstructured data and store data in different ways ranging from column-based(Apache Cassandra), document-based(MongoDB), graph-based(Neo4j), or as a key-value store (Redis).
- This provides the flexibility to store data without a predefined structure and versatility to add fields to the data structure on the go.
- Being schemaless is the key distinction of NoSQL databases, and it also makes them better suited for distributed systems.


## Here Is The Small Example Then You will understand This

# Example 1
```python
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {"message": "Hello, World!"}

api.add_resource(HelloWorld, '/hello')

if __name__ == '__main__':
    app.run(debug=True)
```

# Example 2
```python
from flask import Flask, jsonify

app = Flask(__name__)

# Dummy data for books
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813}
]

# Endpoint to retrieve all books
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

if __name__ == '__main__':
    app.run(debug=True)
```

### A program that creates a simple RESTful API that returns a list of users in JSON format.
```python
from flask import Flask, jsonify

app = Flask(__name__)

# Dummy user data
users = [
    {"id": 1, "name": "Guru", "age": 23},
    {"id": 2, "name": "Mounesh", "age": 23},
    {"id": 3, "name": "Mgpatils", "age": 23}
]

@app.route('/users', methods=['GET'])
def get_users():
    return jsonify(users)

if __name__ == '__main__':
    app.run(debug=True)
```
 ## Square Operation

```python

# using flask_restful 
from flask import Flask, jsonify, request 
from flask_restful import Resource, Api 

# creating the flask app 
app = Flask(__name__) 
# creating an API object 
api = Api(app) 

# making a class for a particular resource 
# the get, post methods correspond to get and post requests 
# they are automatically mapped by flask_restful. 
# other methods include put, delete, etc. 
class Hello(Resource): 

	# corresponds to the GET request. 
	# this function is called whenever there 
	# is a GET request for this resource 
	def get(self): 

		return jsonify({'message': 'hello world'}) 

	# Corresponds to POST request 
	def post(self): 
		
		data = request.get_json()	 # status code 
		return jsonify({'data': data}), 201


# another resource to calculate the square of a number 
class Square(Resource): 

	def get(self, num): 

		return jsonify({'square': num**2}) 


# adding the defined resources along with their corresponding urls 
api.add_resource(Hello, '/') 
api.add_resource(Square, '/square/<int:num>') 


# driver function 
if __name__ == '__main__': 

	app.run(debug = True) 
```

## CRUD operations
```python
from flask import Flask, jsonify, request, abort

app = Flask(__name__)

# Dummy data for books
books = [
    {"id": 1, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"id": 2, "title": "1984", "author": "George Orwell", "year": 1949},
    {"id": 3, "title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813}
]

# Endpoint to retrieve all books (GET)
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books)

# Endpoint to add a new book (POST)
@app.route('/books', methods=['POST'])
def add_book():
    if not request.json or 'title' not in request.json:
        abort(400)  # Bad request
    book = {
        'id': books[-1]['id'] + 1,
        'title': request.json['title'],
        'author': request.json.get('author', ""),
        'year': request.json.get('year', "")
    }
    books.append(book)
    return jsonify({'message': 'Book added', 'book': book}), 201  # Created

# Endpoint to retrieve a specific book (GET)
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)  # Not found
    return jsonify(book[0])

# Endpoint to update a specific book (PUT)
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)  # Not found
    if not request.json:
        abort(400)  # Bad request
    book[0]['title'] = request.json.get('title', book[0]['title'])
    book[0]['author'] = request.json.get('author', book[0]['author'])
    book[0]['year'] = request.json.get('year', book[0]['year'])
    return jsonify({'message': 'Book updated', 'book': book[0]})

# Endpoint to delete a specific book (DELETE)
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = [book for book in books if book['id'] == book_id]
    if len(book) == 0:
        abort(404)  # Not found
    books.remove(book[0])
    return jsonify({'message': 'Book deleted'}), 204  # No content

if __name__ == '__main__':
    app.run(debug=True)
```

```python

from flask import Flask, request
from flask_restful import Api, Resource
from marshmallow import Schema, fields, ValidationError

app = Flask(__name__)
api = Api(app)

class UserSchema(Schema):
    username = fields.Str(required=True)
    email = fields.Email(required=True)

class UserResource(Resource):
    def get(self):
        # Implement logic to retrieve and return user data
        # For demonstration, let's return dummy data
        users = [
            {"username": "user1", "email": "user1@example.com"},
            {"username": "user2", "email": "user2@example.com"}
        ]
        return users, 200

    def post(self):
        # Get user data from form parameters or request JSON
        json_data = request.get_json()
        username = json_data.get('username')
        email = json_data.get('email')

        try:
            # Validate user data
            user_data = UserSchema().load({"username": username, "email": email})
        except ValidationError as err:
            # Handle validation errors
            return {"message": "Validation error", "errors": err.messages}, 400
        
        # Process valid data (in this example, just return the data)
        return user_data, 201

api.add_resource(UserResource, '/user')

if __name__ == '__main__':
    app.run(debug=True)
```
