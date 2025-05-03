from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector

app = Flask(__name__)
CORS(app)

# Configure MariaDB connection
db = mysql.connector.connect(
    host="localhost",
    user="your_user",
    password="your_password",
    database="solo_leveling_db"
)
cursor = db.cursor(dictionary=True)

@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s", (data['username'], data['password']))
    user = cursor.fetchone()
    return jsonify(user if user else {"error": "Invalid credentials"})

@app.route('/api/quests', methods=['GET'])
def get_quests():
    cursor.execute("SELECT * FROM quests")
    quests = cursor.fetchall()
    return jsonify(quests)

if __name__ == '__main__':
    app.run(debug=True)
