# Importamos de la carpeta webpersonal app. App es donde tendrá todas las especificaciones necesarias. 
# Todo esto está definido en el __init__
from webpersonal import app

# Corre el servidor
if __name__ == '__main__':
    app.run()