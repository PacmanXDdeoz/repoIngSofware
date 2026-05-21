from flask import Flask, render_template, request, redirect
from database import getConnection

app = Flask(__name__)

con = getConnection()
cursor = con.cursor()

@app.route('/')
def main():
	return render_template('index.html')

@app.route('/clientes')
def clientes():
	cursor.execute('select * from cliente')
	result = cursor.fetchall()
	return render_template('cliente.html', data=result, seccion=clientes)

@app.route('/productos')
def productos():
	cursor.execute('select * from productos')
	result = cursor.fetchall()
	return render_template('productos.html', data=result, seccion=productos)

@app.route('/ventas')
def ventas():
	cursor.execute('select v.id, v.codigo, p.nombre, p.precio, v.status from ventas v inner join productos p on v.id = p.id where v.status = True')
	result = cursor.fetchall()
	return render_template('ventas.html', data=result, seccion=ventas)

#ENDPOINTS FORMS-VIEW
@app.route('/registrar/clientes')
def registroC():
	return render_template('registrar_clientes.html')

@app.route('/update/clientes')
def updateC():
	cursor.execute('select * from cliente')
	result = cursor.fetchall()
	return render_template('update_clientes.html', data=result)

#ENDPOINTS FORMS
@app.route('/clientes/form', methods=['POST'])
def regClientes():
	nom = request.form['nombre']
	email = request.form['correo']
	phone = request.form['telefono']
	cursor.execute('insert into cliente (nombre, correo, telefono) values (%s, %s, %s)', (nom, email, phone))
	con.commit()
	return redirect('/clientes')

@app.route('/clientes/update', methods=['POST'])
def updClientes():
	id = request.form['id']
	nom = request.form['nombre']
	email = request.form['correo']
	phone = request.form['telefono']
	status = request.form['status']
	cursor.execute('update cliente set nombre = %s, correo = %s, telefono = %s, status = %s where id = %s', (nom, email, phone, status, id))
	con.commit()
	return redirect('/clientes')

@app.route('/clientes/delete', methods=['POST'])
def delClientes():
	id = request.form['id']
	print(id)
	cursor.execute('update cliente set status = false where id = %s', (id,))
	con.commit()
	return redirect('/clientes')

@app.route('/productos/form', methods=['POST'])
def regVentas():
	import random
	code = f"{random.rendint(0,999999):06d}"
	product = request.form['producto_id']
