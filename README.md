# WebStore - Sistema de Ventas

Este proyecto está diseñado para llevar el control de las ventas, clientes e inventario pudiendo mejorar la calidad de un negocio.

Para poder instalar este proyecto en su ordenador deberá seguir unos ciertos pasos primero. Descuide, lo explicaré a detalle para que no se pierda.

## Guía de instalación 
 Primero instalaremos el framework flask. Ejecute la siguiente línea de código en la terminal.

```
    pip install Flask
```
Ahora requerimos de una librería para usar una base de datos MySQL
```
    pip install Flask-pymysql
```
También requerimos de la base de datos. En este caso 
```
pip install Flask-SQLAlchemy
```

Ahora deberá crear manualmente la base de datos en su **gestor de base de datos.** Puede usar rápidamente la siguiente línea de código para crearla.
```
create database (Coloque aquí el nombre de la base de datos)
```

Haga los respectivos cambios en la configuración de la base de datos. Deberá dirigirse primero al archivo **config.py**. Cambie la contraseña, el usuario, coloque el nombre de la base de datos creada

## Ejecución del sistema
Por último ejecutamos el servidor en la consola con el siguiente comando:
```
python app.py
```

© Roberto_X