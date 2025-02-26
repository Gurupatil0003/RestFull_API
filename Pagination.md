
![17405344808196802447823478589289](https://github.com/user-attachments/assets/98387c3a-8968-4c63-a4f3-7c6a7b817dcd)


~~~python


from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///products.db'  # SQLite for simplicity
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {"id": self.id, "name": self.name, "price": self.price}

# Route for Paginated Products
@app.route('/products', methods=['GET'])
def get_products():
    page = request.args.get('page', 1, type=int)  # Default: page 1
    per_page = request.args.get('per_page', 5, type=int)  # Default: 5 per page

    pagination = Product.query.paginate(page=page, per_page=per_page, error_out=False)

    return jsonify({
        "products": [product.to_dict() for product in pagination.items],
        "total": pagination.total,
        "pages": pagination.pages,
        "current_page": pagination.page,
        "next_page": pagination.next_num,
        "prev_page": pagination.prev_num
    })

# Initialize Database & Add Sample Data
@app.before_first_request
def create_tables():
    db.create_all()
    if not Product.query.first():
        products = [Product(name=f"Product {i}", price=i * 10) for i in range(1, 21)]
        db.session.bulk_save_objects(products)
        db.session.commit()

if __name__ == '__main__':
    app.run(debug=True)
~~~
~~~python
GET http://127.0.0.1:5000/products?page=1&per_page=5


~~~

~~~python

GET http://127.0.0.1:5000/products?page=2&per_page=10

~~~
