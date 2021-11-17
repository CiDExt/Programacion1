#!/usr/bin/env python
# coding: utf-8

# # Listas y Tuplas

# :::::{important} ¿Cómo vamos?
# 
# 
# Hasta el momento debemos tener claro lo siguiente:
# 
# 
# ````{tabbed} Página en github
# 
# :::{admonition} Recordemos...
# :class: tip
# Seguimos un tutorial detallado para empezar a manejar repositorios locales y en línea. Adicionalmente, vimos elementos básicos para la creación de páginas utilizando una rama adicional de los repositorios. Esperamos que en esas páginas haya una descripción completa de sus perfiles, ilusiones y los que serían sus próximos proyectos.
# :::
# ````
# 
# ````{tabbed} ¿Qué hace un programador?
# 
# :::{warning} 
# 
# **La respuesta es sencilla**
# 
# Convertir **soluciones** en instrucciones que pueda seguir un computador
# :::
# 
# se hace a través de algoritmos procesos libres de ambigüedades y con todos los pasos necesarios para llegar a la dichosa solución. Usamos herramientas de representación de los algoritmos: pseudocódigo o diagramas de flujo, que permiten resumir los pasos de un proceso.
# 
# ````
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
# 

# En el ejercicio anterior tuvimos un breve acercamiento a diferentes tipos de datos guardados en variables, le brindamos una atención particular a las cadenas de caractéres porque permitían extraer subtextos, caracteres por separado, entre otros. Ese orden intrinseco en cada cadena lo extrapolaremos para organizar secuencias de cualquier tipo de objetos, en este sentido, nos referimos a las listas y a las tuplas. Nuestro objetivo es entender las similitudes y diferencias que hay entre ellas, como también tener presentes algunos de los métodos y funciones más útiles al trabajar con éstos objetos.
# 

# 
# ## Listas:
# 
# 
# Una lista es una estructura de datos en Python conformada como una secuencia de elementos ordenada y modificable. Cada elemento o valor que está dentro de una lista se llama elemento. Así como las cadenas se definen como caracteres entre comillas, las listas se definen teniendo sus elementos entre corchetes `[ ... ]` y separandolos con comas  `,`; es decir, para **crear una lista** basta con escribir entre corchetes los elementos que la componen separados por coma, así: 
# 
# ```Python
# Lista = [Elemento_1,Elemento_2,Elemento_3,Elemento_4,Elemento_5]
# ```
# 
# Por ejemplo, el siguiente arreglo guarda los núumeros enteros de 0 a 3:
# 

# In[1]:


l = [0, 1, 2, 3]
l


# Las listas por lo general contienen elementos del mismo tipo, como ocurre con la lista que acabamos de definir, en la cual cada una de sus entradas es un número entero. Pero ellas pueden contener elementos de diferentes tipos, como por ejemplo:

# In[2]:


m = ['hola', 1, 5.1, id(l)]
m


# Aquí guardamos en `m` una lista con elementos del tipo `str`, `int`, `float` y el resultado de una función el cual es `int`.
# 
# 

# ### Explorar una lista
# 
# Para **acceder a un elemento de la lista** se emplea una notación similar a la utilizada en las cadenas de carcatéres:
# 
# ```Python 
# nombre_de_la_lista[índice]
# ```
# 
# 

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 25.00%; padding-top: 0; height: 0;"><iframe frameborder="0" width="800" height="200" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/6193e9d850419a0d7f19923b" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# 
# El índice de la lista hace referencia a la posición en la cual se encuentra el elemento y éste es un número entero. El primer elemento de una lista tiene como índice el 0, el segundo es el índice 1 y así suscesivamente, lo anterior marca una gran diferencia con otros lenguajes de programación, en los cuales el primer elemento de una lista tiene índice 1.

# In[3]:


m[0]


# In[4]:


m[1]


# In[5]:


l[2]


# Algunos índices negativos también se pueden utilizar, al emplear estos valores estamos indicando que la lista se recorre en orden inverso, es decir, el índice -1 es el último elemento de la lista, el -2 es el penúltimo, etc., como podemos ver a continuación:
# 

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 25.00%; padding-top: 0; height: 0;"><iframe frameborder="0" width="800" height="200" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/6193ec1cc5d9760d8b0e94da" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# In[6]:


l[-1]


# In[7]:


l[3]


# Para poder determinar con certeza el tamaño de la lista se emplea la función `len(lista)`, la cual arroja como resultado dicho valor, por ejemplo

# In[8]:


len(l)


# In[9]:


len(m)


# Si intentamos acceder a algún índice el cual no haga referencia a un índice de nuestra lista, obtendremos como resultado una excepción como la siguiente:

# In[10]:


m[5]


# In[12]:


l[-5]


# En las listas podemos tener como índices números enteros, o expresiones que arrojen  un número entero, por ejemplo

# In[13]:


l[3] is l[2+1]


# :::{admonition} **Ejemplo 1**
# :class: tip
# *(Días de la semana)* Una lista que contengan los días de la semana.
# :::

# In[3]:


Dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]


# :::{admonition} **Ejemplo 2**
# :class: tip
# *(Frutas y verduras)* Haga una lista de frutas y verduras.
# 
# `FV=["Fresas","Papaya","Limón","Brocoli","Acelgas","Espinacas"]`
# :::

# In[4]:


FV=["Fresas","Papaya","Limón","Brocoli","Acelgas","Espinacas"]


# In[5]:


FV


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


# In[ ]:





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

