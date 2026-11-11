import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'dev-secret-key-213141')
    
    # Configuración de Base de Datos MySQL (Aiven Cloud)
    MYSQL_HOST = os.environ.get('DB_HOST') or os.environ.get('MYSQL_HOST') or 'pruebaspython-guillemoyeda17-aca7.f.aivencloud.com'
    MYSQL_PORT = int(os.environ.get('DB_PORT') or os.environ.get('MYSQL_PORT') or 10170)
    MYSQL_USER = os.environ.get('DB_USERNAME') or os.environ.get('MYSQL_USER') or 'avnadmin'
    MYSQL_PASSWORD = os.environ.get('DB_PASSWORD') or os.environ.get('MYSQL_PASSWORD') or 'AVNS_0OeIcqBp6_H3T6sE0py'
    MYSQL_DATABASE = os.environ.get('DB_DATABASE') or os.environ.get('MYSQL_DATABASE') or 'defaultdb'
    MYSQL_SSL_REQUIRED = True
