import os
import psycopg2
from flask import Flask, render_template

app = Flask(__name__)

DB_USER = os.environ.get('DB_USER') #postgres
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST') #localhost
DB_PORT = os.environ.get('DB_PORT') #5432
DB_NAME = os.environ.get('DB_NAME') #postgres

def check_db_connection():
    try:
        conn = psycopg2.connect(
            dbname=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            host=DB_HOST,
            port=DB_PORT
        )
        return conn
    except psycopg2.Error as e:
        print(f"Database connection error: {e}")
        return None

def create_table():
    conn = check_db_connection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS clalit (
            id SERIAL PRIMARY KEY,
            value INTEGER
        )
    """)
    conn.commit()
    print("Table 'clalit' created successfully.")
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/insert')
def insert_data():
    conn = check_db_connection()
    if conn:
        cur = conn.cursor()
        for i in range(1, 11):
            cur.execute(f"INSERT INTO clalit (value) VALUES ({i})")
        conn.commit()
        cur.close()
        return 'Test data inserted successfully.'
    else:
        return 'Failed to connect to the database.'

@app.route('/read')
def read_data():
    conn = check_db_connection()
    if conn:
        cur = conn.cursor()
        cur.execute('SELECT * FROM clalit')
        data = cur.fetchall()
        cur.close()

        html_content = "<h1>Read Data</h1>"
        html_content += "<table border='1'><tr><th>ID</th><th>Value</th></tr>"
        for row in data:
            html_content += f"<tr><td>{row[0]}</td><td>{row[1]}</td></tr>"
        html_content += "</table>"

        return html_content
    else:
        return 'Failed to connect to the database.'

@app.route('/readiness')
def readiness():
    if check_db_connection():
        return '', 200
    else:
        return '', 500

@app.route('/liveness')
def liveness():
    if check_db_connection():
        return '', 200
    else:
        return '', 500

if __name__ == '__main__':
    create_table()
    app.run(host='0.0.0.0', port=5000, debug=False)