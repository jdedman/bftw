from flask import Flask, jsonify


app = Flask (__name__)


@app.route('/')
def hello():
	data = {
		'id': 1,
		'name' : 'Mi Cancion'
	}
	
	return jsonify(data)

if __name__ == '__main__':
	app.run(host='0.0.0.0')