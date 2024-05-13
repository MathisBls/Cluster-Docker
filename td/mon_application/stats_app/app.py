from flask import Flask, render_template
import psycopg2

app = Flask(__name__)

def get_click_count():
    conn = psycopg2.connect(
        host="db",
        database="mon_app",
        user="user",
        password="password"
    )
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM clics")
    count = cur.fetchone()[0]
    cur.close()
    conn.close()
    return count

@app.route('/')
def index():
    count = get_click_count()
    return render_template('index.html', count=count)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)
