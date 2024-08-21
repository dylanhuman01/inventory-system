from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    serial_number = db.Column(db.String(50), nullable=False)
    purchase_date = db.Column(db.String(10), nullable=False)
    warranty_expiry = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    barcode = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    barcode = request.form['barcode']
    item = Item.query.filter_by(barcode=barcode).first()
    if item:
        return jsonify({
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'serial_number': item.serial_number,
            'purchase_date': item.purchase_date,
            'warranty_expiry': item.warranty_expiry,
            'location': item.location,
            'status': item.status
        })
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True) from flask import Flask, render_template, request, jsonify
from flask_sqlalchemy import SQLAlchemy

#app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inventory.db'
db = SQLAlchemy(app)

class Item(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    serial_number = db.Column(db.String(50), nullable=False)
    purchase_date = db.Column(db.String(10), nullable=False)
    warranty_expiry = db.Column(db.String(10), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), nullable=False)
    barcode = db.Column(db.String(100), unique=True, nullable=False)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    barcode = request.form['barcode']
    item = Item.query.filter_by(barcode=barcode).first()
    if item:
        return jsonify({
            'name': item.name,
            'description': item.description,
            'category': item.category,
            'serial_number': item.serial_number,
            'purchase_date': item.purchase_date,
            'warranty_expiry': item.warranty_expiry,
            'location': item.location,
            'status': item.status
        })
    else:
        return jsonify({'error': 'Item not found'}), 404

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)
