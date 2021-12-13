class Config:
    # Configuración base
    DEBUG = True
    TESTING = True


    # Configuración de Base de Datos
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:admin@localhost:3306/crm_proyecto"

# Esto es para el modo producción, es decir cuando publicamos el sistema en la web
class productionConfig(Config):
    DEBUG = False

# Esto es para el modo de desarrollo, cuando estemos programando.
class DevelopmentConfig(Config):
    DEBUG = True
    TESTING = True
    