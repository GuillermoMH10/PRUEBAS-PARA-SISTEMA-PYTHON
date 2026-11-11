from app.database.connection import Database


class ContactoModel:
    @staticmethod
    def listar_todos():
        conn, engine = Database.get_connection()
        try:
            sql = "SELECT id, nombre, apellido, telefono, correo FROM contactos ORDER BY id DESC"
            if engine == 'mysql':
                with conn.cursor() as cursor:
                    cursor.execute(sql)
                    return cursor.fetchall()
            else:
                cursor = conn.execute(sql)
                return [dict(row) for row in cursor.fetchall()]
        finally:
            conn.close()

    @staticmethod
    def obtener_por_id(contacto_id):
        conn, engine = Database.get_connection()
        try:
            if engine == 'mysql':
                with conn.cursor() as cursor:
                    cursor.execute(
                        "SELECT id, nombre, apellido, telefono, correo FROM contactos WHERE id = %s",
                        (contacto_id,)
                    )
                    return cursor.fetchone()
            else:
                cursor = conn.execute(
                    "SELECT id, nombre, apellido, telefono, correo FROM contactos WHERE id = ?",
                    (contacto_id,)
                )
                row = cursor.fetchone()
                return dict(row) if row else None
        finally:
            conn.close()

    @staticmethod
    def crear(nombre, apellido, telefono, correo):
        conn, engine = Database.get_connection()
        try:
            if engine == 'mysql':
                with conn.cursor() as cursor:
                    cursor.execute(
                        "INSERT INTO contactos (nombre, apellido, telefono, correo) VALUES (%s, %s, %s, %s)",
                        (nombre, apellido, telefono, correo)
                    )
                    conn.commit()
                    return cursor.lastrowid
            else:
                cursor = conn.execute(
                    "INSERT INTO contactos (nombre, apellido, telefono, correo) VALUES (?, ?, ?, ?)",
                    (nombre, apellido, telefono, correo)
                )
                conn.commit()
                return cursor.lastrowid
        finally:
            conn.close()

    @staticmethod
    def actualizar(contacto_id, nombre, apellido, telefono, correo):
        conn, engine = Database.get_connection()
        try:
            if engine == 'mysql':
                with conn.cursor() as cursor:
                    cursor.execute(
                        """UPDATE contactos
                           SET nombre = %s, apellido = %s, telefono = %s, correo = %s
                           WHERE id = %s""",
                        (nombre, apellido, telefono, correo, contacto_id)
                    )
                    conn.commit()
                    return cursor.rowcount > 0
            else:
                cursor = conn.execute(
                    """UPDATE contactos
                       SET nombre = ?, apellido = ?, telefono = ?, correo = ?
                       WHERE id = ?""",
                    (nombre, apellido, telefono, correo, contacto_id)
                )
                conn.commit()
                return cursor.rowcount > 0
        finally:
            conn.close()

    @staticmethod
    def eliminar(contacto_id):
        conn, engine = Database.get_connection()
        try:
            if engine == 'mysql':
                with conn.cursor() as cursor:
                    cursor.execute("DELETE FROM contactos WHERE id = %s", (contacto_id,))
                    conn.commit()
                    return cursor.rowcount > 0
            else:
                cursor = conn.execute("DELETE FROM contactos WHERE id = ?", (contacto_id,))
                conn.commit()
                return cursor.rowcount > 0
        finally:
            conn.close()
