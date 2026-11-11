from app.database.connection import Database


class ContactoModel:
    @staticmethod
    def listar_todos():
        conn = Database.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("SELECT id, nombre, apellido, telefono, correo FROM contactos ORDER BY id DESC")
                return cursor.fetchall()
        finally:
            conn.close()

    @staticmethod
    def obtener_por_id(contacto_id):
        conn = Database.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "SELECT id, nombre, apellido, telefono, correo FROM contactos WHERE id = %s",
                    (contacto_id,)
                )
                return cursor.fetchone()
        finally:
            conn.close()

    @staticmethod
    def crear(nombre, apellido, telefono, correo):
        conn = Database.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO contactos (nombre, apellido, telefono, correo) VALUES (%s, %s, %s, %s)",
                    (nombre, apellido, telefono, correo)
                )
                return cursor.lastrowid
        finally:
            conn.close()

    @staticmethod
    def actualizar(contacto_id, nombre, apellido, telefono, correo):
        conn = Database.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute(
                    """UPDATE contactos
                       SET nombre = %s, apellido = %s, telefono = %s, correo = %s
                       WHERE id = %s""",
                    (nombre, apellido, telefono, correo, contacto_id)
                )
                return cursor.rowcount >= 0
        finally:
            conn.close()

    @staticmethod
    def eliminar(contacto_id):
        conn = Database.get_connection()
        try:
            with conn.cursor() as cursor:
                cursor.execute("DELETE FROM contactos WHERE id = %s", (contacto_id,))
                return cursor.rowcount > 0
        finally:
            conn.close()
