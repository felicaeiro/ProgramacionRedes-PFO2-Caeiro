from database import conectar


def crear_usuario(usuario, contraseña):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    INSERT INTO usuarios (usuario, contraseña)
    VALUES (?, ?)
    """, (usuario, contraseña))

    conn.commit()
    conn.close()


def obtener_usuario(usuario):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
    SELECT * FROM usuarios
    WHERE usuario = ?
    """, (usuario,))

    usuario_db = cursor.fetchone()

    conn.close()

    return usuario_db