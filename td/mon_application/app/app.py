from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

def add_entry():
    conn = psycopg2.connect(
        host="db",  # Nom du service de la base de données dans docker-compose
        database="mon_app",  # Nom de la base de données
        user="user",  # Utilisateur
        password="password")  # Mot de passe
    cur = conn.cursor()
    cur.execute("INSERT INTO clics (texte) VALUES ('Clic')")
    conn.commit()
    cur.close()
    conn.close()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        add_entry()
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
