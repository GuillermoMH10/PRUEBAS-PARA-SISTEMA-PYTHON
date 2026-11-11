import sqlite3
import pymysql
from pymysql.cursors import DictCursor
from config import Config


class Database:
    @classmethod
    def get_connection(cls):
        """Conecta directamente a MySQL remoto en cada operación."""
        try:
            conn = pymysql.connect(
                host=Config.MYSQL_HOST,
                port=Config.MYSQL_PORT,
                user=Config.MYSQL_USER,
                password=Config.MYSQL_PASSWORD,
                database=Config.MYSQL_DATABASE,
                charset='utf8mb4',
                cursorclass=DictCursor,
                connect_timeout=10
            )
            return conn, 'mysql'
        except Exception:
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
