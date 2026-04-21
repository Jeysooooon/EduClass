from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Estudiante(db.Model):
    __tablename__ = "Estudiante"

    EstCodigo = db.Column(db.Integer, primary_key=True)
    EstNombre = db.Column(db.String(100), nullable=False)
    EstApellido = db.Column(db.String(100), nullable=False)
    EstDNI = db.Column(db.String(30), nullable=False)
    EstCorreo = db.Column(db.String(120))

    def actualizar_desde_formulario(self, formulario):
        self.EstNombre = formulario["EstNombre"].strip()
        self.EstApellido = formulario["EstApellido"].strip()
        self.EstDNI = formulario["EstDNI"].strip()
        self.EstCorreo = formulario.get("EstCorreo", "").strip() or None
