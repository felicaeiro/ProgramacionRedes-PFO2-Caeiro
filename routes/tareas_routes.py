from flask import Blueprint

tareas_bp = Blueprint("tareas", __name__)


@tareas_bp.route("/tareas", methods=["GET"])
def tareas():

    return """
    <h1>Bienvenido al Sistema de Gestión de Tareas</h1>
    <p>La API está funcionando correctamente.</p>
    """