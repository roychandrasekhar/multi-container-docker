from flask import Flask, jsonify
from flask_restful import Resource, Api
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
api = Api(app)

# MySQL configurations
app.config['MYSQL_HOST'] = 'mysql'
app.config['MYSQL_USER'] = 'myuser'
app.config['MYSQL_PASSWORD'] = 'mypassword'
app.config['MYSQL_DB'] = 'mydatabase'

mysql = MySQL(app)

class Product(Resource):
    def get(self):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('SELECT name FROM products')
        products = cursor.fetchall()
        cursor.close()
        return {'product': [product['name'] for product in products]}

api.add_resource(Product, '/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
