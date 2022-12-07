from flask import Flask

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database\\billing.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
if __name__ == '__main__':
    app.run(debug=True, port=4000)