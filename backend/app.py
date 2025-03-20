from flask import Flask, request, jsonify
from config import app,db
from model import MessageModel  # Import the model

@app.route('/')
def home():
    return "Hello, Flask!"

# Create
@app.route("/create_data_entry", methods=["POST"])
def create_entry():
    data = request.get_json()

    dataModel = MessageModel(**{key: data.get(key) for key in ["first_name", "last_name", "message", "email"]})

    try:
        db.add(dataModel)
        db.commit()
        return jsonify({"message": "Successfully created data entry!"}), 201
    except Exception as e: 
        db.rollback()
        return jsonify({"message": str(e)}), 500

# Read
@app.route("/retrieve_data", methods=["GET"])
def retrieve_data():
    messages = MessageModel.query.all()
    json_data = list(map(lambda message: message.to_json(), messages))
    return jsonify({"data": json_data})

# Update
@app.route("/update_data", methods=["PATCH"])
def update_data():
    pass

# Delete
@app.route("/delete_data", methods=["DELETE"])
def delete_data():
    pass


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)