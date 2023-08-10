from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///crud.db'
db = SQLAlchemy(app)

class Entry(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)

# Move db.create_all() inside the app context block
with app.app_context():
    db.create_all()

# Create operation
@app.route('/create', methods=['POST'])
def create():
    new_entry = Entry(name=request.json["name"], age=request.json["age"])
    db.session.add(new_entry)
    db.session.commit()
    return jsonify({"message": "Entry created"}), 201

# Read operation (Get all entries)
@app.route('/read', methods=['GET'])
def read_all():
    entries = Entry.query.all()
    result = [{"id": entry.id, "name": entry.name, "age": entry.age} for entry in entries]
    return jsonify(result), 200

# Read operation (Get entry by ID)
@app.route('/read/<int:id>', methods=['GET'])
def read(id):
    entry = Entry.query.get(id)
    if entry:
        return jsonify({"id": entry.id, "name": entry.name, "age": entry.age}), 200
    return jsonify({"message": "Entry not found"}), 404

# Update operation
@app.route('/update/<int:id>', methods=['PUT'])
def update(id):
    entry = Entry.query.get(id)
    if entry:
        entry.name = request.json["name"]
        entry.age = request.json["age"]
        db.session.commit()
        return jsonify({"message": "Entry updated"}), 200
    return jsonify({"message": "Entry not found"}), 404

# Delete operation
@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    entry = Entry.query.get(id)
    if entry:
        db.session.delete(entry)
        db.session.commit()
        return jsonify({"message": "Entry deleted"}), 200
    return jsonify({"message": "Entry not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
