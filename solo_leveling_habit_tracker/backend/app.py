from flask import Flask, request, jsonify, send_from_directory
from flask_mysqldb import MySQL
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# MySQL Configuration
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '123'
app.config['MYSQL_DB'] = 'solo_leveling'

mysql = MySQL(app)

# Serve index.html
@app.route('/')
def serve_index():
    return send_from_directory('../frontend', 'solo-leveling-website.html')

# Serve JS
@app.route('/script.js')
def serve_script():
    return send_from_directory('../frontend', 'script.js')

# Save user progress (XP, level)
@app.route('/api/progress', methods=['POST'])
def save_progress():
    data = request.get_json()
    username = data.get('username', 'default_user')
    xp = data['xp']
    level = data['level']

    cursor = mysql.connection.cursor()
    cursor.execute("""
        INSERT INTO users (username, xp, level)
        VALUES (%s, %s, %s)
        ON DUPLICATE KEY UPDATE xp=%s, level=%s
    """, (username, xp, level, xp, level))
    mysql.connection.commit()
    cursor.close()

    return jsonify({"status": "success"})

# Load progress
@app.route('/api/progress/<username>', methods=['GET'])
def load_progress(username):
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT xp, level FROM users WHERE username=%s", (username,))
    result = cursor.fetchone()
    cursor.close()

    if result:
        return jsonify({"xp": result[0], "level": result[1]})
    else:
        return jsonify({"xp": 0, "level": 1})

if __name__ == '__main__':
    app.run(debug=True)
