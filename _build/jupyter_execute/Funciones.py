#!/usr/bin/env python
# coding: utf-8

# # Funciones

# A lo largo de los cuadernos hemos utilizado algunas funciones propias de Python `print`, `int`, `float`, etc. cada una de ellas está hecha para realizar una tarea específica. En el cuaderno anterior, hemos creado una función, `cuadrado`, la cual hace una tarea que nosotros deseábamos y no hay una de las propias de Python que hiciera tal labor:

# In[1]:


def cuadrado(x):
    print('El valor es:',x,'su identidad es:',id(x))
    x = x**2
    print('Su cuadrado es:',x,'y su identidad es:',id(x))
    return x


# In[2]:


cuadrado(3)


# In[3]:


x


# La manera adecuada para definir una función es la siguiente:
# ```
# def nombre_de_la_función (parámetros,separados,por,comas):
#     órdenes
#     ...
#     return el_resultado_que_deseamos_mostrar
# ```
# Para invocar a la función que hemos definido, debemos escribir el nombre de ésta y entre paréntesis los argumentos requeridos para que ésta sea ejecutada así:
# ```
# nombre_de_la_función (parámetros,separados,por,comas)
# ```
# Las funciones se pueden definir sin argumentos, lo cual hace que ejecute sus acciones sin requerir valores para que ésta funcione:
# ```
# nombre_de_la_función ()
# ```

# In[11]:


def funcion_sin_arg1():
    print('Esta función se ejecuta sin requerir valores de entrada')


# In[12]:


def funcion_sin_arg2():
    return'Esta función se ejecuta sin requerir valores de entrada'


# In[13]:


funcion_sin_arg1()


# In[14]:


funcion_sin_arg2()


# La diferencia entre las dos funciones anteriores es que en la segunda tenemos un `return`, es decir, la función tiene una salida que se puede almacenar para necesidades futuras.

# In[16]:


x = funcion_sin_arg1()
print('Éste es el resultado de la primera función:',x)
x = funcion_sin_arg2()
print('Éste es el resultado de la segunda función:',x)


# ## Documentación:
# A las funciones que creamos, es posible añadirles documentación para que sea clara la manera de usarlas y que los argumentos sean aclarados para todos los usuarios:

# In[24]:


def funcion_con_doc1(x):
    '''str de la variable de entrada.
    
    La función requiere de un argumento "x", el cual puede ser un valor numérico o una cadena de caracteres.
    Su salida es el string de la variable de entrada.'''
    return str(x) 


# Para ver esta documentación podemos hacerlo de la siguiente manera:  
# `funcion_con_doc1`+`shift`+`TAB`+`TAB`   
# o con el siguiente comando:
# 

# In[25]:


get_ipython().run_line_magic('pinfo', 'funcion_con_doc1')


# Lo más sano es escribir una descripción muy corta en la primera línea, luego una línea en blanco para continuar con la descripción más completa de la función.

# ## Variables locales:
# Cuando creamos una función y en ella definimos alguna variable, es posible acceder a ella únicamente dentro de la función, si la intentamos llamar fuera de ella, obtendremos un error, como podemos ver a continuación:

# In[32]:


def operaciones(x,y):
    z1 = x+y
    z2 = x-y
    z3 = x*y
    z4 = x/y
    print('Suma:',z1,'Resta:',z2,'Multiplicación:',z3,'División:',z4)


# In[33]:


operaciones(1,2)


# In[34]:


z1


# A las variables `z1`, `z2`, `z3` y `z4` se les conoce como **variables locales**, ya que éstas se "destruyen" al finalizar los cálculos requeridos para finalizar la ejecución de la función `operaciones`.

# # Ejercicios:
# Cree las siguientes funciones:
# * Una función que permita calcular el máximo entre dos números.
# * Una función que ordene de menor a mayor tres números.
# 
# # Ejemplo:
# Crearemos una función que permita contar los resultados obtenidos al lanzar un dado una cierta cantidad de veces.
# 
# Para ello emplearemos la función `randrange(a,b)` del paquete `random`, la cual nos permite obtener un número entero arbitrario en el intervalo $[a,b-1]$ siendo $a$ y $b$ números enteros, por ejemplo:

# In[6]:


import random
random.randrange(1, 7)


# In[17]:


def lanzardados (n):
    # n es la cantidad de veces que lanzaremos el dado
    # Para evitar errores con números no enteros, hacemos la siguiente consideración:
    n = int(n)
    # Definimos los contadores para cada número:
    cont1 = 0
    cont2 = 0
    cont3 = 0
    cont4 = 0
    cont5 = 0
    cont6 = 0
    # Debemos tomar un valor aleatorio entre 1 y 6, la cantidad de veces que indica n, para ello realizamos el siguiente ciclo
    for i in range(1,n+1):
        valor_en_el_lanzamiento = random.randrange(1, 7)
        if valor_en_el_lanzamiento == 1:
            cont1 += 1
        elif valor_en_el_lanzamiento == 2:
            cont2 += 1
        elif valor_en_el_lanzamiento == 3:
            cont3 += 1
        elif valor_en_el_lanzamiento == 4:
            cont4 += 1
        elif valor_en_el_lanzamiento == 5:
            cont5 += 1
        elif valor_en_el_lanzamiento == 6:
            cont6 += 1
    print(f'Valor{"Frecuencia":>13}')
    print(f'{1:>5}{cont1:>10}')
    print(f'{2:>5}{cont2:>10}')
    print(f'{3:>5}{cont3:>10}')
    print(f'{4:>5}{cont4:>10}')
    print(f'{5:>5}{cont5:>10}')
    print(f'{6:>5}{cont6:>10}')


# In[18]:


lanzardados(100)


# # Ejercicio:
# Como hemos podido ver, cada vez que ejecutamos la función anterior obtenemos diferentes resultados. Modifica éste código para que permita obtener los mismos valores cada vez que ejecutamos la función con determinado valor.
