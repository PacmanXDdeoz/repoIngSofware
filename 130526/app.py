from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def hello():
    return '¡Bienvenido a nuestra tienda "El emma"!'