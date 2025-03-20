from flask import Flask, request, jsonify
from database import db_session  # Import the session
from model import DataModel  # Import the model

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"

@app.route('/')
def home():
    return "Hello, Flask!"

# Create
@app.route("/create_data_entry", methods=["POST"])
def create_entry():
    data = request.get_json()

    dataModel = DataModel(**{key: data.get(key) for key in ["first_name", "last_name", "message", "email"]})

    try:
        db_session.add(dataModel)
        db_session.commit()
        return jsonify({"message": "Successfully created data entry!"}), 201
    except Exception as e: 
        db_session.rollback()
        return jsonify({"message": str(e)}), 500

# Read
@app.route("/retrieve_data", methods=["GET"])
def retrieve_data():
    data = request.get_json()
    

# Update
@app.route("/update_data", methods=["PATCH"])
def update_data():
    pass

# Delete
@app.route("/delete_data", methods=["DELETE"])
def delete_data():
    pass


if __name__ == '__main__':
    app.run(debug=True)