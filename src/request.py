'''
Modulo que forma parte del proyecto 'weather_proyect'. Este es un proyecto escolar
realizado para la materia Modelado y programación.

Hecho por Jorge Miguel Aaron Barrientos Alvarez
Correo electrónico: jma.barrientos@ciencias.unam.mx
GitHub: @barrientosalvarez


Este es un proyecto de software libre.

Marzo 2022.
'''

import requests

def weather_request(lat, lon, api_key):
    """
    Esta función recive tres parámetros: lat, lon y api_key; los cuales consisten
    en un valor de latitud y longitud de un aeropuerto y a una key para hacer los 
    request respectivamente. La api, en esta forma de hacer request, nos regresa
    un json con la información climatológica de un lugar en específico. Los valores
    de dicho json a los que accedimos (y los que regresa la función en forma de json)
    son aquellos que consideramos como los más importantes: temperatur, sensación 
    térmica, temperatura mínima y máxima y porcentaje de humedad.

    Considero pertinente que se revise la documentación que nos da la API para cuando
    se hace un request, así se podrán verificar todos los datos climatológicos que la
    API nos regresa. La documentación puede ser consultada en: https://openweathermap.org/current
    """
    url=f"http://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
    
    r=requests.get(url).json()
    main_temp=str(r['main']['temp'])+" °C"
    main_feels_like=str(r['main']['feels_like'])+" °C"
    main_temp_min=str(r['main']['temp_min'])+" °C "
    main_temp_max=str(r['main']['temp_max'])+" °C "
    main_humidity=str(r['main']['humidity'])+"%"

    return{
        'temperature':main_temp,
        'feels_like':main_feels_like,
        'min_temperature':main_temp_min,
        'max_temperature':main_temp_max,
        'humidity':main_humidity
    }
