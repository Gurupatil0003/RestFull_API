from flask import Flask, jsonify
from werkzeug.exceptions import NotFound

app = Flask(__name__)

@app.errorhandler(NotFound)
def not_found_error(error):
    return jsonify({'error': 'Not Found'}), 404

if __name__ == '__main__':
    app.run(debug=True)
