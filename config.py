import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-213141')
    
    # Configuración de Base de Datos MySQL (AwardSpace / Remota)
    # Puedes definir MYSQL_HOST en las variables de entorno de Render si cambia el nodo (ej. fdb1030.awardspace.net)
    MYSQL_HOST = os.environ.get('MYSQL_HOST', 'fdb1030.awardspace.net')
    MYSQL_PORT = int(os.environ.get('MYSQL_PORT', 3306))
    MYSQL_USER = os.environ.get('MYSQL_USER', '4518892_pruebasdepython')
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'Memo1234.')
    MYSQL_DATABASE = os.environ.get('MYSQL_DATABASE', '4518892_pruebasdepython')
    
    # Respaldo local automático si el servidor remoto bloquea conexiones externas
    FALLBACK_SQLITE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'local_backup.db')
