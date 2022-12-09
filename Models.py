from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Productos(db.Model):
    __tablename__ = 'PRODUCTOS'
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.String(50), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)

    def __init__(self, id_producto, nombre, descripcion, precio, cantidad):
        self.id_producto = id_producto
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.cantidad = cantidad

    # def __repr__(self):
    #     return f"Producto: {self.nombre}"

class Factura(db.Model):
    __tablename__ = 'FACTURA'
    id_factura = db.Column(db.Integer, primary_key=True)
    id_cliente = db.Column(db.String(50), nullable=False)
    subtotal = db.Column(db.Float, nullable=False)
    total = db.Column(db.Float, nullable=False)

    def __init__(self, id_factura, id_cliente, subtotal, total):
        self.id_factura = id_factura
        self.id_cliente = id_cliente
        self.subtotal = subtotal
        self.total = total

    # def __repr__(self):
    #     return f"Factura: {self.id_factura}"

class Compras(db.Model):
    __tablename__ = 'COMPRAS'
    id_factura = db.Column(db.Integer, primary_key=True)
    id_producto = db.Column(db.Integer, primary_key=True)
    precio_producto = db.Column(db.Float, nullable=False)

    def __init__(self, id_factura, id_producto, precio_producto):
        self.id_factura = id_factura
        self.id_producto = id_producto
        self.precio_producto = precio_producto

    # def __repr__(self):
    #     return f"Compra: {self.id_factura}"

class Cliente(db.Model):
    __tablename__ = 'CLIENTE'
    id_cliente = db.Column(db.String(50), primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)
    telefono = db.Column(db.String(50), nullable=False)
    direccion = db.Column(db.String(50), nullable=False)

    def __init__(self, id_cliente, nombre, telefono, direccion):
        self.id_cliente = id_cliente
        self.nombre = nombre
        self.telefono = telefono
        self.direccion = direccion

    # def __repr__(self):
    #     return f"Cliente: {self.nombre}"