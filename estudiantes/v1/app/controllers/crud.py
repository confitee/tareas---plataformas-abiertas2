from flask import Blueprint, jsonify, request

crud_endpoints = Blueprint("crud_endpoints", __name__)


@crud_endpoints.get("/estudiantes")
def obtener_estudiantes():
    return jsonify(
        {
            "mensaje": "Lista de estudiantes obtenida correctamente.",
            "estudiantes": ["Ana", "Carlos", "María"],
        }
    ), 200


@crud_endpoints.post("/estudiantes")
def agregar_estudiante():
    data = request.get_json(silent=True) or {}
    nombre = data.get("nombre")
    if not isinstance(nombre, str) or not nombre.strip():
        return jsonify({"error": "Debe enviar un nombre de estudiante en formato JSON."}), 400

    return jsonify(
        {
            "mensaje": "Estudiante agregado correctamente.",
            "estudiante": nombre.strip(),
        }
    ), 201


@crud_endpoints.put("/estudiantes/<int:student_id>")
def actualizar_estudiante(student_id):
    data = request.get_json(silent=True) or {}
    nombre = data.get("nombre")
    if not isinstance(nombre, str) or not nombre.strip():
        return jsonify({"error": "Debe enviar un nombre de estudiante en formato JSON."}), 400

    return jsonify(
        {
            "mensaje": "Estudiante actualizado correctamente.",
            "id": student_id,
        }
    ), 200


@crud_endpoints.delete("/estudiantes/<int:student_id>")
def eliminar_estudiante(student_id):
    return jsonify(
        {
            "mensaje": "Estudiante eliminado correctamente.",
            "id": student_id,
        }
    ), 200
