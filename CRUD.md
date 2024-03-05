# CRUD operation 

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

# Here We are Gone Perform CRUD operation Using CURL method

## GET Method
```pyhon
curl -X GET http://127.0.0.1:5000/books
```

## POST
```python
curl -X POST -H "Content-Type: application/json" -d "{\"title\":\"New Book\", \"author\":\"Author Name\", \"year\":2022}" http://127.0.0.1:5000/books

```

## PUT
```python

curl -X PUT -H "Content-Type: application/json" -d "{\"title\":\"Updated Title\", \"author\":\"Updated Author\", \"year\":2023}" http://127.0.0.1:5000/books/1

```

## DELETE

```python

curl -X DELETE http://127.0.0.1:5000/books/1

```



## other Method 

- First Create One json file with

- Here My Json File Name data.json
```python
{
    "title": "Still Thinking",
    "author": "Guru patil",
    "year": 2023
}

```

## POST Method
```python
curl -X POST -H "Content-Type: application/json" -d @data.json http://127.0.0.1:5000/books

```
## PUT method

-Here Name my file name as update_data.json
```python
{
    "title": "Peace",
    "author": "God",
    "year": 2023
}

```

```python
curl -X PUT -H "Content-Type: application/json" -d @update_data.json http://127.0.0.1:5000/books/1
```
