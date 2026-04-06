from flask import Flask, request, jsonify
from flask_cors import CORS
import sqlite3

app = Flask(__name__)
CORS(app)

DB = 'jobs.db'


def get_db_connection():
    return sqlite3.connect(DB)

def init_db():
    conn = get_db_connection()
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    company TEXT,
    role TEXT,
    status TEXT
    )''')
    conn.commit()
    conn.close()

init_db()

@app.route('/jobs', methods=['GET'])
def get_jobs():
    try:
        conn = get_db_connection()
        c = conn.cursor()
        jobs = c.execute("SELECT * FROM jobs").fetchall()
        conn.close()
        return jsonify(jobs)
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/jobs', methods=['POST'])
def create_job():
    try:
        data = request.json

        
        if not data.get('company') or not data.get('role'):
            return jsonify({"error": "Company and role required"}), 400

        if data['status'] not in ["Applied", "Interview", "Offer", "Rejected"]:
            return jsonify({"error": "Invalid status"}), 400

        conn = get_db_connection()
        c = conn.cursor()
        c.execute(
            "INSERT INTO jobs (company, role, status) VALUES (?, ?, ?)",
            (data['company'], data['role'], data['status'])
        )
        conn.commit()
        conn.close()

        return jsonify({"message": "Job added"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/jobs/<int:id>', methods=['PUT'])
def update_job(id):
    try:
        data = request.json

        if data['status'] not in ["Applied", "Interview", "Offer", "Rejected"]:
            return jsonify({"error": "Invalid status"}), 400

        conn = get_db_connection()
        c = conn.cursor()
        c.execute("UPDATE jobs SET status=? WHERE id=?", (data['status'], id))
        conn.commit()
        conn.close()

        return jsonify({"message": "Updated"})
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/ai/match', methods=['POST'])
def ai_match():
    return jsonify({
        "score": 80,
        "missing_keywords": ["Docker", "System Design"],
        "suggestions": "Add backend + deployment experience"
    })


if __name__ == "__main__":
    app.run(debug=True)