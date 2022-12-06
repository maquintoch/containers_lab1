from datetime import datetime
from time import sleep

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///honeypot.sqlite3'
db = SQLAlchemy(app)


class Honey(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    address = db.Column(db.String(80), nullable=False)
    user = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String(80), nullable=False)
    date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


db.create_all()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():

    sleep(2)

    if request.method == 'GET':
        return render_template('login.html')

    db.session.add(
        Honey(
            address=request.remote_addr,
            user=request.form.get('user'),
            password=request.form.get('password')
        )
    )
    db.session.commit()

    return render_template('invalid.html')


@app.route('/honey')
def honey():
    return render_template('honey.html', attempts=Honey.query.all())
