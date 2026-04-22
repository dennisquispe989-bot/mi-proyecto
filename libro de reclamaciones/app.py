from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def formulario():
    return render_template("formulario.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nombre = request.form["nombre"]
    dni = request.form["dni"]
    mensaje = request.form["mensaje"]

    with open("reclamos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre} - {dni}: {mensaje}\n")

    return "Reclamo enviado correctamente ✅"

if __name__ == "__main__":
    app.run(debug=True)
