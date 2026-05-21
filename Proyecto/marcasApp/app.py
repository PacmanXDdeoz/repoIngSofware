from flask import Flask, render_template, redirect, request
from database import getConnection

app = Flask(__name__)

con = getConnection()
cursor = con.cursor()

@app.route('/')
def main():
	cursor.execute('select * from marcas')
	result = cursor.fetchall()
	return render_template('index.html', data=result)

@app.route('/empleados')
def empleados():
	cursor.execute('select * from empleados')
	result = cursor.fetchall()
	return render_template('empleados.html', data=result)

@app.route('/guardar_marca', METHODS=['POST'])
def guardar_marca():
	nom = request.form['nombre']
	cursor.execute("insert into marcas (nombre, status) values (%s, 1);",(nom,))
	con.commit()
	return redirect('/')