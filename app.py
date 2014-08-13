from flask import Flask, jsonify
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask (__name__)

# Initialize Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///soundem.db'
db = SQLAlchemy(app)

#Create class/table in DB
class Artist(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), unique=True)
	bio = db.Column(db.Text)

#Constructor method
	def __init__(self, name, bio=None): 
		self.name = name

		if bio:
			self.bio = bio





@app.route('/')
def hello():
	data = {
		'id': 1,
		'name' : 'Mi Cancion'
	}

	return jsonify(data)

if __name__ == '__main__':
	app.run(host='0.0.0.0')