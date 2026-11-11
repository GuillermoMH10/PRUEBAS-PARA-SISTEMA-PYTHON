import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-213141')
    
    # Configuración de Base de Datos MySQL (FreeDB.tech)
    # Soporta tanto DB_* como MYSQL_*
    MYSQL_HOST = os.environ.get('DB_HOST') or os.environ.get('MYSQL_HOST') or 'sql.freedb.tech'
    MYSQL_PORT = int(os.environ.get('DB_PORT') or os.environ.get('MYSQL_PORT') or 3306)
    MYSQL_USER = os.environ.get('DB_USERNAME') or os.environ.get('MYSQL_USER') or 'u_W1vnWM'
    MYSQL_PASSWORD = os.environ.get('DB_PASSWORD') or os.environ.get('MYSQL_PASSWORD') or 'kH33KGMR5fI9'
    MYSQL_DATABASE = os.environ.get('DB_DATABASE') or os.environ.get('MYSQL_DATABASE') or 'freedb_o8WFZ0gt'
