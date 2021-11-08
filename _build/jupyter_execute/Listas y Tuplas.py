#!/usr/bin/env python
# coding: utf-8

# # Listas y Tuplas

# En los cuadernos anteriores tuvimos un breve acercamiento a las listas, en el presente, el objetivo es entender las similitudes y diferencias que hay entre ellas y las tuplas, como también tener presentes algunos de los métodos y funciones más útiles al trabajar con éstos objetos.
# 
# ## Listas:
# Para **crear una lista** basta con escribir entre corchetes los elementos que la componen separados por coma, así: `l = [0, 1, 2, 3]`
# 
# 

# In[1]:


l = [0, 1, 2, 3]
l


# Las listas por lo general contienen elementos del mismo tipo, como ocurre con la lista que acabamos de definir, en la cual cada una de sus entradas es un número entero. Pero ellas pueden contener elementos de diferentes tipos, como por ejemplo:

# In[2]:


m = ['hola', 1, 5.1, id(l)]
m


# lista en la cual vemos elementos del tipo `str`, `int`, `float` y el resultado de una función el cual es `int`.
# 
# Para **acceder a un elemento de la lista** se emplea la siguiente notación `nombre_de_la_lista[índice]`, el índice de la lista hace referencia a la posición en la cual se encuentra el elemento y éste es un número entero no negativo, es decir, el primer elemento de una lista tiene como índice el 0, el segundo es el índice 1 y así suscesivamente, esto marca una diferencia con otros lenguajes de programación, en los cuales el primer elemento de una lista tiene índice 1.

# In[3]:


m[0]


# In[4]:


m[1]


# In[5]:


l[2]


# Algunos índices negativos también se pueden utilizar, éstos los que indican es que la lista se recorre en orden inverso, es decir, el índice -1 es el último elemento de la lista, el -2 es el penúltimo, etc., como podemos ver a continuación:

# In[6]:


import IPython.display as display
fig00 = """
<iframe width="800" height="300" src="https://www.geogebra.org/classic/fkkeq7rx" style="border: 1px solid black"></iframe>
"""
display.HTML(fig00)


# In[7]:


l[-1]


# In[8]:


l[3]


# Para poder determinar con certeza el tamaño de la lista se emplea la función `len(lista)`, la cual arroja como resultado dicho valor, por ejemplo

# In[9]:


len(l)


# In[10]:


len(m)


# Si intentamos acceder a algún índice el cual no exceda el tamaño de nuestra lista, obtendremos como resultado un error, así:

# In[11]:


m[5]


# In[12]:


l[-5]


# En las listas podemos tener como índices números enteros, o expresiones que arrojen  un número entero, por ejemplo

# In[13]:


l[3] is l[2+1]


# El contenido de las listas se puede modificar de manera muy sencilla, accedemos a la posición que deseamos modificar y asignamos el valor que deseamos esté allí, por ejemplo:

# In[14]:


m[0] = 1
m


# Esto muestra que las listas son **objetos mutables**, es decir, que se pueden modificar. 
# 
# Pero no todas las secuencias de objetos lo son, por ejemplo, al definir la cadena `s = 'hola'`, no podemos modificar el elemento `s[0]`:

# In[15]:


s = 'hola'


# In[16]:


s[0]


# In[17]:


s[0] = 'B'


# Una necesidad recurrente es: **agregar elementos a una lista**, para ello la forma más natural de hacerlo es mediante el método `lista.append(elemento_a_agregar)`:

# In[18]:


l


# In[19]:


l.append('cuatro')
l


# Las listas pueden concatenarse, es decir, dadas dos listas, obtendremos como resultado una nueva lista que tenga los elementos de la primera lista seguido de los de la segunda, así:

# In[20]:


M = l+m
M


# Esto nos permite agregar elementos a una lista de otra manera, empleando el operador `+=`, como podemos ver:

# In[21]:


l += [5]
l


# ### Ejercicio
# 1. Crea un bloque de código que dada una lista en blanco vaya agregando elementos a ésta. Dichos elementos deberán ser la suma de los índices hasta la posición en que se halla el elemento.
# 
# 

# En otras ocasiones es muy necesario eliminar elementos de las listas, por ejemplo, vamos a eliminar el segundo elemento de la lista `M` que creamos anteriormente:

# In[22]:


del M[2]
M


# Es decir, al seguir la línea de comando `del lista[índice_que_se_desea_eliminar]`, se borra la entrada de la lista.

# ## Tuplas
# Las tuplas, a diferencia de las listas, son objetos inmutables en los cuales se almacenan datos, bien sean del mismo o de diferentes tipos, siendo éste último el uso más frecuente.
# 
# De modo que definiremos nuestra primera tupa:

# In[23]:


temperatura = 'Enero', '01', 19
#Equivalentemente
#t = ('Enero', '01', 19)
temperatura
#Sin importar como la definamos, siempore se visualizarán sus elementos entre paréntesis y separados por una coma


# Para conocer la cantidad de elementos que hay en una tupla, empleamos la misma función que para las listas, la función `len(tupla)`, así:

# In[24]:


len(temperatura)


# Si deseamos definir una tupla con un único elemento, debemos hacerlo de la siguiente manera:

# In[25]:


tupla1elemento = 23, #Observa la coma
tupla1elemento


# La coma es la que indica que es una tupla, ya que se si hace sin ella, incluso entre paréntesis, se guardará el entero 23 y no la tupla cuyo único elemento es el 23.
# 
# Para acceder a la información almacenada en las diferentes entradas de una tupla, lo hacemos de la misma manera que lo hicimos con las listas, es decir, `tupla[índice]`, así:

# In[26]:


temperatura[0]


# y éstas se pueden operar:

# In[27]:


'La temperatura máxima en Bogotá el '+ temperatura[1]+' de '+temperatura[0]+' del 2021 fue de '+str(temperatura[-1])


# ¿Qué pasa si intentamos modificar una entrada de una tupla?

# In[28]:


temperatura[0]='hola'


# Como lo comentamos antes, las tuplas son **inmutables**.
# 
# Para agregar elementos a una tupla empleamos el operador `+=`, de la misma manera que lo hicimos con las listas. Para las tuplas no disponemos del método `append`.

# In[29]:


tupla1elemento += ('a',)
tupla1elemento


# Como hemos recalcado las tuplas son inmutables, pero pueden contener elementos mutables, por ejemplo:

# In[30]:


tupla1elemento += ([1,2,3,4],)
tupla1elemento


# In[31]:


tupla1elemento[2]=1
#genererá un error ya que no podemos modificar el elemento de la tupla


# In[34]:


#Pero podemos modificar la lista que está dentro de la tupla
tupla1elemento[2][3]='cuatro'
tupla1elemento

