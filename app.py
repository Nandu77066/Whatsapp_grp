from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
from datetime import datetime
import os

app = Flask(__name__)
CORS(app)




MONGO_URI = os.environ.get("mongodb+srv://nandud7967_db_user:77066Nandu@cluster0.tnadqgz.mongodb.net/?appName=Cluster0")

client = MongoClient(MONGO_URI)

db = client["cable_whatsapp"]
collection = db["pending_members"]


@app.route("/")
def home():
    return "Backend Running"


@app.route("/members", methods=["POST"])
def add_member():

    data = request.get_json()

    phone = data.get("phone_number")

    if not phone:
        return jsonify({
            "success": False,
            "message": "Phone number missing"
        }), 400

    collection.insert_one({
        "phone_number": phone,
        "grp": False,
        "created_at": datetime.utcnow()
    })

    return jsonify({
        "success": True,
        "message": "Saved Successfully"
    })


if __name__ == "__main__":
    app.run(debug=True)
