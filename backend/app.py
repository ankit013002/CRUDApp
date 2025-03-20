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
    first_name = data.get("first_name")
    last_name = data.get("last_name")
    message = data.get("message")
    email = data.get("email")

    if not first_name or not last_name or not message or not email:
        return (jsonify({"message": "You must include a first name, last name, message, and email"}), 400)

    new_message = MessageModel(first_name = first_name, last_name = last_name, message = message, email = email)
    
    try:
        db.session.add(new_message)
        db.session.commit()
    except Exception as e: 
        db.session.rollback()
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Data entry successfully added!"}), 201

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