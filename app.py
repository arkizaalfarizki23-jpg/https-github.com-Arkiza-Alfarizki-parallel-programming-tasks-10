from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# Koneksi ke database MySQL (tabel sudah ada)
app.config['SQLALCHEMY_DATABASE_URI'] = (
    'mysql+pymysql://root:@localhost:3306/kampus'
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Mapping tabel mahasiswa (tanpa create table)
class Mahasiswa(db.Model):
    __tablename__ = 'mahasiswa'
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    prodi = db.Column(db.String(100))

@app.route('/')
def index():
    data = Mahasiswa.query.all()
    return render_template('index.html', rows=data)

if __name__ == '__main__':
    app.run(debug=True)
