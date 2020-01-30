# Agencia de Viajes UCO
  Trabajo Final para la asignatura de Programación Web (PW).
  Trabajo realizado por [Javier Ramírez Quintero](https://github.com/xab1t0)


## Descripción

  Este proyecto está realizado bajo [Django v1.10](https://www.djangoproject.com/) y [Python v2.7](https://www.python.org/download/releases/2.7/)

  AgenciaDeViajesUCO es una agencia de viajes online, donde el usuario podrá ver las ciudades ofertadas, así como, los hoteles disponibles en cada ciudad.

  Es necesario el Registro y el posterior logueo.


## Requisitos

  Es necesario tener instalado [Django v1.10](https://www.djangoproject.com/) y [Python v2.7](https://www.python.org/download/releases/2.7/)

  Además ya que incorpora imágenes necesitamos: [Pillow](http://pillow.readthedocs.io/en/3.1.x/installation.html)
  ```
    pip install Pillow
  ```
  Si necesita crear un Superusuario procederemos:
  ```
    python manage.py createsuperuser
  ```
## Uso

  El uso es bastante sencillo, si el usuario no se registra no podrá reservar hotel, sólo podrá ver las ciudades y hoteles disponibles para cada ciudad.

  Para registrarse es necesario introducir un nombre y UNA CONTRASEÑA CON MÍNIMO DE 8 CARACTERES combinando letras y números.

  Una vez logueado, podrá ver su perfil, reservas (cuando tenga).

  Cuando quiera, podrá realizar la solicitud de reserva de hotel. Posteriormente, la Agencia aceptará la solicitud, y esta aparecerá en la pestaña, Mis Reservas.

  PD.: Para los superusuarios, sólo podrán ver lo mismo que un usuario no registrado, en cambio, si podrá acceder a la Admin de Django.
