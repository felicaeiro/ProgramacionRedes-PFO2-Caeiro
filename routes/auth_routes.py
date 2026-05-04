from flask import Blueprint, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from database import conectar
import sqlite3

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/registro", methods=["POST"])
def registro():

    datos = request.get_json()

    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    if not usuario or not contraseña:
        return jsonify({
            "error": "Faltan datos"
        }), 400

    hash_password = generate_password_hash(contraseña)

    try:
        conn = conectar()
        cursor = conn.cursor()

        cursor.execute("""
        INSERT INTO usuarios (usuario, contraseña)
        VALUES (?, ?)
        """, (usuario, hash_password))

        conn.commit()
        conn.close()

        return jsonify({
            "mensaje": "Usuario registrado correctamente"
        }), 201

    except sqlite3.IntegrityError:
        return jsonify({
            "error": "El usuario ya existe"
        }), 400


@auth_bp.route("/login", methods=["POST"])
def login():

    datos = request.get_json()

    usuario = datos.get("usuario")
    contraseña = datos.get("contraseña")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE usuario = ?
    """, (usuario,))

    usuario_db = cursor.fetchone()

    conn.close()

    if usuario_db is None:
        return jsonify({
            "error": "Usuario no encontrado"
        }), 404

    if check_password_hash(usuario_db["contraseña"], contraseña):
        return jsonify({
            "mensaje": "Login exitoso"
        }), 200

    return jsonify({
        "error": "Contraseña incorrecta"
    }), 401


@auth_bp.route("/usuarios", methods=["GET"])
def usuarios():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT id, usuario FROM usuarios")
    usuarios = cursor.fetchall()

    conn.close()

    resultado = [
        {"id": usuario["id"], "usuario": usuario["usuario"]}
        for usuario in usuarios
    ]

    return jsonify(resultado), 200