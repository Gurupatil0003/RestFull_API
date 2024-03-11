from flask import Flask, jsonify
from werkzeug.exceptions import BadRequest
from werkzeug.exceptions import MethodNotAllowed

@app.errorhandler(MethodNotAllowed)
def method_not_allowed_error(error):
    return jsonify({'error': 'Method Not Allowed'}), 405


if __name__ == '__main__':
    app.run(debug=True)
