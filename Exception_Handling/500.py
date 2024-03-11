from flask import Flask, jsonify

from werkzeug.exceptions import InternalServerError
app = Flask(__name__)

@app.errorhandler(InternalServerError)
def internal_server_error(error):
    return jsonify({'error': 'Internal Server Error'}), 500

if __name__ == '__main__':
   app.run(debug=True)
