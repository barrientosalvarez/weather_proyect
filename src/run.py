'''
Modulo que forma parte del proyecto 'weather_proyect'. Este es un proyecto escolar
realizado para la materia Modelado y Programación.

Hecho por Jorge Miguel Aaron Barrientos Alvarez.
Correo electrónico: jma.barrientos@ciencias.unam
GitHub: @barrientosalvarez.

Este es un proyecto de software libre.

Marzo 2022.
'''


import reader
import cache

from datetime import datetime

"""
Este es el punto de partida de nuestro programa. Primero, se verifica la existencia
de el archivo que tendá nuestro caché. De no ser así, se procede a llamar a la función
'read_and_request' del módulo 'reader' la cual: lee el archivo csv con la información
de los vuelos, hace los request necesarios (omitiendo repetidos) y los guarda en un 
caché local para al finalizar guardar la información del caché local en un archivo 
.json que funcionará como caché global.

En caso de que el archivo con el caché exista, se procede a revisar la hora en la que
el caché fue actualizado por última vez. Si ha pasado más de una hora desde que se 
actualizó por última vez el caché, se procede a hacer nuevos request para todos los 
aeropuertos y a actualizar el caché globlal con la nueva información.

En caso de que el archivo con el caché exista y haya pasado menos de una hora desde
su última actualización, se procederá a acceder a la información del caché para 
mostrarla.
"""
if(cache.check_exist()==False):
    reader.read_and_request()
else:
    if(cache.check_cache_time()):
        reader.read_and_show()
    else:
        reader.read_and_request()



