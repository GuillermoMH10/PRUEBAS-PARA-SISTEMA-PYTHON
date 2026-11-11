import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-213141')
    
    # Configuración de Base de Datos MySQL (FreeDB.tech)
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sql.freedb.tech')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER = os.environ.get('MYSQL_USER', 'u_W1vnWM')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'kH33KGMR5fI9')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'freedb_o8WFZ0gt')
    
    FALLBACK_SQLITE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local_backup.db')
