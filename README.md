# PROYECTO-1-
Proyecto 1: Web Service

## Semblanza

Día a día miles de personas van y vienen de aeropuertos a aeropuertos, cambiando luego drasticamente de 

zona horaria y clima. El aeropuerto de la Ciudad de México te contrata para una tarea, la cual es entregar 

un informe del clima de la ciudad de salida y laciudad de llegada para tres mil tickets que salen el mismo 

día que se corre el algoritmo. No es interactivo, solo nos interesa el clima.

## Distribución del proyecto.

```bash
.
├── prototiposB
│   ├── src
│   │   ├── cache.py
│   │   ├── data
│   │   │   ├── api_key.txt
│   │   │   ├── cache
│   │   │   └── dataset1.csv
│   │   ├── __init__.py
│   │   ├── reader.py
│   │   ├── request.py
│   │   └── run.py
│   └── test
│       └── test.py
└── README.md

```

## Requisitos de ejecución.

Para ejecutar el proyecto son necesarios los guientes requisitos:

* Compilador de python: para instalarlo en los distintos sistemas operativos, sugerimos llevar acabo la 

  siguiente búsqueda en un navegador web:

```bash
how to install python on <tu sistema operativo>
```
   Para obtener instrucciones específivas. En algunos casos será necesario que, después  de instalar 

   el compilador de python y antes de continuat, se instale 'pip'.Sugerimos realizar una búsqueda similar a 

   la anterior en un navegador web:

```bash
how to install pip on <tu sistema operativo>
```

* Librería requests: una vez teniendo los dos requisitos anteriores, necesitaremos descargar la librería 

  'requests'. Para hacerlo, basta con ejecutar el siguiente comando en la terminal:

```bash
pip install requests
```

* API Key de [OpenWeatherMap](https://openweathermap.org): para el funcionamiento del proyecto es necesario 

 contar con una llave (API key) de [OpenWeatherMap](https://openweathermap.org). Es muy sencillo (y gratis) 

 obtener una. Lo que se tiene que hacer es dar click en  [el siguiente enlce](https://openweathermap.org/api), seleccionar el boton que dice

***Subscribe*** justo abajo del letrero ***Current Weather Data***, para posteriormente seleccionar el botón 

que dice ***Get API key*** abajo del letrero ***Free***. Para casi finalizar tendrás que llenar el formulario 

con tus datos (necesitaras un correo electronico al cual tengas acceso), verificar que tienes más de 16 años, 

aceptar los términos y condiciones y hacer el captcha. Una vez que todo este listo y hayas enviado el formulario 

tendrás que ir al correo electrónico que ingresaste para verificar tu cuenta. Una vez hecho esto, y ya para 

finalizar, necesitas volver a la página de inicio de [OpenWeatherMap](https://openweathermap.org), iniciar seción (si no está

iniciada), y pulsar el botón con tu nombre (éste se encuentra en la parte superior derecha de la web, justo a 

la izquierda del botón ***Support***). Una vez pulsado el botón con tu nombre se desplegará un menú. Selecciona 

la opción ***My API keys***. Te llevará a un nuevo apartado en el que encontrarás bajo un letrero ***key*** una

secuencia alfanumérica. Esa es tu API key. Cópiala y pégala dentro del archivo  ***api_key.txt*** que se encuentra 

dentro de la carpeta ***data*** que a su vez se encuentra dentro de la carpeta ***src*** dentro de la carpeta 

***prototiposB*** (vuelve a revisar la ***Distribución del proyecto***). No olvides guardar el archivo.

## Ejecución.

Si estás usando un sistema operativo Linux tienes que hacer lo siguiente: ir a la  carpeta ***src***, presionar 

click derecho y seleccionar la opción ***Open in terminal***, o ***Abrir en terminal***. Una vez estando en la 

terminal, necesitarás escribir el siguiente comando:

```bash
python run.py
```

y presionar ***Enter***. Iniciará la ejecución del proyecto. Si el comando anterior no funciona, prueba con:

```bash
python3 run.py
```

## Autore
* Barrientos Alvarez Jorge Miguel Aaron    |    jma.barrientos@ciencias.unma.mx 







