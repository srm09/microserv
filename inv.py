from flask import Flask
from flask import jsonify
from flask import request

app = Flask(__name__)

VERSION = "1.0"

@app.route("/")
def version():
	"Root API version"
	return jsonify(version=VERSION)
