from flask import Flask
from Models import db, Productos

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database\\billing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/api/v1/products')
def get_products():
    products = Productos.query.all()
    print(products)
    return 'It works!'

if __name__ == '__main__':
    app.run(debug=True, port=4000)