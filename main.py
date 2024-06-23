from flask import Flask
import random

app = Flask(__name__)

facts_list=["La mayoría de las personas que sufren adicción tecnológica experimentan un fuerte estrés cuando se encuentran fuera del área de cobertura de la red o no pueden utilizar sus dispositivos","Según un estudio realizado en 2018, más del 50% de las personas de entre 18 y 34 años se consideran dependientes de sus smartphones","El estudio de la dependencia tecnológica es una de las áreas más relevantes de la investigación científica moderna","Según un estudio de 2019, más del 60% de las personas responden a mensajes de trabajo en sus smartphones en los 15 minutos siguientes a salir del trabajo", "Una forma de combatir la dependencia tecnológica es buscar actividades que aporten placer y mejoren el estado de ánimo", "Elon Musk afirma que las redes sociales están diseñadas para mantenernos dentro de la plataforma, para que pasemos el mayor tiempo posible viendo contenidos", "Elon Musk también aboga por la regulación de las redes sociales y la protección de los datos personales de los usuarios. Afirma que las redes sociales recopilan una enorme cantidad de información sobre nosotros, que luego puede utilizarse para manipular nuestros pensamientos y comportamientos", "Las redes sociales tienen aspectos positivos y negativos, y debemos ser conscientes de ambos cuando utilicemos estas plataformas"]

@app.route("/")
def hello_world():
    return '<h1 style="color: red; font-size:50px;">Hello World!</h1><a href="/random_fact">¡Ver un dato aleatorio!</a><br><a href="/Miguel">ir donde migue</a><br><a href="/coin">tirar moneda</a><br><a href="/password">generar password</a>'

@app.route("/Miguel")
def hello_migue():
    return '<h1>Hello Migue!</h1><a href="/Leli">ir donde leli</a><br><a href="/">Volver al mundo</a>'

@app.route("/Leli")
def hello_leli():
    return '<h1>Hello Leli!</h1><a href="/Joshi">ir donde joshi</a><br><a href="/">volver la mundo</a>'

@app.route("/Joshi")
def hello_joshi():
    return '<h1>Hello Joshi!</h1><a href="/">volver la mundo</a>'

@app.route("/random_fact")
def random_fact():
    return f'<p>{random.choice(facts_list)}</p><a href="/">volver la mundo</a>'

@app.route("/coin")
def coin():
    flip = random.randint(0, 1)
    if flip == 0:
        return '<h1>CARA</h1>'
    else:
        return '<h1>SELLO<h1/>'
    
@app.route("/password")
def password():
    contrasena = ""
    caracteres = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
    for _ in range(8):
        contrasena += random.choice(caracteres)
    return '<h1>{contrasena}<h1/>'

    

app.run(debug=True)