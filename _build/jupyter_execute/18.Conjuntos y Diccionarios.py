#!/usr/bin/env python
# coding: utf-8

# # Conjuntos

# :::::{important} ¿Qué debemos tener presente?
# 
# 
# Objetos mutables e inmutables
# 
# 
# ````{tabbed} Mutables
# 
# :::{admonition} ¿Cuáles son?
# :class: tip
# * Listas.
# * Conjuntos.
# * Diccionarios.
# :::
# ````
# 
# ````{tabbed} Inmutables
# 
# :::{admonition} ¿Cuáles no son?
# :class: tip
# * Números (`int`, `float`, `bool`).
# * Cadenas de caracteres (`str`).
# * Tuplas.
# * Frozen sets.
# :::
# ````
# :::::

# Un **conjunto** es un objeto el cual se puede crear de dos maneras, la primera es escribiendo los elementos entre llaves `{}` separados por comas, y la otra es mediante la función `set()`, en la cual el argumento es un iterable el cual contiene los elementos del conjunto que deseamos crear:

# In[1]:


{0,1,2,3}


# In[2]:


set([0,1,2,3])


# In[3]:


set((0,1,2,3))


# ## Particularidades:
# Los conjuntos **no permiten repeticiones**, por ejemplo:

# In[4]:


print(set([1,2,3,1,2,1]))
# es el mismo conjunto:
print({1,2,3})


# Los conjuntos **no tienen un orden**, como lo tenían las listas y las tuplas:

# In[5]:


print({1,2,3})
print({3,1,2})
print({2,3,1})


# Los elementos de un conjunto **no pueden ser objetos mutables**, como listas, conjuntos o diccionarios:

# In[6]:


print({1,[2,3]})


# In[7]:


print({1,{2,3}})


# In[8]:


print({1,{"dos":2,"tres":3}})


# Pero sí puede tener elementos del tipo tupla:

# In[9]:


print({1,(2,3)})


# Los conjuntos **no tienen un índice**, esto es completamente diferente a lo que habíamos trabajado hasta el momento, y es natural dado que los elementos no tienen un orden:

# In[10]:


c = {1,2,3}


# In[11]:


c[0]


# Lo anterior implica que los elementos de los conjuntos no se pueden modificar, podemos agregar o quitar elementos pero no remplazar los que teníamos en la definición del conjunto:

# In[12]:


c2 = {"uno",2,3.0}


# Para **agregar un único elemento** empleamos el siguiente método:
# 

# In[13]:


c2.add(4)
c2


# Para **agregar múltiples elementos** a un conjunto empleamos el método `update`, teniendo presente que las repeticiones de elementos serán omitidas:

# In[14]:


c2.update([1,2,3])
c2


# Del mismo modo en que agregamos elementos, podemos quitarlos de nuestros conjuntos, con los métodos `remove` o `discard`. La diferencia entre ellos es que si al emplear el método `remove` el elemento no está en el conjunto, arroja error; pero con `discard` el conjunto no se ve afectado ni erroja errores:

# In[15]:


c2.remove(3)
c2


# In[16]:


c2.remove(5)
c2


# In[17]:


c2.discard(5)
c2


# In[18]:


c2.discard("uno")
c2


# El método `pop` elimina un elemento del conjunto, por lo general toma el primer elemento de éste luego del ordenamiento interno realizado:

# In[19]:


c2.pop()
c2


# Si queremos eliminar todos los elementos del conjunto, basta emplear el método `clear`:

# In[20]:


c2.clear()
c2


# ## Operaciones entre conjuntos
# Como hemos podido ver, los conjuntos que hemos trabajado en el cuderno se comportan de la misma manera que los conjuntos que usualmente trabajamos en matemáticas, además están las operaciones usuales entre ellos: **unión, intersección, diferencia** y **diferencia simétrica:**

# ### Unión
# 

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/619e631d894c1a0d819afcfe" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# Como bien sabemos, la unión de dos conjuntos se define como los el conjunto formado por los elementos que hacen parte de uno u otro. 
# Si definimos los conjuintos:

# In[21]:


u1 = {"a","e","i","o","u"}
u2 = {1,2,3,4}


# In[22]:


#La unión entre ellos se realiza así:
u1.union(u2)


# ### Intersección
# La intersección entre dos conjuntos, como bien sabemos, es el conjunto formado por los elementos que hay en común entre ellos:

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/619e739b3d3b610db6c57305" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# La forma de hacer dicha operación con los conjuntos de Python es la siguiente:

# In[23]:


i1 = {"a","e","i","o","u"}
i2 = {"a",2,3,"u"}
i3 = {"e","o",5}


# In[24]:


print(i1.intersection(i2))
print(i1.intersection(i3))
print(i3.intersection(i2))


# Por su lado el método `intersection_update`, remplaza el contenido de un conjunto por el de la intersección de él con otro conjunto dado

# In[25]:


#i1 será remplazado por la intersección {'e', 'o'}
i1.intersection_update(i3)
i1


# ### Diferencia
# La diferencia entre el conjunto A y el conjunto B, son los elementos que tiene A que no tiene B. Ésta operación, a diferencia de la unión y la intersección, no es conmutativa.

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/619e751275c5c20d8bdc9f92" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# El código que debe ejecutarse para hacer dicha operación entre dos conjuntos es el siguiente:

# In[26]:


d1 = {"h","o","l","a"}
d2 = {"b","u","e","n","a","s"}


# In[27]:


d1.difference(d2)


# In[28]:


d2.difference(d1)


# También podemos actualizar el contenido de un conjunto por la diferencia de él con otro conjunto, empleando el método `difference_update`, así:

# In[29]:


d2.difference_update(d1)
d2


# ### Diferencia simétrica
# Ésta operación, dados dos conjuntos A y B, se puede ver de dos maneras: La primera es como la diferencia de A y B unida con la diferencia de B con A. La segunda es como la diferencia entre la unión de A con B con la intersección de los dos conjuntos. La forma gráfica de entenderla es la siguiente:

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/619e751aae59f30d5cb30220" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# In[30]:


d1 = {"h","o","l","a"}
d2 = {"b","u","e","n","a","s"}


# In[31]:


d1.symmetric_difference(d2)


# In[32]:


d1.union(d2).difference(d1.intersection(d2))


# Con el método  `symmetric_difference_update`, podemos actualizar el contenido de un conjunto por la diferencia simétrica de él con otro conjunto, como podemos ver a continuación:

# In[33]:


d1.symmetric_difference_update(d2)
d1


# ### Ejercicios
# 1. Investiga la diferencia entre los objetos del tipo `frozenset` y los tipo `set`, que estudiamos en el presente cuaderno.

# # Diccionarios
# Los diccionarios son una colección ordenada de elementos, y para cada elemento en él existe una pareja `key : value` asociada.
# 
# Éstos objetos están optimizados para mostrar el "valor" cuando conocemos la "llave" o "clave".
# 
# La creación de éstos es muy sencilla, cada pareja `key : value` debe ir separada de la otra con coma, y las llaves deben ser objetos inmutables `str`, `int`, `float` o `tuple`, así:
# ```python
# {llave_1:valor_1, llave_2:valor_2, ... ,llave_n:valor_n}
# ```

# In[34]:


dic1 = {"Nombre":"Pepito","Apellido":"Pérez","Edad":20}


# Éstos también se pueden crear con la función `dict`

# In[35]:


dict([("nombre","Pepito"),("Apellido","Pérez"),("edad",20)])


# Los diccionarios pueden tener llaves de un único tipo, como en el ejemplo anterior, o pueden ser mixtas:

# In[36]:


dic2 = {1:"Arroz",2:"Aceite",3:20,4:1}


# Si deseamos acceder a un valor en especial, debemos seguir la idea de las listas, pero el índice se remplaza por el nombre de la llave así;
# ```python
# elemento = diccionario["llave"]
# ```
# por ejemplo:

# In[37]:


dic1["Nombre"]


# In[38]:


dic2[1]


# O con el método `get()`

# In[39]:


dic2.get(2)


# Para añadir elementos a un diccionario, basta con llamar al diccionario, la llave que deseamos modificar y asignar el valor deseado
# ```python
# diccionario["llave"] = valor
# ```

# In[40]:


dic2[5] = "pan"
dic2


# O mediante el método `update`, el cual como argumento tendrá la pareja `key : value` que se desea anexar en el diccionario:

# In[41]:


dic2.update({6:"chocolate"})
dic2


# ## Ejercicio:
# 1. Cree un diccionario que se llame notas, en el cual estén los nombres y los valores de cuatro notas obtenidas por "Pepito Pérez".

# In[42]:


Notas = {"Quiz1":3.5, "Parcial1":2.3, "AulaVirtual":5.0, "Taller1":4.3 }
Notas


# Ahora agregaremos el diccionario de antes, al primero que creamos

# In[43]:


dic1["Notas"] = Notas
dic1


# El ejemplo anterior nos muestra que podemos anidar diccionarios, es decir, un elemento de un diccionario puede ser otro diccionario.
# 
# Para acceder a dichos valores debemos llamar las dos llaves:

# In[44]:


dic1["Notas"]["Quiz1"]


# Para **modificar** los elementos del diccionario, accedemos a su llave y cambiamos el valor, por ejemplo:

# In[45]:


dic1["Edad"] = 15
dic1


# Si nuestro interés es eliminar elementos del diccionario tenemos dos métodos: `pop()` y `popitem()`.
# 
# El argumento de `pop()` es la llave del elemento que deseamos eliminar, mientras que `popitem()` no necesita de argumentos, ya que elimina un elemento al azar.

# In[46]:


dic2.pop(1,"Arroz")
dic2


# In[47]:


dic2.popitem()


# y al igual que con los conjuntos, el método `clear` permite eliminar todos los elementos del diccionario:

# In[48]:


dic2.clear()
dic2


# Los diccionarios también se pueden crear por comprensión, de la misma manera en la que hicimos las listas:

# In[49]:


cuadrados = {x:x**2 for x in range(0,5)}
cuadrados


# De los diccionarios también podemos extraer las listas de las llaves y de los valores, así:

# In[50]:


list(cuadrados.keys())


# In[51]:


list(cuadrados.values())


# ## Ejercicios
# 1. Cree un diccionario con la siguiente estructura:
# ```python
# Notas = {nombre : [lista_de_notas]}
# ```
# con por lo menos 5 estudiantes, los cuales cada uno deberá tener 6 notas numéricas entre 0 y 5.0
# 2. Cree una función la cual calcule la definitivad de los estudiantes del ejercicio anterior teniendo en cuenta que las tres primeras notas valen el 10% cada una, las dos siguientes 15% cada una y  la última nota el 40% de la nota definitiva.
