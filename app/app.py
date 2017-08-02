from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from schema import SchemaError
from helper import schema, discover_province
import os

app = Flask(__name__)

# Configurations
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route('/properties', methods=['POST'])
def create_imovel():

    if request.data:
        request_data = request.get_json(force=True)
        try:
            schema.validate([request_data])
            record = Properties(request_data['x'],
                                request_data['y'],
                                request_data['title'],
                                request_data['price'],
                                request_data['description'],
                                request_data['beds'],
                                request_data['baths'],
                                request_data['squareMeters'])
            db.session.add(record)
            db.session.commit()
            return jsonify(message='Imovel criado com sucesso! Id: %s' % record)
        except SchemaError, e:
            return jsonify(message=str(e))
    else:
        return jsonify(message='Cade o body !?')

@app.route('/properties/<id>', methods=['GET'])
def find_propertie(id):

    record = Properties.query.get(id)
    province = discover_province(record.x, record.y)
    return jsonify(id=record.id,
                    x=record.x,
                    y=record.y,
                    title=record.title,
                    price=record.price,
                    description=record.description,
                    beds=record.beds,
                    baths=record.baths,
                    squareMeters=record.squareMeters,
                    province=province)

@app.route('/properties', methods=['GET'])
def find_properties():

    ax = request.args.get('ax')
    ay = request.args.get('ay')
    bx = request.args.get('bx')
    by = request.args.get('by')
    records = Properties.query.filter((Properties.x <= ax) &
                                      (Properties.y <= ay) &
                                      (Properties.x <= bx) &
                                      (Properties.y <= by))
    properties = []
    for record in records:
        propertie = {}
        propertie['id'] = record.id
        propertie['x'] = record.x
        propertie['y'] = record.y
        propertie['title'] = record.title
        propertie['price'] = record.price
        propertie['description'] = record.description
        propertie['beds'] = record.beds
        propertie['baths'] = record.baths
        propertie['squareMeters'] = record.squareMeters
        propertie['province'] = discover_province(record.x, record.y)
        properties.append(propertie)
    return jsonify(foundProperties=records.count(), properties=properties)

class Properties(db.Model):

    __tablename__  = 'table_properties'
    __table_args__ = {'sqlite_autoincrement': True}

    id = db.Column('id', db.Integer, primary_key=True)
    x = db.Column('x', db.Integer)
    y = db.Column('y', db.Integer)
    title = db.Column('title', db.Unicode)
    price = db.Column('price', db.Integer)
    description = db.Column('description', db.Unicode)
    beds = db.Column('beds', db.Integer)
    baths = db.Column('baths', db.Integer)
    squareMeters = db.Column('squareMeters', db.Integer)

    def __init__(self, x, y, title, price, description, beds, baths, squareMeters):
        self.x = x
        self.y = y
        self.title = title
        self.price = price
        self.description = description
        self.beds = beds
        self.baths = baths
        self.squareMeters = squareMeters

    def __repr__(self):
        return '%s' % self.id