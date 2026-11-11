import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-213141')
    
    # Configuración de Base de Datos MySQL (InfinityFree)
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'sql307.infinityfree.com')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER = os.environ.get('MYSQL_USER', 'if0_43415220')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Memo213141')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', 'if0_43415220_pruebaspython')
    
    # Respaldo local automático si InfinityFree bloquea conexiones remotas fuera de su red
    FALLBACK_SQLITE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local_backup.db')
