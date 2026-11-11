import pymysql
from pymysql.cursors import DictCursor
from config import Config


class Database:
    @classmethod
    def get_connection(cls):
        """Conecta exclusivamente al servidor MySQL configurado."""
        conn = pymysql.connect(
            host=Config.MYSQL_HOST,
            port=Config.MYSQL_PORT,
            user=Config.MYSQL_USER,
            password=Config.MYSQL_PASSWORD,
            database=Config.MYSQL_DATABASE,
            charset='utf8mb4',
            cursorclass=DictCursor,
            connect_timeout=15,
            autocommit=True
        )
        return conn

    @classmethod
    def init_db(cls):
        conn = cls.get_connection()
        try:
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
        finally:
            conn.close()
