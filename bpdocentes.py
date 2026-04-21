from flask import Blueprint, flash, redirect, render_template, request, url_for

from db import get_db_connection

bp_docentes = Blueprint("docente", __name__, url_prefix="/docente")


def obtener_docente(codigo):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Docente WHERE DocCodigo = %s", (codigo,))
        return cursor.fetchone()
    finally:
        cursor.close()
        conn.close()


@bp_docentes.route("/")
def index():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM Docente ORDER BY DocCodigo ASC")
        datos = cursor.fetchall()
    finally:
        cursor.close()
        conn.close()

    return render_template("docente/index.html", lista_docentes=datos)


@bp_docentes.route("/agregar", methods=["GET", "POST"])
def agregar():
    if request.method == "POST":
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                INSERT INTO Docente (
                    DocNombre,
                    DocApellido,
                    DocEspecialidad,
                    DocTelefono
                ) VALUES (%s, %s, %s, %s)
                """,
                (
                    request.form["DocNombre"].strip(),
                    request.form["DocApellido"].strip(),
                    request.form["DocEspecialidad"].strip(),
                    request.form.get("DocTelefono", "").strip(),
                ),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

        flash("Docente agregado correctamente.", "success")
        return redirect(url_for("docente.index"))

    return render_template("docente/agregar.html")


@bp_docentes.route("/editar/<int:codigo>", methods=["GET", "POST"])
def editar(codigo):
    docente = obtener_docente(codigo)
    if docente is None:
        flash("No se encontro el docente solicitado.", "warning")
        return redirect(url_for("docente.index"))

    if request.method == "POST":
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                """
                UPDATE Docente
                SET DocNombre = %s,
                    DocApellido = %s,
                    DocEspecialidad = %s,
                    DocTelefono = %s
                WHERE DocCodigo = %s
                """,
                (
                    request.form["DocNombre"].strip(),
                    request.form["DocApellido"].strip(),
                    request.form["DocEspecialidad"].strip(),
                    request.form.get("DocTelefono", "").strip(),
                    codigo,
                ),
            )
            conn.commit()
        finally:
            cursor.close()
            conn.close()

        flash("Docente actualizado correctamente.", "info")
        return redirect(url_for("docente.index"))

    return render_template("docente/editar.html", docente=docente)


@bp_docentes.route("/eliminar/<int:codigo>", methods=["GET", "POST"])
def eliminar(codigo):
    docente = obtener_docente(codigo)
    if docente is None:
        flash("No se encontro el docente solicitado.", "warning")
        return redirect(url_for("docente.index"))

    if request.method == "POST":
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("DELETE FROM Docente WHERE DocCodigo = %s", (codigo,))
            conn.commit()
        finally:
            cursor.close()
            conn.close()

        flash("Docente eliminado correctamente.", "danger")
        return redirect(url_for("docente.index"))

    return render_template("docente/eliminar.html", docente=docente)
