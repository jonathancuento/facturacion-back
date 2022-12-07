import sqlite3 as sql

DB_PATH = ".\\billing.db"

def createDB():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.executescript("""
        CREATE TABLE PRODUCTOS (
            id_producto integer,
            nombre text,
            descripcion text,
            precio numeric,
            cantida integer,
            PRIMARY KEY(id_producto)
        );
        CREATE TABLE FACTURA (
            id_factura integer,
            id_cliente text,
            subtotal numeric,
            total numeric,
            PRIMARY KEY(id_factura)
        );
        CREATE TABLE COMPRAS (
            id_factura integer,
            id_producto integer,
            precio_producto numeric,
            PRIMARY KEY(id_factura, id_producto)
        );
        CREATE TABLE CLIENTE (
            id_cliente text,
            nombre text,
            telefono text,
            direccion text,
            PRIMARY KEY(id_cliente)
        );
    """)
    conn.commit()
    conn.close()

def addData():
    conn = sql.connect(DB_PATH)
    cursor = conn.cursor()  
    dataPRODUCTOS = [
        (1, 'Coca Cola', 'Bebida gaseosa', 1.50, 100),
        (2, 'Pepsi', 'Bebida gaseosa', 1.50, 100),
    ]
    dataFACTURA = [
        (1, '1', 0, 0),
        (2, '2', 0, 0),
    ]
    dataCOMPRAS = [
        (1, 1, 1.50),
        (1, 2, 1.50),
    ]
    dataCLIENTE = [
        ('1', 'Juan Perez', '809-555-5555', 'Santo Domingo'),
        ('2', 'Maria Perez', '809-555-5555', 'Santo Domingo'),
    ]
    cursor.executemany("INSERT INTO PRODUCTOS VALUES (?,?,?,?,?)", dataPRODUCTOS)
    cursor.executemany("INSERT INTO FACTURA VALUES (?,?,?,?)", dataFACTURA)
    cursor.executemany("INSERT INTO COMPRAS VALUES (?,?,?)", dataCOMPRAS)
    cursor.executemany("INSERT INTO CLIENTE VALUES (?,?,?,?)", dataCLIENTE)
    conn.commit()
    conn.close()

if __name__ == "__main__":
    print('CREANDO BASE DE DATOS...')
    createDB()
    print('AGREGANDO DATOS...')
    addData()
    print('LISTO!')
