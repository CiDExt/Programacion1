#!/usr/bin/env python
# coding: utf-8

# # Referencias en Python:

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

# :::{Note} Apuntadores
# 
# En lenguajes como **C** o **C++** los apuntadores son unas herramientas destacadas en la optimización de rutinas puesto que indican la dirección de memoria donde se guardan las variables. 
# En ese sentido, en tareas como la asignación dinámica de memoria, la creación de código conciso y compacto (sin reescribir encabezados) y en la eficiencia del código;  los apuntadores son fundamentales para los programadores en C o C++. Si quieres más información consulta en [https://www.tutorialspoint.com/cprogramming/c_pointers.htm](https://www.tutorialspoint.com/cprogramming/c_pointers.htm)
# 
# :::
# 
# 

# En Python no hay apuntadores, todo por mantener  los 20 principios de [Zen de Python](https://www.python.org/dev/peps/pep-0020/). Recordemos:
# 

# In[1]:


import this


# En este particular, la implementación de apuntadores contradice varios de los principios del lenguaje, ya bien se por su complejidad, por hacer cambios implicitos y porque esencialmente Python se concentra en la usabilidad más que en la velocidad. 
# 
# No quiere decir lo anterior que Python impida optimizar código con algunas ideas provenientes del uso de apuntadores, hay algunos beneficios de estas ideas que se pueden implementar en Python. Veamos en detalle lo que significa guardar un valor en Python.

# ## ¡Todo es objeto!
# 
# En el estudio de [paradigmas de programación](/7.Paradigmas.html) vimos que hay un estilo de programación orientado a objetos, en ese resumen vimos que el concepto de objeto que se entiende como una entidad abstracta conformado por métodos y atributos. Veamos lo siguiente: 

# In[2]:


isinstance(1,int)


# `isinstance()` permite identificar si un **objeto** es una **instancia** de una clase. Aquí ya estamos diciendo que el entero es un **objeto**, como si quisieramos decir que implicitamente todo lo que clasifique isinstance es un objeto, y pues :

# In[3]:


isinstance(1,object)


# Claramente si pensamos en más y más elementos tendriamos un resultado similar:

# In[4]:


import math 
print(isinstance(math.sqrt,object))
print(isinstance(math.pi,object))
print(isinstance([1,2,3],object))
print(isinstance({1:1,2:2,3:'Hola'},object))


# Estos objetos en Python tienen una estructura interesante, se tratan, la mayoría de veces, de la misma manera por el lenguaje y siempre cuentan con dos partes importantes:
# 
# * [Conteo de referencias](https://docs.python.org/es/3/c-api/intro.html#reference-counts), para hacer gestión de memoria, ver [https://realpython.com/python-memory-management/](https://realpython.com/python-memory-management/) y
# * [Tipo](https://docs.python.org/es/3/reference/datamodel.html#types) que determina qué tipo de objeto es (por ejemplo, un número entero, una lista o una función definida por el usuario).
# 
# 
# 
# 

# ## Diferencias de las variables entre C y Python

# **En el caso de C** 
# 
# Si hacemos lo siguiente:
# 
# ```C
# int x=152
# ```
# 
# estamos siguiendo el siguiente proceso:
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/619bd815ba39a10d85c08574" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>
# 

# Lo que ocurre es que se asigna un espaciode memoria para un número entero, el valor 152 se almacena en ese espacio de memoria y se indica que `x` apunta a ese valor. 

# Si cambiamos el valor de la variable,
# 
# ```C
# x=898
# ```
# 
# entonces cambiamos el valor guardado en ese espacio de memoria:
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/619bdc85672a090d98e7f21e" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# **En el caso de Python** 
# 
# El ejercicio análogo hace un proceso un poco más largo. Crea un `PyObject`, identifica que el tipo de ese elemento es entero indica que ese objeto tiene valor 152, por otro lado crea un nombre llamado `x`, apunta `x` a `PyObject` y aumenta el contador de referencias del `PyObject` en 1:
# 
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/619beb4f672a090d98e7f3ad" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# Observe que la memoria guarda el objeto 152, en este caso el nombre `x` no tiene dirección de memoria, si hacemos una actualización como  ` x=153 ` ocurre lo siguiente:
# 
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/619bf2d9672a090d98e7f4a0" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# Si hacemos algo más interesante, como por ejemplo `y= x `
# 
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/619c230456355d0dcbd80610" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>
# 
# Note que el contador de referencias se va actualizando cada vez que se hace una asignación nueva.

# ### Objetos mutables vs inmutables
# 
# Recuerdas la gran diferencia de la lista y la tupla, la lista se puede modificar cuando se quiera, en la tupla no puedo hacer eso, por ejemplo:

# In[5]:


a=(1,2,3)
b=[1,2,3]


# In[6]:


b[0]=2
print(b)


# In[7]:


a[0]=2
print(a)


# Pasa muy parecido con las cadenas de caracteres:

# In[13]:


txt='hola'
txt[0]='b'
txt


# En particular tenemos que:
# 
# |Tipo|¿Inmutable?|
# |:--:|:--:|
# |`int`|Sí|
# |`float`|Sí|
# |`bool`|Sí|
# |`complex`|Sí|
# |`tuple`|Sí|
# |`frozenset`|Sí|
# |`str`|Sí|
# |`list`|No|
# |`set`|No|
# |`dict`|No|

# Ahora bien, en Python, el usuario relaciona el objeto y su contenido mediante una referencia, la cual es a la dirección en la cual se encuentra alojado dicho objeto en la memoria del computador (apuntador) mediante la función `id()`, así: 

# In[14]:


id(1)


# En una asignación como la siguiente: 
# ```Python
# x = 1
# ``` 
# `x` no contiene el valor 1, pero sí la información del objeto en la memoria, en el cual se se encuentra alojado tal valor. En otras palabras, podríamos afirmar que `x` "apunta" o "se refiere" a un objeto en el cual se halla alojado el 1.
# 
# 

# In[15]:


x=1
id(x)


# Observe que las dos salidas coinciden. Algo que debemos tener claro es que dos objetos diferentes no pueden estar alojados en la misma dirección, es decir, cada objeto tiene una única dirección en la memoria. No nos es posible acceder a la dirección de los objetos, pero podemos acceder al identificador único que ellos poseen:

# In[16]:


print(id(1))
print(id(2))


# Muy probablemente, este número entero que obtuvimos, conocido como la **identidad** del objeto, sea diferente en cada máquina y en cada oportunidad que reiniciemos el kernel. El siguiente es un ejempo muy claro en el cual podremos ver que la identidad de cada objeto es única:

# In[20]:


def cuadrado(x):
    print('El valor es:',x,'y su identidad es:',id(x))
    print('Su cuadrado es:',x**2,'y su identidad es:',id(x**2))
    return x**2


# In[21]:


cuadrado(1)


# In[22]:


cuadrado(x)


# Notemos que la función `cuadrado` regresa el mismo valor de identidad para 1, su cuadrado, $x$ y su cuadrado, ya que en ambos casos hablamos del mismo objeto, mientras que para el siguiente caso el valor de la identidad del parámetro y de su cuadrado cambian:  

# Si hay un cambio:

# In[23]:


cuadrado(2)


# Para comprobar que dos elementos tienen la misma identidad empleamos la función `is`, así:

# In[ ]:


x is 1


# In[ ]:


2 is x+1


# Notemos que, la función puede recibir la referencia a un objeto inmutable, y por más cálculos que se hagan sobre dicho objeto, éste no estará afectado, por ejemplo: 

# In[28]:


y = 2


# In[29]:


def cuadrado(x):
    print('El valor es:',x,'su identidad es:',id(x))
    x = x**2
    print('Su cuadrado es:',x,'y su identidad es:',id(x))
    return y


# In[26]:


cuadrado(y)


# In[27]:


y


# Cabe resaltar que si no hacemos uso de la referencia del valor original, se estaría almacenando un poco de *basura* en nuestra memoria.

# En el caso de los objetos mutables pasa algo muy curioso, veamos:

# In[31]:


Lista=[1,2,3]
print(Lista)
print(id(Lista))


# In[32]:


Lista[1]=0
print(Lista)
print(id(Lista))


# Estos objetos cambian no solo en Python sino que en la memoria también, a diferencia de los elementos inmutables que asumen cambios en nuevos espacios de memoria, los elementos mutables cambian en ese mismo espacio. 

# ## Cierre
# 
# Python tiene una filosofia interesante frente al uso de memoria, cambia totalmente la idea detrás de los apuntadores y utiliza nombres más allá que variables. Si quisiese aplicar ideas de optimización con apuntadores en este lenguaje debería trabajar con objetos mutables, sin embargo, recuerda:

# In[35]:


import this

