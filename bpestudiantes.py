from flask import Blueprint, flash, redirect, render_template, request, url_for

from models import Estudiante, db

bp_estudiantes = Blueprint("estudiante", __name__, url_prefix="/estudiante")


@bp_estudiantes.route("/")
def index():
    datos = Estudiante.query.order_by(Estudiante.EstCodigo.asc()).all()
    return render_template("estudiante/index.html", lista_estudiantes=datos)


@bp_estudiantes.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        estudiante = Estudiante()
        estudiante.actualizar_desde_formulario(request.form)
        db.session.add(estudiante)
        db.session.commit()
        flash("Estudiante agregado correctamente.", "success")
        return redirect(url_for("estudiante.index"))

    return render_template("estudiante/agregar.html")


@bp_estudiantes.route("/editar/<int:codigo>", methods=["GET", "POST"])
def editar(codigo):
    estudiante = db.session.get(Estudiante, codigo)
    if estudiante is None:
        flash("No se encontro el estudiante solicitado.", "warning")
        return redirect(url_for("estudiante.index"))

    if request.method == "POST":
        estudiante.actualizar_desde_formulario(request.form)
        db.session.commit()
        flash("Estudiante actualizado correctamente.", "info")
        return redirect(url_for("estudiante.index"))

    return render_template("estudiante/editar.html", estudiante=estudiante)


@bp_estudiantes.route("/eliminar/<int:codigo>", methods=["GET", "POST"])
def eliminar(codigo):
    estudiante = db.session.get(Estudiante, codigo)
    if estudiante is None:
        flash("No se encontro el estudiante solicitado.", "warning")
        return redirect(url_for("estudiante.index"))

    if request.method == "POST":
        db.session.delete(estudiante)
        db.session.commit()
        flash("Estudiante eliminado correctamente.", "danger")
        return redirect(url_for("estudiante.index"))

    return render_template("estudiante/eliminar.html", estudiante=estudiante)
