#!/usr/bin/env python
# coding: utf-8

# # Bucles (for)
# 
# :::::{important} ¿Cómo vamos?
# 
# 
# Hasta el momento debemos tener claro lo siguiente:
# 
# 
# ````{tabbed} Paradigmas de Programación
# 
# :::{admonition} Recordemos...
# :class: tip
# Un **paradigma de programación** indica las guías y métodos de realizar cálculos y la manera en que se deben estructurar y organizar las tareas que debe llevar a cabo un programa. Se asocian a cierto estilo de programación y al modelo de computación (operaciones permitidas) admitido en nuestro sistema.
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
# 
# 
# 

# La iteración que veremos hoy es la iteración definida, en esta se repite un proceso para elementos alojados en una colección de objetos. El bucle que lo permite es `for` y funciona de la siguiente manera:
# 
# ```Python
# for objeto in colección_de_objetos:
#     instrucción_1
#     instrucción_2
#     ...
#     instrucción_n
# otras instrucciones
# otras instrucciones
# otras instrucciones    
# ```

# En las instrucciones dentro de `for` el valor de objeto varía conforme se vaya recorriendo la colección. Un ejemplo muy sencillo puede ser:

# In[1]:


Lista=['Elemento_1','Elemento_2','Elemento_3']
print('Sentencia previa a iniciar el bucle.\n')
for Elemento in Lista:
    print(' -> Instrucción inicial dentro del bucle para el:')
    print(' ->',Elemento)
    print(' ')
    print(' -> Fin de la iteración\n\n')
print('Fin del bucle')


# La colección que recorre el `for` debe ser un  elemento iterable. Hay elementos iterables que no son tan evidentes. Por ejemplo:

# In[2]:


for i in 'Hola Mundo':
    print(i)


# El ejemplo anterior recorrió cada caracter de la cadena de caractéres, esta cadena se reconoce como elemento iterable, al respecto tenemos los siguientes tipos de datos:
# 
# * **Cadenas de caracteres**
# * **Listas**
# * **Tuplas**
# * **Conjuntos**
# * **Diccionarios**

# para saber si son iterables podemos utilizar la función `iter()`:

# In[3]:


iter('Hola')


# si el resultado es de la forma `<str_iterator at *****>` el objeto es iterable. En otro caso obtenemos una excepción:

# In[4]:


iter(20)


# Aparte de los tipos de datos mencionados anteriormente en Python hay una gran cantidad de datos iterables, el método mencionado `iter`  sobre el objeto lista es el que permite recorrer los elementos de una lista. De hecho podemos utilizarla de nuestra parte usando su complemento `next()`. Veamos:

# In[13]:


Lista=['Elemento_1','Elemento_2','Elemento_3']
iterable=iter(Lista)
print(next(iterable))
print(next(iterable))
print(next(iterable))


# Si hacemos el siguiente `next` tendremos un problema:

# In[14]:


next(iterable)


# In[16]:


print(iterable)


# Observemos el siguiente código, salvo por la excepción ¿Qué podríamos estar viendo?

# In[27]:


Lista=['Elemento_1','Elemento_2','Elemento_3','Elemento_4','Elemento_5']
iterable=iter(Lista)
while True:
    elemento=next(iterable)
    print(elemento)


# Indiscutiblemente `for` recorre las listas ayudandose del iterador y la función next. `StopIteration` muestra el final del camino del for. Veremos a continuación unos elementos que son extremadamente útiles para trabajar con `for`.

# 
# 
# ## Funciones útiles para trabajar con for
# 
# ### range()
# 
# `range()`es una función de Python que genera un elemento iterable que recorre un rango numérico, tenemos:
# 

# 
# ```Python 
# range(start, stop, step) ## start hace referencia al inicio del rango numérico, 
#                          ## por defecto es 0.
#                          ##
#                          ## stop  hace referencia el límite final del  
#                          ## rango numérico, no se toca por el rango.
#                          ##
#                          ## step hace referencia al paso del rango, 
#                          ##por defecto es 1.
#         
#         
# ```

# Así si quiero la lista de los números del 1 al 10 escribo:

# In[30]:


range(1,11) 


# para verificarlo, sabiendo que el rango numérico es iterable,  escribimos:

# In[31]:


for i in range(1,11):
    print(i)


# Si quiero la lista de los pares menores o iguales a 10 y mayores o iguales a 2 escribimos:

# In[32]:


lista=range(2,11,2)
for i in lista:
    print(i)


# Si utilizamos `help` para entender como funcione `range()`tenemos:

# In[3]:


help(range)


# ### enumerate()
# 
# `enumerate()` crea una lista a partir del argumento que puede ser un elemento iterable en el cual cada elemento corresponde a una tupla que contiene un índice para el elemento y el elemento al que alude. En el siguiente script vemos como `for` permite desentrañar la función:

# In[33]:


Lista=['Elemento_1','Elemento_2','Elemento_3','Elemento_4','Elemento_5']

for i in enumerate(Lista):
    print(i)


# Podemos referenciar los elementos por separado desde el mismo `for`:

# In[34]:


for i,j in enumerate(Lista):
    print('El índice de', j, 'es', i,'\n')


# Es una herramienta muy útil cuando requerimos la posición del elemento.

# ## break y continue en for
# 
# Como en `while` podemos interrumpir el ciclo en `for`, usamos `break` y `continue`:
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 116.67%; padding-top: 0; height: 0;"><iframe frameborder="0" width="600" height="700" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/619837a5c909030d904263d9" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# In[40]:


Lista=['Elemento_1','Elemento_2','Elemento_3','Elemento_4','Elemento_5']
for i in Lista:
    if 'Elemento_3'==i:
        break     
    print(i)
    
print('Bucle terminado.')
    


# In[41]:


Lista=['Elemento_1','Elemento_2','Elemento_3','Elemento_4','Elemento_5']
for i in Lista:
    if 'Elemento_3'==i:
        continue   
    print(i)
    
print('Bucle terminado.')


# ## else en for
# 
# Igual que en `while` for puede trabajarse con `else`, su interpretación es similar:

# In[44]:


FV = ['Papa', 'Limón', 'Cebolla', 'Arroz']
s = 'Chocolate'

for i in FV:
    if i == s:
        print(s, 'fue encontrado en la lista.')
        break
else:
    print(s, 'no fue encontrado en la lista.')


# In[45]:


FV = ['Papa', 'Limón', 'Cebolla', 'Arroz','Chocolate']
s = 'Chocolate'

for i in FV:
    if i == s:
        print(s, 'fue encontrado en la lista.')
        break
else:
    print(s, 'no fue encontrado en la lista.')


# ## Cierre
# 
# Hemos visto la iteración definida en Python, acabamos de recorrer listas y abrimos los ojos a nuevos algoritmos y formas de trabajar. Con eso completamos la revisión de estructuras de control fundamentales y según el [teorema de Böhm–Jacopini](https://en.wikipedia.org/wiki/Structured_program_theorem) ya podemos crear cualquier función computable. 

# ## Ejercicio 1
# 
# Defina una lista con los días de este mes. Utilice el paquete `datetime`. Defina un algoritmo para determinar cuales de esos días hacen referencia a días de fin de semana.

# ## Ejercicio 2
# 
# Haga un algoritmo que identifoque los primeros 100 números primos.
