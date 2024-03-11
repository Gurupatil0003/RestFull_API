from flask import Flask, jsonify
from werkzeug.exceptions import BadRequest

@app.errorhandler(BadRequest)
def bad_request_error(error):
    return jsonify({'error': 'Bad Request'}), 400

if __name__ == '__main__':
    app.run(debug=True)
