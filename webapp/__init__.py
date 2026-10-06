"""Application factory: there is no module-level app object and no root app.py."""
from flask import Flask, render_template, request


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        return render_template("index.html")

    @app.route("/about")
    def about():
        return render_template("about.html")

    @app.route("/contact", methods=["GET", "POST"])
    def contact():
        name = request.form.get("name", "").strip() if request.method == "POST" else ""
        return render_template("contact.html", name=name)

    return app
