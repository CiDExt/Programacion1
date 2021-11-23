#!/usr/bin/env python
# coding: utf-8

# # Math y Random - introducción

# :::::{important} ¿Qué debemos tener presente?
# 
# 
# Módulos y paquetes
# 
# 
# ````{tabbed} Módulos
# 
# :::{admonition} ¿Qué es?
# :class: tip
# Un módulo, es un archivo de Python cuyos objetos (funciones, clases y demás) pueden ser accedidos desde otro archivo.  
# Son una gran herramienta para organizar grandes códigos.
# :::
# ````
# 
# ````{tabbed} Paquetes
# 
# :::{admonition} ¿Qué son?
# :class: tip 
# Son carpetas las cuales contienen varios módulos.
# :::
# ````
# 
# :::::

# ## Paquete  Math
# En muchos de los cálculos que debemos realizar, requerimos emplear funciones matemáticas y para ello debemos emplear el paquete `math`, primero lo importaremos:
# ```python
# import math
# ```

# Una vez el paquete ha sido importado, podremos hacer uso de sus constantes y funciones. Algunas de las más relevantes son:
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/math1.png?raw=true"  width=600 >
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/math2.png?raw=true"  width=600 >
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/math3.png?raw=true"  width=600 >
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/math4.png?raw=true"  width=600 >
# 

# ## Paquete Random

# En algunos de nuestros ejemplos hemos visto la forma de crear listas de números "aleatorios", ha llegado el momento de entender la forma de hacerlo:

# In[1]:


import random


# La primera función que vamos a conocer es  `seed`, ésta permite crear una semilla, la cual permite que el experimento que se realice o el código que se ejecute sea reproducible, es decir, sin importar la máquina, el día ni la hora, se obtenga los mismos resultados.

# In[2]:


random.seed(a='hola')
random.randrange(0, 10)


# In[3]:


random.seed(a=4.3)
random.randrange(0, 10)


# In[4]:


random.seed(a='hola',version=1)
random.randrange(0, 10)


# In[5]:


random.seed(a=4.3,version=1)
random.randrange(0, 10)


# La sintáxis de la función es la siguiente:
# ```python
# random.seed(a = "valor de la semilla", version = n)
# ```
# El valor de la semilla puede ser un objeto `int`, `float`, `bytes`, `bytearray` y `str`, mientras que la versión puede ser 1 o 2; la versión 1 es compatible con versiones anteriores de Python y no genera el mismo rango de valores para las semillas `str` y `bytes`, como pudimos ver con los ejemplos anteriores.
# 
# La siguiente función a tener en cuenta, es la función `randrange` la cual nos permitirá elegir un valor en un determinado rango de valores e incluso permite incluir la separación entre las elecciones, la manera de emlearla es la siguiente:
# ```python
# random.randrange(inicio, fin+1, salto)
# ```
# Los valores inicial y final deben ser números enteros.
# 
# ### Ejercicio
# 1. Crea una lista de 20 valores aleatorios desde el 20 hasta 49 cuyos elementos estén separados 3 unidades, entre sí.
# 2. La diferencia en los resultados obtenidos al ejecutar el código en dos bloques diferentes y todo el código en un único bloque a qué se debe

# In[6]:


import time
lista1 = []
random.seed(a=time.time())
for i in range(10):
    lista1.append(random.randrange(0, 10))    


# In[7]:


lista2 = []
random.seed(a=time.time())
for i in range(10):
    lista2.append(random.randrange(0, 10))  
print(lista1,lista2)


# In[8]:


import time
lista1 = []
random.seed(a=time.time())
for i in range(10):
    lista1.append(random.randrange(0, 10))    
lista2 = []
random.seed(a=time.time())
for i in range(10):
    lista2.append(random.randrange(0, 10))  
print(lista1,lista2)


# Una función que permite elegir un número entero de manera aleatoria de en un intervalo dado es: `randint`. Los argumentos de ésta función son los extremos del intervalo, los cuales deben ser números enteros, en el cual estamos pensando elegir nuestro número aleatorio. Su sintáxis es la siguiente:
# ```python
# random.randint(extremo_inferior,extremo_superior)
# ```

# In[9]:


random.randint(0,5)


# En ocasiones necesitaremos extraer un valor aleatorio de una lista que hallamos creado, para ello emplearemos la función `choice`: 

# In[10]:


random.choice(['cero',1,2,3.14,'cuatro'])


# Ésta función tiene un único argumento, el cual es la lista de la cual deseamos extraer el valor al azar:
# ```python
# random.choice(lista)
# ```

# ### Ejercicio
# 1. Modifica el siguiente código para que las dos elecciones siempre sean iguales.

# In[11]:


random.seed(a=1)
p = random.choice(lista1)
q = random.choice(lista2)
print(p,q)


# No siempre necesitamos generar valores enteros, en oportunidades requerimos crear listas de números flotantes, tarea para la que usaremos la función `uniform`, ésta nos permite generar un número aleatorio de coma flotante entre los números mencionados en sus argumentos; el límite inferior se incluye y el superior no. 

# In[12]:


random.uniform(0,5)


# # Cierre
# En python existen una variedad inmensa de paquetes, cada uno con sus funciones específicas, En el cuaderno abordamos dos paquetes que nos servirán en el futuro, pero cabe mencionar que existen otros como `NumPy`, `SymPy` y `Matplotlib` que abordaremos más adelante.

# In[ ]:




