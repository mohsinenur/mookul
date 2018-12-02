from web import app
from flask_sqlalchemy import SQLAlchemy

# Config MySQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:@localhost/mookuldb'
db = SQLAlchemy(app)


class User(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(80), unique=True, nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	phone = db.Column(db.String(20), unique=True, nullable=False)
