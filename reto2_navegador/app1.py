
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

history = []
current_page = None

allowed_pages = [
    "uam.edu.ni",
    "python.org",
    "github.com",
    "josedata.com",
    "daviddata.com"
]

@app.route("/", methods=["GET", "POST"])
def index():
    global current_page

    message = ""

    if request.method == "POST":
        option = request.form.get("option")

        if option == "visit":
            url = request.form.get("url", "").strip().lower()

            if url not in allowed_pages:
                message = "Pestaña equicada"
            else:
                if current_page is not None:
                    history.append(current_page)

                current_page = url
                message = "Página visitada correctamente"

        elif option == "back":
            if len(history) == 0:
                message = "No existen páginas anteriores"
            else:
                current_page = history.pop()
                message = "Regresaste a la página anterior"

        elif option == "current":
            if current_page is None:
                message = "No hay ninguna página abierta"
            else:
                message = "Página actual: " + current_page

    return render_template(
        "index.html",
        current_page=current_page,
        history=list(reversed(history)),
        allowed_pages=allowed_pages,
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
