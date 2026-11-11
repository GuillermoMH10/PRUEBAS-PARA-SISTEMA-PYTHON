import sqlite3
import pymysql
from pymysql.cursors import DictCursor
from config import Config


class Database:
    _mode = None  # 'mysql' o 'sqlite_fallback'

    @classmethod
    def get_connection(cls):
        """Intenta conectar a MySQL con las credenciales configuradas.
        Si el servidor remoto (ej. InfinityFree desde fuera de su red) no responde,
        opera de forma transparente con base local para no interrumpir el uso.
        """
        if cls._mode != 'sqlite_fallback':
            try:
                conn = pymysql.connect(
                    host=Config.MYSQL_HOST,
                    port=Config.MYSQL_PORT,
                    user=Config.MYSQL_USER,
                    password=Config.MYSQL_PASSWORD,
                    database=Config.MYSQL_DATABASE,
                    charset='utf8mb4',
                    cursorclass=DictCursor,
                    connect_timeout=3
                )
                cls._mode = 'mysql'
                return conn, 'mysql'
            except Exception:
                cls._mode = 'sqlite_fallback'

        conn = sqlite3.connect(Config.FALLBACK_SQLITE_PATH)
        conn.row_factory = sqlite3.Row
        return conn, 'sqlite'

    @classmethod
    def init_db(cls):
        conn, engine = cls.get_connection()
        try:
            if engine == 'mysql':
                with conn.cursor() as cursor:
                    cursor.execute("""
                        CREATE TABLE IF NOT EXISTS contactos (
                            id INT AUTO_INCREMENT PRIMARY KEY,
                            nombre VARCHAR(100) NOT NULL,
                            apellido VARCHAR(100) NOT NULL,
                            telefono VARCHAR(30) NOT NULL,
                            correo VARCHAR(150) NOT NULL,
                            creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                        ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
                    """)
                conn.commit()
            else:
                conn.execute("""
                    CREATE TABLE IF NOT EXISTS contactos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nombre TEXT NOT NULL,
                        apellido TEXT NOT NULL,
                        telefono TEXT NOT NULL,
                        correo TEXT NOT NULL,
                        creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
                """)
                conn.commit()
        finally:
            conn.close()
