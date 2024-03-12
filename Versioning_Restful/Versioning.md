# Versioning
One of the major challenges surrounding exposing services is handling updates to the API contract. Clients may not want to update their applications when the API changes, so an API versioning strategy becomes crucial. A versioning strategy allows clients to continue using the existing REST API and migrate their applications to the newer API when they are ready.

There are four common ways to version a REST API.

#### 1. Versioning through URI Path
http://www.example.com/api/1/products

REST API versioning through the URI path
One way to version a REST API is to include the version number in the URI path.

xMatters uses this strategy, and so do DevOps teams at Facebook, Twitter, Airbnb, and many more.

The internal version of the API uses the 1.2.3 format, so it looks as follows:

MAJOR.MINOR.PATCH

Major version: The version used in the URI and denotes breaking changes to the API. Internally, a new major version implies creating a new API and the version number is used to route to the correct host.
Minor and Patch versions: These are transparent to the client and used internally for backward-compatible updates. They are usually communicated in change logs to inform clients about a new functionality or a bug fix.
This solution often uses URI routing to point to a specific version of the API. Because cache keys (in this situation URIs) are changed by version, clients can easily cache resources. When a new version of the REST API is released, it is perceived as a new entry in the cache.

Pros: Clients can cache resources easily
Cons: This solution has a pretty big footprint in the code base as introducing breaking changes implies branching the entire API

### 2. Versioning through query parameters
http://www.example.com/api/products?version=1

REST API versioning through the query string
Another option for versioning a REST API is to include the version number as a query parameter.

This is a straightforward way of versioning an API from an implementation point of view.

~~~python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    version = request.args.get('version')
    
    if version == 'v1':
        # Logic for version 1
        return jsonify({'data': 'Version 1'})
    elif version == 'v2':
        # Logic for version 2
        return jsonify({'data': 'Version 2'})
    else:
        return jsonify({'error': 'Invalid version specified'}), 400

if __name__ == '__main__':
    app.run(debug=True)
~~~

#### Try below url for access the Version 
~~~python
/api/data?version=v1
~~~
- Pros: It’s a straightforward way to version an API, and it’s easy to default to the latest version
- Cons: Query parameters are more difficult to use for routing requests to the proper API version

### 3. Versioning through custom headers
curl -H “Accepts-version: 1.0”
http://www.example.com/api/products

REST APIs can also be versioned by providing custom headers with the version number included as an attribute.The main difference between this approach and the two previous ones is that it doesn’t clutter the URI with versioning information.
~~~python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    version = request.headers.get('X-API-Version')
    
    if version == 'v1':
        # Logic for version 1
        return jsonify({'data': 'Version 1'})
    elif version == 'v2':
        # Logic for version 2
        return jsonify({'data': 'Version 2'})
    else:
        return jsonify({'error': 'Invalid version specified'}), 400

if __name__ == '__main__':
    app.run(debug=True)

~~~

~~~python
GET /api/data HTTP/1.1
Host: example.com
X-API-Version: v1


~~~

- Pros: It doesn’t clutter the URI with versioning information
- Cons: It requires custom headers

### 4. Versioning through content negotiation
curl -H “Accept: application/vnd.xm.device+json; version=1” http://www.example.com/api/products

The last strategy we are addressing is versioning through content negotiation.

This approach allows us to version a single resource representation instead of versioning the entire API which gives us a more granular control over versioning. It also creates a smaller footprint in the code base as we don’t have to fork the entire application when creating a new version. Another advantage of this approach is that it doesn’t require implementing URI routing rules introduced by versioning through the URI path.

One of the drawbacks of this approach is that it is less accessible than URI-versioned APIs: Requiring HTTP headers with media types makes it more difficult to test and explore the API using a browser.

~~~python
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/data', methods=['GET'])
def get_data():
    accept_header = request.headers.get('Accept')
    
    if 'application/vnd.company.v1+json' in accept_header:
        # Logic for version 1
        return jsonify({'data': 'Version 1'})
    elif 'application/vnd.company.v2+json' in accept_header:
        # Logic for version 2
        return jsonify({'data': 'Version 2'})
    else:
        return jsonify({'error': 'Unsupported version requested'}), 406

if __name__ == '__main__':
    app.run(debug=True)
~~~

~~~python

GET /api/data HTTP/1.1
Host: example.com
Accept: application/vnd.company.v1+json


~~~
    

- Pros: Allows us to version a single resource representation instead of versioning the entire API, which gives us a more granular control over versioning. Creates a smaller footprint. Doesn’t require implementing URI routing rules.

- Cons: Requiring HTTP headers with media types makes it more difficult to test and explore the API using a browser

### Summary
Versioning is a crucial part of API design. It gives developers the ability to improve their API without breaking the client’s applications when new updates are rolled out.
