from flask import Flask, request, jsonify
from flask_mysqldb import MySQL
from flask_cors import CORS
from config import DB_CONFIG

app = Flask(__name__)
CORS(app)

# Load DB config
app.config.update(DB_CONFIG)
mysql = MySQL(app)

@app.route('/')
def home():
    return "Solo Leveling Habit Tracker API is running!"

@app.route('/get_stats', methods=['GET'])
def get_stats():
    username = request.args.get('username')
    cur = mysql.connection.cursor()
    cur.execute("SELECT level, xp FROM users WHERE username = %s", (username,))
    result = cur.fetchone()
    cur.close()

    if result:
        return jsonify({'username': username, 'level': result[0], 'xp': result[1]})
    else:
        return jsonify({'error': 'User not found'}), 404

@app.route('/update_stats', methods=['POST'])
def update_stats():
    data = request.json
    username = data.get('username')
    level = data.get('level')
    xp = data.get('xp')

    cur = mysql.connection.cursor()
    cur.execute("INSERT INTO users (username, level, xp) VALUES (%s, %s, %s) ON DUPLICATE KEY UPDATE level=%s, xp=%s",
                (username, level, xp, level, xp))
    mysql.connection.commit()
    cur.close()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)