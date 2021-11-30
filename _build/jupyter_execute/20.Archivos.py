#!/usr/bin/env python
# coding: utf-8

# # Archivos

# :::::{important} ¿Qué aprenderemos?
# 
# 
# Crear y manipular archivos
# 
# ````{tabbed} JSON
# 
# :::{admonition} ¿Qué son?
# :class: tip
# Es un tipo de archivos que permiten almacenar información y su estructura, además son legibles por humanos.
# :::
# ````
# 
# ````{tabbed} CSV
# 
# :::{admonition} ¿Qué son?
# :class: tip 
# Archivos legibles por humanos pero que no mantienen la estructura de los datos.
# :::
# ````
# 
# :::::

# Cuando el programa con el que estamos ejecutando estos cuadernos se cierra, las variables, listas, tuplas, ect, que hemos creado y manipulado se pierden. Es por esto que los archivos toman una gran relevancia, pues perminten mantener la información generada en el largo plazo. Por ello, en el presente cuaderno nos centraremos en la creación, modificación y actualización de archivos.
# 
# La manera en que Python ve un **archivo de texto** es como un arreglo o lista de carácteres, mientras que un **archivo binario** (imágenes, videos, etc.) lo ve como un arreglo de bytes; en ambos casos el primer elemento esta ubicado en la posición 0, es por ello que un archivo con n carácteres o bytes el último elemento esta ubicado en la posición n-1.
# 
# Cada uno de los archivos que se abran en Python generarán un `file object`, el cual permite nuestra interacción con el archivo.
# 
# Cada sistema operativo tiene su propia manera de identificar el final de un archivo, puede ser mediante un marcador específico o mediante el conteo del total de carácteres que tiene el archivo.
# 
# ## Creando un .txt
# Con las siguientes líneas crearemos un archivo con cinco entradas (filas), cada una de ellas contendrá el código de una persona, su apellido y el dinero que adeuda a un pequeño fondo de ahorros: 
# 
# 

# In[1]:


with open('fondo.txt', mode='w') as fondo:
    fondo.write('1 Morales 240000\n')
    fondo.write('2 Rodríguez 578138\n')
    fondo.write('3 Blanco 793000\n')
    fondo.write('4 García 238458\n')
    fondo.write('5 Romero 9125489\n')


# Una forma alternativa de ingresar información al archivo es mediante la siguiente línea de código

# In[2]:


with open('fondo.txt', mode='a') as fondo:
    print('6 Jaimes 275981', file=fondo)


# ### With
# Así como este pequeño bloque de código, muchas de las aplicaciones que como científicos de datos realizarán en un futuro, requieren establecer conecciones a archivos, redes, bases de datos, etc. y siempre se deben liberar los recursos tan pronto como ya no se requieren, esto con el fin de que otras alpicaciones puedan acceder a ellos, es por ello que `with` realiza las siguientes labores:
# 1. Adquiere el recurso (en nuestro ejemplo `fondo.txt`)  y asigna su correspondiente objeto a una variable (`fondo`).
# 2. Permite el uso del recurso mediante la variable (`write` y `print`).
# 3. Invoca al método `close` para liberar el recurso, cuando se alcanza el final del `with`.
# 
# ### Open
# La función `open` abre un archivo (en nuestro ejemplo `fondo.txt`) y le asigna un objeto de archivo. El modo asigna las tareas que se pueden realizar cuando se abre el archivo *leer*, *escrbir*, etc. los posibles modos son:
# 
# |Modo|Tarea|
# |:-:|:-:|
# |"r"|Read: Valor por defecto. Abre un archivo para lectura. Genera error si el archivo no existe|
# |"a"|Append: Abre un archivo para agregarle información, crea el archivo si no existe|
# |"w"|Write: Abre un archivo para escritura, crea el archivo si no existe|
# |"x"|Create: Crea el archivo especificado. Genera error si el archivo existe|
# |"t"|Text: Valor por defecto. El archivo a manipular será de tipo texto|
# |"b"|Binary: El archivo a manipular será de tipo binario|
# |"+"|Update: Abre un archivo para actualizarlo debe estar precedido de `r`, `w` o `a` e indica que el archivo también será para leer y escribir|
# 
# ### Write
# En el ejemplo hemos visto que, con `with` hemos podido asignar el objeto que regresa `open` a la variable `fondo` con la cláusula `as`, dicha variable `fondo` permite la interacción con el archivo. Posteriormente empleamos el método `write` para escribir cinco registros en nuestro archivo, el método tiene como argumento la cadena de carácteres que deseamos incluir en el archivo.

# ## Leyendo archivos
# 
# Con el código que ejecutamos anteriormente, hemos creado un archivo (fondo.txt) en nuestra actual ubicación. Ahora veremos la manera de leer tal información:

# In[3]:


with open('fondo.txt', mode='r') as fondo:
    print(f'{"Código":<10}{"Apellido":<10}{"Balance":>10}')
    for registro in fondo:
        codigo, apellido, balance = registro.split()
        print(f'{codigo:<10}{apellido:<10}{balance:>10}')


# Hemos accedido al archivo con el modo `"r"`, ya que queremos evitar modificaciones accidentales sobre él. La iteración que hemos realizado sobre el objeto que representa al archivo, se hace por cada "registro", es decir, línea por línea y en cada interación lo que hacemos es dividir el texto en "palabras" con el método `split`, y "desempacamos" la cadena con la forma en que almacenamos su contenido en las variables `codigo`, `apellido` y  `balance`. Finalmente imprimimos el texto en columnas de ancho fijo, las cuales están alineadas a la izquierda, las dos primeras y a la derecha la última.
# 
# Otra forma de leer archivos es mediante el método `readlines`, el cual retorna una lista en la cual cada entrada es una línea del documento:

# In[4]:


open('fondo.txt', mode='r').readlines()


# Este método es útil en archivos pequeños, pero cuando se trata de archivos de gran tamaño, es mejor hacer la iteración que mostramos al principio.

# ## Actualizando archivos
# Si en nuestro archivos quisiéramos cambiar el apellido 'Blanco' por el apellido 'Cervantes', el registro original es:
# ```python
# 3 Blanco 793000
# ``` 
# si se sobreescribe el apellido, el nuevo registro sería:
# ```python
# 3 Cervantes3000
# ```
# Esto ocurre por el tamaño del apellido con el que se esta actualizando el registro, tiene tres carácteres más.
# ### Ejercicio
# 1. ¿Qué ideas propone para solucionar este problema?
# 
# Una de las posibles respuestas es:
# 1. Copiar los dos primeros registros en otro archivos.
# 2. Generar la entrada que se desea en el archivo creado.
# 3. Copiar el resto de registros al nuevo.
# 4. Eliminar el archivo viejo.
# 5. Renombrar el nuevo archivo
# 

# In[5]:


with open('fondo.txt', mode='r') as fondo:
    for registro in fondo:
        codigo, apellido, balance = registro.split()
        if apellido == 'Blanco':
            with open('fondo2.txt', mode='a+') as fondo2:
                fondo2.write('3 Cervantes 793000\n')
        else:
            with open('fondo2.txt', mode='a+') as fondo2:
                fondo2.write(registro)            


# Para eliminar y renombrar el nuevo archivo debemos importar la librería `os`, para emplear la función `remove`: la cual como argumento recibe el nombre del archivo que se desea eliminar, y la función `rename`: esta recibe dos argumentos, el primero es el nombre del archivo al que le deseamos cambiar el nombre y el segundo el nombre con el que deseamos se quede tal archivo.

# In[6]:


import os
#os.remove('fondo.txt')
os.rename('fondo2.txt', 'fondo.txt')


# ### Ejercicio
# 1. En el diligenciamento de los datos del fondo a habido un error, los registros 5 y 6 tienen los apellidos intercambiados. Modifica el código anterior para arreglar este asunto (utiliza las variables `codigo` y `balance` durante el proceso).

# ## Serialización con JSON
# Los archivos `JSON (JavaScript Object Notation)` son ampliamente utilizados para serializar y transmitir datos estructurados a través de una conexión de red, es por ello que muchos de los servicios basados en la nube los emplean, además no sólo permiten enviar la estructura de los datos (listas, conjuntos, diccionarios y más), son también legibles por los humanos. 
# 
# Los objetos JSON son similares a los diccionarios en Python, ya que son `property names` y `values` separados por coma entre llaves, así:
# ```python
# {"Código": 1, "Apellido": "Morales", "Balance": 240000}
# ```
# También en los archivos JSON se aceptan arreglos, los cuales son como las listas de Pyhon, valores separados por coma encerrados en corchetes:
# ```python
# [1,2,3,4,5,6]
# ```
# Los valores que se pueden almacenar en dichos arreglos son:
# 1. Carácteres encerrados en comillas dobes ("Morales").
# 2. Números (1 o 2.34).
# 3. Valores Booleanos (`true` y `false`).
# 4. `Null` (equivalente al `None` de Python).
# 5. Arreglos ([1,2,3,4,5,6]).
# 6. Otros objetos JSON.
# 
# La librería `json` nos permite convertir los objetos al formato en que deben estar en un archivo JSON, esta tarea se conoce como **serializar** los datos. Vamos a definir un diccionario en el cual hay una llave llamada `cuenta` a la cual se le asigna un valor, este consiste en una lista de diccionarios que representan dos cuentas. Cada uno de los diccionarios esta conformado por el código, apellido y balance:

# In[7]:


cuentas_dict = {'cuenta': [{'Código': 1, 'Apellido': 'Morales', 'Balance': 240000},
                              {'Código': 2, 'Apellido': 'Rodríguez', 'Balance': 578138}]}


# In[8]:


import json
with open('cuentas.json', 'w') as cuentas:
    json.dump(cuentas_dict, cuentas)


# Si abrimos el archivo que acabamos de crear, lo veremos así:
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/json1.png?raw=true" width="200">
# 
# o así:
# 
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/json2.png?raw=true" width="600">
# 
# 
# Note que las cadenas de texto en JSON van siempre entre comillas dobles.
# 
# 
# 

# La función `dumps` convierte un objeto de Python en objetos de JSON. 

# ### Deserializar
# La función `load`, del paquete `json`, permite leer todo el contenido del archivo que se ingresa como argumento de ella y convertir los objetos tipo JSON a objetos de Python. Este proceso se conoce como deserializar los datos. Vamos a utilizar el ejemplo anterior para reconstruir nuestro diccionario original:

# In[9]:


with open('cuentas.json', 'r') as cuentas:
    cuentas_json = json.load(cuentas)


# Ya hemos almacenado la información del archivo en la variable `cuentas_json`, de modo que podemos interactuar con dicho contenido:

# In[10]:


cuentas_json


# In[11]:


#Acceder al diccionario cuenta:
cuentas_json['cuenta']


# In[12]:


#Acceder a las cuentas individuales:
cuentas_json['cuenta'][0]


# In[13]:


cuentas_json['cuenta'][1]


# Como antes, podemos manipular el diccionario que hemos creado:

# In[14]:


cuentas_json['cuenta'].append({'Código':3,'Apellido': 'Blanco', 'Balance': 793000})
cuentas_json


# Para hacer un *pretty print* de los objetos de JSON, podemos hacer la siguiente combinación de `dumps` y `load`:

# In[15]:


with open('cuentas.json', 'r') as cuentas:
    print(json.dumps(json.load(cuentas), indent=3))


# el argumento adicional que hemos empleado `indent`, se puede utilizar cuando se almacena la información en el archivo. Sirve para dar el tamaño de la sangría a la hora de imprimir la información.

# ## Archivos CSV
# En ciencia de datos es muy común trabajar con archivos CSV (comma-separated values), ya que son legibles por humanos pero tienen la desventaja que no guardan la estructura de la información. El paquete `csv` tiene funciones para trabajar con este tipo de archivos, sin embargo no es el único ya que paquetes como `pandas` tienen sus funciones para manipularlos también.

# In[16]:


import csv


# In[17]:


with open('fondo.csv', mode='w', newline='') as cuentas:
    writer = csv.writer(cuentas)
    writer.writerow([1,'Morales',240000])
    writer.writerow([2,'Rodríguez',578138])
    writer.writerow([3,'Blanco',793000])
    writer.writerow([4,'García',238458])
    writer.writerow([5,'Romero',9125489])
    writer.writerow([6,'Jaimes',275981])


# La función `writer` regresa un objeto que tiene permitido escribir determinado objeto en el archivo.
# 
# Cada llamada que se hace del método `writerow` recibe un iterable el cual se almacenará en el archivo, el separador que se usa por defecto es la coma, pero se puede especificar el delimitador de los valores.
# 
# Para leer archivos CSV, seguimos las mismas ideas de antes:

# In[18]:


with open('fondo.csv', 'r', newline='') as cuentas:
    print(f'{"Código":<10}{"Apellido":<10}{"Balance":>10}')
    reader = csv.reader(cuentas)
    for registro in reader:
        codigo, apellido, balance = registro
        print(f'{codigo:<10}{apellido:<10}{balance:>10}')


# La función `reader` crea un objeto que lee la información almacenada en el archivo tipo CSV. El `for` que está en el bloque de código anterior, permite recorrer uno por uno los registros almacenados en el CSV, y los valores de dichas entradas vienen como una lista, la cual se *desempaca*  en las variables `codigo`, `apellido` y `balance`.
# 
# A la hora de almacenar la información en este tipo de archivos se debe tener mucho cuidado con las comas presentes en los datos, ya que una coma sobrante o faltante modificará el archivo sensiblemente, por ejemplo:
# ```python
# 1,2,3,4,5,6
# ```
# genera una lista de 6 valores enteros.
# ```python
# 1,2,34,5,6
# ```
# genera una lista de 5 valores enteros.
# ```python
# 1,2,3,4,,5,6
# ```
# genera una lista de 7 valores, 6 enteros y uno *vacío*.
# 
# ### Ejercicio
# 1. Busca la manera de escribir y leer la información en un archivo CSV empleando la librería `pandas`.
# 
