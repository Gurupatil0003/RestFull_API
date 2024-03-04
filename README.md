# RestFull_API
Rest stands for Representational State Transfer.

Let's understand the meaning of each word in the REST acronym.

 State means data
 Representational means formats (such as XML, JSON, YAML, HTML, etc)
 Transfer means carry data between consumer and provider using the HTTP protocol
 
![Example Image](https://github.com/Gurupatil0003/RestFull_API/blob/master/rest-api.png/)
![Example Image](https://github.com/Gurupatil0003/RestFull_API/blob/master/rest-api.png/)


## Features of REST Overview

- Uniform Interface
-Representations
- Messages
- Links between resources
- Caching
- Stateless
- 
## Uniform Interface
- A logical URI system with uniform ways to fetch and manipulate data is what makes REST easy to work with.
- In REST architecture, there is the concept of safe and idempotent methods.
- Safe methods are the ones that do not modify resources. An example include GET and HEAD.
- An idempotent method is a method that produces the same results no matter how many times is executed. These are GET, PUT and DELETE.


##2 . Representations

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

SQL databases use SQL for data manipulation and definition.
SQL systems work great when the data in use needs to be relational and the schema is predefined.
SQL databases store data in forms of the tables made up of rows and columns and vertically scalable.
7. NoSQL Databases

## NoSQL databases

have a dynamic schema for unstructured data and store data in different ways ranging from column-based(Apache Cassandra), document-based(MongoDB), graph-based(Neo4j), or as a key-value store (Redis).
This provides the flexibility to store data without a predefined structure and versatility to add fields to the data structure on the go.
Being schemaless is the key distinction of NoSQL databases, and it also makes them better suited for distributed systems.
