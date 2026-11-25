
from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)

# MySQL database connection
def get_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="fixora_db"
    )

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/test-db")
def test_db():
    try:
        db = get_db()
        cursor = db.cursor()
        cursor.execute("SHOW TABLES")

        tables = cursor.fetchall()

        cursor.close()
        db.close()

        return {
            "message": "Database connected successfully!",
            "tables": [table[0] for table in tables]
        }

    except Exception as e:
        return {"error": str(e)}, 500

if __name__ == "__main__":
    app.run(debug=True)
