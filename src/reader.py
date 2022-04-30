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
import request
import cache


def read_and_request():
    """
    Esta funcion primero lee dos archivos: un archivo txt que contiene una llave 
    para hacer los request y el archivo csv con la información de los vuelos. Una
    vez abiertos estos archivos, se procede a hacer los request con la función
    'weather_request' del modulo 'request'. Para hacer los request, accedemos a 
    información específica de latitud y longitud de los aeropuertos de origen y 
    destino, esto línea por línea. 
    
    La función cuenta con un cache local llamado 'de_cache' (como el mapa), la cual
    nos permite no hacer request repetidas. Al finalizar todos los request, dicho
    caché local se 'imprime' en el archivo .json que funcionará como caché global.

    Sobre los request: estos se hacen de manera individual: por un lado se hace el
    request del origen y se guarda en el caché, e, independientemente, se hace el 
    request del destino y se guarda en el caché. Guardar información por aeropuertos
    y no por vuelos es muy conveniente. Así, por ejemplo, si el i-ésimo vuelo es uno 
    de MEX a MTY, y nuestro i+1-ésimo vuelo es uno de MTY a TLC, cuando lleguemos
    a hacer los request del i+1-ésimo vuelo no tendremos que pedir información de
    ambos aeropuertos, en ese caso sería unicamente del TLC ya que la información
    del MTY ya la tendríamos en nuestro caché local.

    Nota: a esta función se accede unicamente si: 1) el archivo .json que funciona
    como caché global no existe, o 2) si ha pasado más de una hora de la última 
    actualización del caché global (el caché tiene tiempo de vida de una hora)
    """
    with open('data/api_key.txt') as key_file:
        api_key=key_file.readline()
        api_key=api_key.rstrip()

    with open('data/dataset1.csv') as file:
        reader=csv.reader(file)

        next(reader)

        de_cache={}

        for row in reader: 
            origin_id=row[0]
            destination_id=row[1]

            if origin_id not in de_cache:
                de_cache[origin_id]=request.weather_request(row[2], row[3], api_key)

            if destination_id not in de_cache:
                de_cache[destination_id]=request.weather_request(row[4], row[5], api_key)

            print("\n\nOrigin: ", origin_id, "\n", de_cache[origin_id])
            print("\nDestination: ", destination_id, "\n", de_cache[destination_id])


        cache.primitive_caching(de_cache)
    

def read_and_show():
    """
    Esta función nos permite primero leer el csv con la información de los vuelos
    para posteriormente mostrar la información climatológica de los aeropuertos de 
    dichos vuelos que tenemos en nuestro archivo .json que funciona como caché global.

    Nota: a esta función se accede unicamente si: 1) el archivo .json que funciona
    como caché globla existe (que exista implica que contiene información, así está
    diseñado el proyecto) y 2) ha pasado menos de una hora desde que el archivo .json
    que funciona como caché global fue actualizado por última vez (el caché del
    tiene tiempo de vida de una hora)
    """
    with open('data/dataset1.csv') as file:
        reader=csv.reader(file)
        next(reader)

        for row in reader:
            origin_id=row[0]
            destination_id=row[1]
            cache.show(origin_id, destination_id)


    



