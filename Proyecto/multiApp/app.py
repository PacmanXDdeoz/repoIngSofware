from flask import Flask, request, render_template, redirect
from database import getConnection

app = Flask(__name__)

con = getConnection()
cursor = con.cursor()

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/marcas')
def marcas():
	cursor.execute('select * from marcas')
	consulta = cursor.fetchall()
	return render_template('marcas.html', data=consulta)

@app.route('/empleados')
def empleados():
	cursor.execute('select * from empleados')
	consulta = cursor.fetchall()
	return render_template('empleados.html', data=consulta)

@app.route('/productos')
def productos():
	cursor.execute('select * from productos')
	consulta = cursor.fetchall()
	return render_template('productos.html', data=consulta)

@app.route('/marcas/form', methods=['POST'])
def marcasForm():
	marca = request.form['marca']
	cursor.execute('insert into marcas (marca) values (%s)', (marca,))
	con.commit()
	return redirect('/marcas')

@app.route('/empleados/form', methods=['POST'])
def empleadosForm():
	empleado = request.form['empleado']
	puesto = request.form['puesto']
	cursor.execute('insert into empleados (nombre, puesto) values (%s, %s)', (empleado, puesto))
	con.commit()
	return redirect('/empleados')

@app.route('/productos/form', methods=['POST'])
def productosForm():
	producto = request.form['producto']
	precio = requesto.form['precio']
	cursor.execute('insert into productos (producto, precio) values (%s, %s)', (producto, precio))
	con.commit()
	return redirect('/productos')
