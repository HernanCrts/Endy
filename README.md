# Endy
Se trata de una aplicación que se lanza junto a otra que puede tardar un rato (ya sea nmap, dirb, etc) ,al terminar, este te avisará con una notificación por pantalla y un leve sonido.

## Para ejecutar el comando:
     $ python3 endy.py <tarea a realizar>

## Ejemplo
     $ python3 endy.py nmap 192.168.1.0/24 -sV -O

## Información adicional
Recomiendo poner la carpeta Endy en la raíz del sistema (en la configuración del fichero esta ubicada ahí) y crear el siguiente Alias en el fichero de la Shell en uso, quedando de la siguiente forma:

     alias endy='python3 /endy/endy.py'<br>
Para ejecutar el comando una vez hecho el Alias, sería:
