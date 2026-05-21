from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hola():
	return render_template('index.html')

@app.route('/nombre/')
def nombre():
	return render_template('nombre.html')

@app.route('/carrera/')
def carrera():
	return render_template('carrera.html')
