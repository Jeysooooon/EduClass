import os

from dotenv import load_dotenv
from flask import Flask, render_template

from bpdocentes import bp_docentes
from bpestudiantes import bp_estudiantes
from db import get_database_uri
from models import db

load_dotenv()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "educlass-dev-key")
app.config["SQLALCHEMY_DATABASE_URI"] = get_database_uri()
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)
app.register_blueprint(bp_estudiantes)
app.register_blueprint(bp_docentes)


@app.route("/")
def index():
    return render_template("index.html")
