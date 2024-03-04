## what is Json
- JSON stands for JavaScript Object Notation

- JSON is a lightweight format for storing and transporting data

- JSON is often used when data is sent from a server to a web page

- JSON is "self-describing" and easy to understand

## syntax/Rule
- Data is in name/value pairs
- Data is separated by commas
- Curly braces hold objects
- Square brackets hold arrays

## JSON Objects
- JSON objects are written inside curly braces.

- Just like in JavaScript, objects can contain multiple name/value pairs:
```python
{"firstName":"John", "lastName":"Doe"}
```

## JSON Arrays
- JSON arrays are written inside square brackets.

-Just like in JavaScript, an array can contain objects:
``` python
"employees":[
    {"firstName":"John", "lastName":"Doe"},
    {"firstName":"Anna", "lastName":"Smith"},
    {"firstName":"Peter", "lastName":"Jones"}
]
```
## jsonify

- jsonify is a function provided by Flask for JSON serialization. 
- It converts a Python dictionary into a JSON response object that can be returned from a Flask route or view function.
