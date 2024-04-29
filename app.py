from flask_bootstrap import Bootstrap5
from flask import Flask, render_template, request

app = Flask(__name__)

bootstrap = Bootstrap5(app)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nombre = request.form.get("nombre")
        edad = request.form.get("edad")
        ciudad_de_residencia = request.form.get("ciudad de residencia")
        saludo1 = "\n¡Hola, {}, de {}! Bienvenido a la Universidad de Málaga.".format(nombre, ciudad_de_residencia)
        saludo2 = f"\nDisfruta estudiando aquí. Sólo tienes {edad} años y toda una vida por delante."
        return render_template("resultado2.html", nombre=nombre, edad=edad, ciudad_de_residencia=ciudad_de_residencia, saludo1=saludo1, saludo2=saludo2)

        
    return render_template("index2.html")

if __name__ == "__main__":
    app.run(debug=True, port=5000)