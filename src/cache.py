'''
Modulo que forma parte del proyecto 'weather_proyect'. Este es un proyecto escolar
realizado para la materia Modelado y Programación.

Hecho por Jorge Miguel Aaron Barrientos Alvarez.
Correo electrónico: jma.barrientos@ciencias.unam
GitHub: @barrientosalvarez.

Este es un proyecto de software libre.

Marzo 2022.
'''


import csv
import os.path
import json

from datetime import datetime


def check_exist():
    """
    Esta funcion nos permite verificar si el archivo .json donde se encuentra 
    el caché existe. La función regresa 'True', si en efecto existe. 'False' en
    otro caso
    """
    return os.path.exists('data/cache/_cache_.json')

def check_cache_time():
    """
    Función que nos permite saber a qué hora fue llenado por última vez el caché.
    La función verifica el dato 'hour' en el archivo .json del caché y regresa
    dicho valor. Esta función es necesaria para darle tiempo de vida al caché.
    A pesar de que funciona, la función no está completa, ya que sólo se regresa
    el valor de la hora en la que fue llenado el caché, y para que el tiempo de vida
    sea de una hora es también necesario regresar el valor de los minutos en los que
    se llenó el caché
    """
    with open('data/cache/_cache_.json') as f:
        now=datetime.now()
        current_time={
            'hour': now.strftime("%H"),
            'minutes': now.strftime("%M")
        }

        data=json.load(f)
        buff=data['time']

        if(buff['hour']==current_time['hour']):
            return True;

        elif(current_time['minutes']>=buff['minutes']):
            return False;

        else:
            return True;
        


def primitive_caching(data):
    """
    Esta función recive un data que es .json y lo va imprimiendo en el archivo
    que tendrá nuestro caché. Dicho .json contiene la información meteorológica 
    (no repetida) de los distintos orígenes y destinos por separado. Justo antes
    de imprimir el data en el archivo, se le agrega también la hora actual, ya que
    ésta es la hora en la que se llenó dicho caché.
    """
    with open('data/cache/_cache_.json', 'w', encoding='utf-8') as f:
        now=datetime.now()
        data['time']={
            'hour':now.strftime("%H"),
            'minutes':now.strftime("%M")
        }
        json.dump(data, f)


def show(origin_id, destination_id):
    """
    Esta función nos permite abrir un archivo .json que contiene nuestro caché para
    imprimir su información. La función recive dos parámetros, los cuales corresponden
    a las llaves de la información climatológica de los aeropuertos de un vuelo:
    origen y destino.
    """
    f=open('data/cache/_cache_.json', 'r')
    data=json.loads(f.read())
    
    print("\n\nOrigin: ", origin_id, "\n", data[origin_id])
    print("\nDestination: ", destination_id, "\n", data[destination_id])


