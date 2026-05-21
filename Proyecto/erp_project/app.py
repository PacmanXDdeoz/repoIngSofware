from flask import Flask, render_template, redirect, request, session
import pdfplumber

from database import getConnection

app = Flask(__name__)
app.config['SECRET_KEY'] = "TIiJbElGh3el7yvdAcTGIGE4kSwXQtCWKxAQmVDgrkOeJKQc3ZbocpFigFgpsH3T"

con=getConnection()
cursor=con.cursor()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/signup_form')
def signup_form():
	return render_template('signup.html')

@app.route('/dashboard')
def main():
	return render_template('main.html')

@app.route('/library')
def library():
	cursor.execute('select * from books')
	result = cursor.fetchall()
	return render_template('library.html', data=result)

@app.route('/read')
def read():
	cursor.execute('select  from books')
	result = cursor.fetchall()
	path = result[5]
	text = ""

	with pdfplumber.open(path) as pdf:
		for pagina in pdf.pages:
			text += pagina.extract_text()+"\n"
	return render_template('read.html', content=text)

# ? FORMS
@app.route('/signup', methods=['POST'])
def signup():
	name=request.form['name']
	ap=request.form['ap']
	user=request.form['username']
	email=request.form['email']
	pas=request.form['pass']
	cursor.execute("insert into users (name, lastname, username, email, password) values (%s, %s, %s, %s, crypt(%s, gen_salt('bf')))", (name, ap, user, email, pas))
	con.commit()
	return redirect('/')

@app.route('/login', methods=['POST'])
def login():
	email=request.form['email']
	pas=request.form['pass']
	cursor.execute("select id from users where email = %s and password = crypt(%s, password)", (email, pas))
	result = cursor.fetchall()
	if result:
		session['id'] = result[0]
		return redirect('/dashboard')
	else:
		return 'Usuario no encontrado'
	return redirect('/')
		
/static/documents/El_que_susurra_en_la_oscuridad-H._P._Lovecraft.pdf