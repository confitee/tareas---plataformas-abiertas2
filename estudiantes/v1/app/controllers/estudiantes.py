from flask import Blueprint, jsonify, request

estudiantes_endpoints = Blueprint("estudiantes_endpoints", __name__)


@estudiantes_endpoints.get("/")
@estudiantes_endpoints.get("/hola")
def hola():
    return jsonify({"message": "¡Bienvenido a la API de estudiantes!"}), 200


@estudiantes_endpoints.get("/saludo")
def saludar():
    nombre = request.args.get("nombre", "").strip()
    if not nombre:
        return jsonify({"error": "Debe de ingresar el nombre del estudiante."}), 400

    return jsonify({"saludo": f"Hola {nombre}"}), 200
