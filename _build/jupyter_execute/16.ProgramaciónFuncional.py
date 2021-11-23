#!/usr/bin/env python
# coding: utf-8

# # Programación funcional

# :::::{important} ¿Cómo vamos?
# 
# 
# Hasta el momento debemos tener claro lo siguiente:
# 
# 
# ````{tabbed} Funciones en Python
# 
# :::{admonition} Recordemos...
# :class: tip
# Hemos logrado crear funciones en Python, así mismo estudiamos como documentarlas y las diferentes formas de definirlas según los argumentos que reciben.
# :::
# ````
# 
# 
# ````{tabbed} Variables
# 
# :::{admonition} Recordemos...
# :class: tip
# Una variable en Python sirve para **guardar un valor específico**, ya sea **numérico**, **texto** u otro [**Tipo de Dato**](https://www.w3schools.com/python/python_datatypes.asp) con un nombre que nosotros escojamos. Debemos escribir una expresión de la forma:
# 
# [Nombre de variable]=[Valor para guardar]
# 
# :::
# ````
# :::::

# La **programación funcional** es un paradigma de programación en el que el método principal de cálculo es la evaluación de funciones. La programación funcional no es tan usada en Python, sin embargo, hay que conocerlo porque seguramente habrán situaciones en la que esa forma de trabajar puede mejorar la eficiencia algorítmica. 

# En la programación funcional, cada programa consiste en la evaluación de funciones compuestas y el cálculo es libre de valores intermedios pues todo se contempla como entrada y salida de una función. En Python hay posibilidad de implementar este modelo de programación por dos razones:
# 
# * Es posible tomar una función como argumento de otra y 
# * es posible tener como salida una función.
# 
# En gran medida esto es por una razón muy particular de Python: **¡Todo es objeto!**
# 
# Es decir, las funciones están al nivel de las cadenas de caracteres y los números. En el siguiente ejemplo, se define una función y se estudia como una variable comun y corriente:
# 
# 
# 
# 
# 

# In[1]:


def func(x):
    return x*5

otrafun=func


# In[2]:


otrafun(20)


# Observa que:

# In[3]:


id(func)


# In[4]:


id(otrafun)


# Acabamos de ver que tiene un comportamiento de variable, hagamos un ejemplo más atrevido, incluiremosla función en una lista y la evaluaremos con la lista:

# In[5]:


Lista=[1,2,func]
print(Lista)


# In[6]:


Lista[2](10)


# La flexibilidad de la función permite que se evalúe una función como argumento de otra, veamos un ejemplo:

# In[7]:


def func(x):
    return x*5

def externa(funcion,x):
    return funcion(x+52)    


# In[8]:


externa(func,10)


# ***
# :::{note}
# Python permite usar decoradores para facilitar la sintáxis de esta composición de funciones, por ejemplo:
# :::

# In[9]:


def decorador(x):
    def wrapper(funcion):
        print("Something is happening before the function is called.")
        funcion(x+52)
        print("Something is happening after the function is called.")
    return wrapper

@decorador(10)
def func(x):
    print(x*5)


# Veámoslo con algo más sencillo:

# In[10]:


def my_decorator(func):
    def wrapper():
        print("Vamos a llamar a la función que dice !Viva la vida!")
        func()
        print("Ya lo dijo.")
    return wrapper

@my_decorator
def vivalavida():
    print("¡Viva la vida!")


# In[11]:


vivalavida()


# ***

# Los diferentes niveles de llamada de la función son importantes en la definición, tenemos por ejemplo:

# In[12]:


def funcion_1():
    def funcion_2():
        print('Hola, estoy metido en dos funciones')
    return funcion_2 


# In[13]:


otrafun=funcion_1()


# In[14]:


otrafun()


# In[15]:


funcion_1()()


# Como se puede apreciar, para poder obtener el resultado tuvimos que poner dos paréntesis en la funcion_1.

# ## Definición de funciones con *lambda*
# 
# En Python podemos generar funciones rápidamente y de manera anónima, se trata de las expresiones lambda, una forma corta y concisa de declarar funciones en Python. Su sintáxis es la siguiente:
# 
# ```Python
# lambda argumentos: expresión
# 
# ```
Por ejemplo, en la siguiente celda se evalúa, sin guardar, la función x+4 para x=2:
# In[16]:


(lambda x: x+4)(2)


# Podriamos guardar la expresión lambda en una variable:

# In[17]:


cuadrado= lambda x: x**2


# In[18]:


cuadrado(10)


# Aprovechemos y miremos el tipo de dato que guarda una expresión lambda:

# In[19]:


type(cuadrado)


# observe que pasa con la función definida de manera habitual:

# In[20]:


def cuadrado(x):
    return x**2
type(cuadrado)


# La función lambda admite varios argumentos, por ejemplo:

# In[21]:


suma=lambda x,y: x+y


# In[22]:


suma(3,5)


# Pero solo se deja una salida:

# In[23]:


suma_y_resta=lambda x,y: x+y,x-y


# El error es ocasionado porque no sale un solo elemento, podemos usar tuplas o listas para obtener varios datos:

# In[70]:


suma_y_resta=lambda x,y: (x+y,x-y)


# In[71]:


suma_y_resta(8,3)


# ## Funciones especiales para aplicar funciones
# 
# Para una adecuada implementación de un estilo funcional de programación, Python cuenta con tres métodos muy especiales que complementan muy bien este paradigma. Hablamos de `map()` y `filter()`. Veamos en detalle algunos ejemplos que nos pueden orientar en su practicidad:
# 
# ### `map()`
# 
# La función `map()` es una función integrada de Python que aplica una función a cada elemento de un iterable. En el estiulo funcional se asemeja a una estructura de iteración y por lo tanto podría verse como un bucle declarado (vale la pena recordar esos dos tipos de programación: declarada e imperativa).
# 
# La sintaxis de map es:
# 
# ```Python
# map(funcion,iterable)
# ```
# 
# 

# In[76]:


map(lambda x: x+'2','hola')


# El objeto que `map` guarda es un iterador, ya conocemos varias formas de verlo:
# 

# In[77]:


ejemplo=map(lambda x: x+'2','hola')
for i in ejemplo:
    print(i)


# In[78]:


ejemplo=map(lambda x: x+'2','hola')
list(ejemplo)


# In[80]:


ejemplo=map(lambda x: x+'2','hola')
set(ejemplo) ## No tan bueno


# Otro ejemplo bien interesante puede ser:

# In[82]:


ejemplo2=map(lambda x: True if x**2 >= 5050 else False,range(100))


# Recuerden usar `list` para ver el resultado:
# 
# ```Python
# list(ejemplo2)
# ```

# **map con varios iterables**
# 
# `map()` admite varios iterables en sus argumentos, tenemos que:
# ```Python
# map(funcion, iterable_1,iterable_2,...,iterable_n)
# ```

# En este caso, la función admite $n$ variables y la longitud de la salida coincide con la de cada iterable. De hecho, usando notación matemática tenemos:
# 
# $$map(f,[x_1,x_2,\cdots, x_n],[y_1,y_2,\cdots, y_n],[z_1,z_2,\cdots, z_n])=[f(x_1,y_1,z_1),f(x_2,y_2,z_2),\cdots,f(x_n,y_n,z_n)] $$

# In[88]:


list(map(lambda x,y,z: x+y+z+'2','hola','adios','chao'))


# Todos los iterables deben ser de la misma longitud, si no tendremos error:

# In[87]:


list(map(lambda x,y,z: x+y+z+'2','hola','adios','chao','bye'))


# Otro ejemplo más aclarador:

# In[89]:


list(map(lambda x,y,z: x+y+z,'ABCDE','abcde','12345'))


# ### `filter()`
# 
# La función `filter()` permite seleccionar elementos de un iterable según la función dada, por ejemplo:

# In[93]:


filter(lambda x:x if x!='a' else '','armadura')


# Lo convertimos en lista:

# In[94]:


list(filter(lambda x:x if x!='a' else '','armadura'))


# Por ejemplo podemos extraer los pares de la lista de los primeros 30 enteros positivos:

# In[98]:


def es_par(x):
    return x%2==0


# In[99]:


list(filter(es_par,range(1,31)))


# Es una función muy util, combina el poder de un bucle con un condicional. Resulta bastante útil para diferentes probemas de selección.
# 

# ## Cierre
# 
# En esta sección exploramos conceptos elementales de la programación funcional, es evidente su diferencia con la programación estructurada que conociamos y posiblemente habrán muchos algoritmos que para nuestra formación inicial no se puedan llevar a cabo con este estilo de programación. NO obstante, la potencia de poder aplicar funciones y de crear algoritmos en este sentido se utiliza bastante en el análisis de tablas de datos, de hecho, siguiendo los lineamientos de este estilo es más fácil paralelizar la computación y el valor final de las ejecuciones es más transparente que lo que se obtiene por la programación estructurada.
# 
