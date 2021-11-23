#!/usr/bin/env python
# coding: utf-8

# # Más sobre listas

# :::::{important} ¿Qué debemos recordar?
# 
# 
# Sobre listas debemos tener claro lo siguiente:
# 
# 
# ````{tabbed} Como definir listas
# 
# :::{admonition} Recordemos...
# :class: tip
# ```python
# l = [0, 1, 2, 3]
# ```
# :::
# ````
# 
# ````{tabbed} Índices en las listas
# :::{admonition} Recordemos...
# :class: tip 
# Los índices inician en $0$ y aumentan de uno en uno, algunos índices negativos también se pueden utilizar, al emplear estos valores estamos indicando que la lista se recorre en orden inverso, es decir, el índice -1 es el último elemento de la lista, el -2 es el penúltimo, etc., como podemos ver a continuación:
# <img src="https://github.com/MRippe7/CienciaDatos/blob/main/Imagenes/listas.png?raw=true"  width=300 >
# :::
# ````
# 
# ````{tabbed} Objetos mutables
# 
# :::{warning}  ¿Cómo así?
# El contenido de las listas se puede modificar, como por ejemplo con la lista anterior:
# ```python
# l[0]=[10]
# ```
# :::
# ````
# :::::

# ## Sub-listas
# Hay  oportunidades en las que nuestra necesidad sea extraer una sub-lista de la lista que tenemos, por ejemplo, de la lista `l = [0, 1, 2, 3, 4, 5]` requerimos los elementos desde el índice 2 hasta el 4 de nuestra lista, o los primeros $3$ elementos  o los últimos $4$, éstas tres sub-listas se obtienen así:

# In[1]:


l = [0, 1, 2, 3, 4, 5]


# In[2]:


subl = l[2:5]
subl


# In[3]:


primeros = l[:3]
primeros


# In[4]:


ultimos = l[2:]
#para mayor facilidad, podemos emplear los índices negativos
#ultimos = l[-4:] 
ultimos


# Es decir, para extraer una sub-lista basta con hacerlo de la siguiente manera:
# ```python
# lista[índice_inicial:índice_final]
# ```
# Si el ínidice inicial se omite, la lista se considerará desde el primer elemento, de manera análoga ocurre con el índice final, si se omite la sub-lista llegará hasta el último elemento de la lista original.
# 
# Los valores negativos se emplean cuando se desea hablar de los últimos elementos de una lista, con el fin de evitar confusiones.
# 
# ### Ejercicio:
# Extraiga tres sub-listas de una lista cuyos valores coinciden con el valor del índice, en ellas deberán estar:
# 1. Los primeros 20 elementos.
# 2. Los elementos desde le índice 100 hasta el índice 200.
# 3. Los últimos 30 elementos.
# 
# Calcule el promedio de cada una de éstas listas.
# 
# ## Eliminando entradas de una lista
# En otras ocasiones es muy necesario eliminar elementos de las listas, por ejemplo, vamos a eliminar el tercer elemento de la lista `M = [0, 1, 2, 3, 'cuatro', 1, 1, 5.1, id(l)]` 

# In[5]:


M = [0, 1, 2, 3, 'cuatro', 1, 1, 5.1, id(l)]


# In[6]:


del M[2]
M


# Es decir, al seguir la línea de comando 
# ```python
# del lista[índice_que_se_desea_eliminar]
# ```
# se borra la entrada de la lista.

# ## Listas por Comprensión:
# Las listas se pueden crear de una manera un poco más avanzada, empleando la característica que las define. Si por ejemplo, deseamos crear la lista de los primeros $5$ números pares podemos emplear el siguiente código:

# In[7]:


pares = [2*i for i in range(5)]
pares


# La línea anterior es equivalente al siguiente bloque:

# In[8]:


pares = []
for i in range(5):
    pares.append(2*i)
pares


# De momento, podemos decir que las listas por comprensión se crean de la siguiente manera:
# ```python
# [expresión_que_depende_de_i for i in lista_en_la_que_varía_i]
# ```
# Pero en ocasiones, es necesario introducir alguna condición ya que no requerimos de todos los valores de la lista. Por ejemplo, si en la lista anterior deseamos omitir los múltiplos de $3$, la siguiente línea nos sería útil:

# In[9]:


pares2 = [2*i for i in range(5) if i%3!=0]
pares2


# Esta simple línea equivale a redactar el siguiente bloque:

# In[10]:


pares2 = []
for i in range(5):
    if i%3!=0:
        pares2.append(2*i)
pares2


# Como podemos observar, las listas por comprensión nos facilitan la escritura de listas, pero debemos tener muy claras la expresión que tienen en común todos los elementos de ella y las posibles condiciones para poder agregarlos o no. De manera general las listas por comprensión se escribren así:
# ```python
# [expresión_que_depende_de_i for i in lista_en_la_que_varía_i if condiciones] 
# ```
# ### Ejercicio:
# 1. Crea una lista por comprensión cuya lista que recorre sea una cadena de caracteres arbitraria, y almacene las consonantes únicamente.

# Además de las condiciones anteriores, podemos crear listas por comprensión con ciclos anidados, como por ejemplo:

# In[11]:


nombres1 = ['Luis' ,'Pedro' ,'Michele', 'Albert', 'María José']
nombres2 = ['Luisa', 'María José' ,'Michele', 'Ana', 'Jenny']
comunes = [a for a in nombres1 for b in nombres2 if a == b]
comunes


# De manera general, las listas por comprensión se pueden crear de la siguiente manera:
# ```python
# [expresión for a in lista_para_a (opcional if condición_para_a)
#            for b in lista_para_b (opcional if condición_para_b)
#            for c in lista_para_c (opcional if condición_para_c)
#            ...]
# ```

# ### Ejercicio:
# 1. Crea dos listas de números enteros y haga una lista por comprensión en la que se almacenen los productos de los números en ellas que no sean pares.

# ## Tuplas
# Las tuplas, a diferencia de las listas, son objetos inmutables en los cuales se almacenan datos, bien sean del mismo o de diferentes tipos, siendo éste último el uso más frecuente.
# 
# De modo que definiremos nuestra primera tupa:

# In[12]:


temperatura = 'Enero', '01', 19
#Equivalentemente
#t = ('Enero', '01', 19)
temperatura


# Sin importar como la definamos: siempre se visualizarán sus elementos entre paréntesis y separados por una coma.   
# 
# Para conocer la cantidad de elementos que hay en una tupla, empleamos la misma función que para las listas, la función 
# ```python 
# len(tupla)
# ```
# así:

# In[13]:


len(temperatura)


# Si deseamos definir una tupla con un único elemento, debemos hacerlo de la siguiente manera:

# In[14]:


tupla1elemento = 23, #Observa la coma
tupla1elemento


# La coma es la que indica que es una tupla, ya que se si hace sin ella, incluso entre paréntesis, se guardará el entero 23 y no la tupla cuyo único elemento es el 23.
# 
# Para acceder a la información almacenada en las diferentes entradas de una tupla, lo hacemos de la misma manera que lo hicimos con las listas, es decir, `tupla[índice]`, así:

# In[15]:


temperatura[0]


# y éstas se pueden operar:

# In[16]:


'La temperatura máxima en Bogotá el '+ temperatura[1]+' de '+temperatura[0]+' del 2021 fue de '+str(temperatura[-1])


# ¿Qué pasa si intentamos modificar una entrada de una tupla?

# In[17]:


temperatura[0]='hola'


# Como lo comentamos antes, las tuplas son **inmutables**.
# 
# Para agregar elementos a una tupla empleamos el operador `+=`, de la misma manera que lo hicimos con las listas. Para las tuplas no disponemos del método `append`.

# In[18]:


tupla1elemento += ('a',)
tupla1elemento


# Como hemos recalcado las tuplas son inmutables, pero pueden contener elementos mutables, por ejemplo:

# In[19]:


tupla1elemento += ([1,2,3,4],)
tupla1elemento


# In[20]:


tupla1elemento[2]=1
#genererá un error ya que no podemos modificar el elemento de la tupla


# In[21]:


#Pero podemos modificar la lista que está dentro de la tupla
tupla1elemento[2][3]='cuatro'
tupla1elemento


# En este cuaderno, hemos estudiado las herramientas básicas sobre las listas y las tuplas, para así poder tener un mejor desempeño a la hora de elaborar nuestros programas.

# ## Métodos de ordenamiento
# Una de las primeras tareas que se abordan cuando se trabaja con listas es la de **ordenar**, ya que para diversas labores es necesario que los elementos estén dispuestos de ésta manera. 
# 
# Para llevar a cabo ésta tarea existen diferentes formas de hacerlo, una forma conocida es mediante el **método burbuja**, el cual se basa en simples comparaciones e intercambios.
# 
# ```
#     Una lista de n valores se recorre n-1 veces, en las cuales se irán comparando los términos de izquierda a derecha con el siguiente, de tal manera que, si el i-ésimo término es mayor que el que se ubica en la posición i+1, éstos se intercambian de lo contrario se dejan tal cual. Las comparaciones se van reduciendo ya que en la parte derecha de la lista se van almacenando los términos mayores con el orden deseado.
# ```
# 
# Por ejemplo, en la lista que definimos anteriormente, al aplicar las comparaciones del método de la burbuja en la primera iteración, obtenemos lo siguiente:
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/burbuja.png?raw=true">
# 
# El nombre de éste método es debido a que las comparaciones se hacen en pequeñas burbujas de toda la lista.
# 
# Una implementación de éste método se puede consultar en la siguiente función:

# In[22]:


from time import time


# In[23]:


def burbuja(l):  
    tiempo_inicial = time()
    for i in range(1,len(l)-1):
        for j in range(len(l)-i-1):
            if l[j]>l[j+1]:
                l[j],l[j+1] = l[j+1],l[j]
    tiempo_transcurrido = time() - tiempo_inicial
    print('El proceso tardó {0} segundos'.format(tiempo_transcurrido))
    return l    


# En nuestro código hay dos líneas muy particulares `tiempo_inicial = time()` y `tiempo_transcurrido = time() - tiempo_inicial`, éstas permiten calcular el tiempo transcurrido en los cálculos para ordenar la lista. La función `time()` está disponible gracias a la importación de la libreria con el mismo nombre.
# 
# Hagamos un ensayo con una lista corta:

# In[24]:


burbuja([5,7,3,1,1,3,16])


# Ahora ordenaremos una lista de $1000$ elementos aleatorios, para tal fin, lo primero que haremos es definirla:

# In[25]:


import random
random.seed(2022)
aleatorios = [random.randint(0,1000) for i in range(1000)]


# In[26]:


burbuja(aleatorios)


# Otra forma, quizá un poco más *artesanal*, se puede expresar de la siguiente manera:
# ```
# Busque el menor elemento de toda la lista, almacene dicho valor como el primer elemento de otra lista y elimine el valor de la lista original. De la nueva lista busque el elemento menor, guardelo como el siguiente valor en la lista creada y elimine el valor de la lista original. Repita el proceso hasta que no queden elementos en la lista original.
# ```
# Esta tarea la podemos ver programada en el siguiente bloque de código:

# In[27]:


def ordenamiento1(l):
    tiempo_inicial = time()
    m = []
    for i in range(len(l)):
        Min = l[0]
        for j in l:
            if j < Min:
                Min = j
        m.append(Min)
        del l[l.index(Min)]
    tiempo_transcurrido = time() - tiempo_inicial
    print('El proceso tardó {0} segundos'.format(tiempo_transcurrido))
    return m    


# Probemos con la lista corta:

# In[28]:


ordenamiento1([5,7,3,1,1,3,16])


# In[29]:


random.seed(2022)
aleatorios = [random.randint(0,1000) for i in range(1000)]
#aleatorios


# In[30]:


ordenamiento1(aleatorios)


# En Python existe una manera natural de hacerlo y es con la función `sorted` o con el método `lista.sort()`, en los cuales subyace el **método Timsort**, los cuales son supremamente eficientes:

# In[31]:


l = [5,7,3,1,1,3,16]
sorted(l)


# In[32]:


l = [5,7,3,1,1,3,16]
l.sort()
l


# Estas funciones tienen argumentos que pueden ser de gran ayuda para nosotros, por ejemplo, ordenar de mayor a menor la lista, requeriría definir una función nueva para nosotros, pero con éstas predefinidas basta con escribir lo siguiente:

# In[33]:


l = [5,7,3,1,1,3,16]
l.sort(reverse=True)
l


# ### Ejercicio:
# 1. Como hemos visto hay diferentes métodos para ordenar listas, unos más eficientes que otros. Busque un método diferente a los expuestos en el cuaderno, haga una un resumen en palabras del método y escriba una función que permita hacer esta tarea.
# 2. Cree una lista de 400 valores, en los cuales estén almacenadas las ventas de la última semana de un almacén, aplique los métodos vistos en clase y el que usted construyó y determine cual es más eficiente sobre dicha lista.

# ## Filtros
# En muchas ocasiones nos será necesario elegir algunos valores de una lista que cumplan con un cierto criterio, por ejemplo de la lista `[10,20,50,70,90,60,40,30,40,8,95,74,69,45]`, extraigamos los valores que son mayores o iguales a 50:

# In[34]:


lista = [10,20,50,70,90,60,40,30,40,8,95,74,69,45]
lista_filtrada = []
for i in lista:
    if i >= 50:
        lista_filtrada.append(i)
lista_filtrada        


# In[35]:


lfiltrada = filter(lambda i:i>= 50,lista)


# Si observamos el resultado de un filtro, éste un objeto tipo `filter`, para poder ver su contenido empleamos el comando `list`, así:

# In[36]:


list(lfiltrada)


# Si se llega a dar el caso que el filtro viene dado como el resultado de una función, primero debemos definir dicha función y luego aplicamos el filto, así:

# In[37]:


random.seed(2022)
lista = [random.randint(0,250) for i in range(100)]


# In[38]:


def par(x):
    return x%2==0


# In[39]:


len(list(filter(par,lista)))


# La escritura de un filtro, es en gerenal, la siguiente:
# ```python
# filter(función,lista)
# ```
# ### Ejercicios
# 1. Use la lista de las 400 ventas de la semana anterior creada anteriormente. Calcule el promedio de dicha lista y aplique un filtro sobre ella para conocer la cantidad de ventas que están por encima de dicho valor y las que están por debajo de él. Guarda estas listas como *ventassobreprom* y *ventasbajoprom*, respectivamente.
# 2. Cree una función que filtre las vocales y aplique el filtro sobre la siguiente cadena: 
# ```
# En un lugar de la Mancha, de cuyo nombre no quiero acordarme, no ha mucho tiempo que vivía un hidalgo de los de lanza en astillero, adarga antigua, rocín flaco y galgo corredor. Una olla de algo más vaca que carnero, salpicón las más noches, duelos y quebrantos los sábados, lantejas los viernes, algún palomino de añadidura los domingos, consumían las tres partes de su hacienda. El resto della concluían sayo de velarte, calzas de velludo para las fiestas, con sus pantuflos de lo mesmo, y los días de entresemana se honraba con su vellorí de lo más fino. Tenía en su casa una ama que pasaba de los cuarenta y una sobrina que no llegaba a los veinte, y un mozo de campo y plaza que así ensillaba el rocín como tomaba la podadera. Frisaba la edad de nuestro hidalgo con los cincuenta años. Era de complexión recia, seco de carnes, enjuto de rostro, gran madrugador y amigo de la caza. Quieren decir que tenía el sobrenombre de «Quijada», o «Quesada», que en esto hay alguna diferencia en los autores que deste caso escriben, aunque por conjeturas verisímilesII se deja entender que se llamaba «Quijana»III, . Pero esto importa poco a nuestro cuento: basta que en la narración dél no se salga un punto de la verdad.
#                                                                 Don quijote de la mancha - Miguel de Cervantes Saavedra
# ```
# ## Mapear
# En otras oportunidades necesitaremos aplicar una función sobre todos los elementos de la lista, es allí cuando aplicamos la función `map`. El resultado de ésta función  es un objeto tipo `map` y el cual se puede volver una lista de la misma manera como hicimos con los filtros, por ejemplo

# In[40]:


def f1(x):
    return x**2+1


# In[41]:


list(map(f1,[1,2,3,4,5]))


# La diferencia entre `map`y `filter`, es que en `map` aplicamos una función sobre cada elemento de la lista y en `filter` buscamos un criterio de selección booleano.
# 
# Los mapeos se pueden aplicar sobre cadenas de caracteres, por ejemplo:

# In[42]:


cadena = list('Hoy es un gran día para aprender más herramientas de programación')


# In[43]:


list(map(lambda x:x.upper(),cadena))


# También podemos aplicar los mapeos sobre varias listas, siempre que la función lo permita:

# In[44]:


nume1 = [1, 2, 3]
nume2 = [4, 5, 6]
  
result = map(lambda x, y: x + y, nume1, nume2)
print(list(result))


# ### Ejercicio
# 1. Aplica un mapeo sobre las listas ventassobreprom y ventasbajoprom, para obtener los valores de las ventas sin IVA, suponiendo que todos los productos consumidos están gravados con éste impuesto. A estas listas sería convieniente nombrarlas *ventassobreprom_iva* y *ventasbajoprom_iva*.

# ## Reducir
# La función `reduce` del paquete `functools`, es una útil herramienta cuando deseamos aplicar una función sobre una lista y sus resultados de manera sucesiva. Por ejemplo, para calcular la suma de los elementos de una lista sabemos que existe la función `sum`, pero de manera alternativa podemos ejecutar el siguiente código:

# In[45]:


from functools import reduce


# In[46]:


reduce(lambda x,y:x+y,[1,2,3,4,5])


# In[47]:


def fun(x,y):
    return x+y


# In[48]:


reduce(fun,[1,2,3,4,5])


# Notemos que la función `reduce` se aplica de izquierda a derecha, y la función que se aplica sobre la lista debe tener dos argumentos y su resultado es la acumulación de los resultados obtenidos de dicha función sobre la lista.
# 
# El siguiente diagrama ayuda a entender de mejor manera su funcionamiento:
# 
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/reduce.png?raw=true" style="width:70%;">
# 
# `reduce` tiene un argumento adicional, el cual es opcional, dicho argumento es el valor inicial, por ejemplo, el siguiente resultado inicia en $10$ y a eso le suma $1$, al resultado luego le suma $2$ y así hasta agotar la lista:
# 

# In[49]:


reduce(fun,[1,2,3,4,5],10)


# En general las reducciones se escriben de la siguiente manera:
# ```python
# from functools import reduce
# reduce(función,lista,valor_inicial(opcional))
# ```

# ### Ejercicios:
# 1. Halle el mínimo de las listas *ventassobreprom_iva* y *ventasbajoprom_iva*, empleando `reduce` y una función lambda.
# 2. Halle el máximo de las listas *ventassobreprom_iva* y *ventasbajoprom_iva*, empleando `reduce` y una función lambda.
# 3. Cree una función de dos argumentos ($1$ o $0$) que verifique la tabla de verdad del operador lógico **Y**. Utilice un `reduce` sobre diferentes listas de unos y ceros. ¿Qué puede concluir?
# 4. Cree una función de dos argumentos ($1$ o $0$) que verifique la tabla de verdad del operador lógico **O**. Utilice un `reduce` sobre diferentes listas de unos y ceros. ¿Qué puede concluir?
# 
# Estas herramientas que hemos adquirido durante el cuaderno, serán de gran utilidad en cursos futuros, en especial cuando se aborden las bases de datos. Por ello es fundamental que se reconozcan las diferencias entre los filtros, mapeos y reducciones:
# 
# | Función   |      Descripción      |  Argumentos |
# |:----------:|:-------------:|:------:|
# | filtro |  verifica si se cumple una y extrae una sublista de la lista dada | función, lista |
# | mapeo |    Aplica una función a cada elemento de una lista dada   |   función, lista |
# | reducción | Aplica una función sobre una lista de manera reiterada, hasta reducirla a un único valor |   función, lista, valor inicial(opcional) |
# 
# 
# ____
# **Observación:** Los filtros, mapeos y reducciones que vimos específicamente para listas, se pueden aplicar también sobre cualquier objeto iterable, es decir, *listas*, *tuplas*, *diccionarios* y *conjuntos*.
# ____

# ## Listas n-dimensionales
# 
# Para darnos una idea, iniciaremos tratando lo que son listas bidimensionales.
# 
# Consideremos las siguientes listas:

# In[50]:


l1 = [0,1,2,3]
l2 = [10,11,12,13]
l3 = [20,21,22,23]


# Partiendo de ellas, podemos obtener la siguiente lista:

# In[51]:


L = [l1,l2,l3]
L


# `L` es una lista, y sus elementos son listas, es decir, es una lista de listas. Para acceder a un elemento en particular necesitamos tener dos índices, uno para acceder a la lista `L` y otro para la lista en la cual nos ubiquemos (`l1`, `l2`, `l3`). Por ejemplo, para acceder a la primera lista y a su primer elemento escribimos así:

# In[52]:


L[0][0]


# Para entender un poco mejor la distribución de las listas de listas, podemos visualizarlas como una *matriz*, en la que, las filas van indicadas por el primer índice y las columnas por el segundo: 
# 
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/listasn1.png?raw=true"  width=600 >
# 
# Siguiendo esta idea, si quisiéramos sumar el elemento de la fila $1$ columna $2$, con el de la fila $2$ columna $1$, emplearíamos la siguiente línea de código:

# In[53]:


L[1][2]+L[2][1]


# Para un arreglo arbitrario `a`, la idea es la misma, el primer índice es para las filas y el segundo para las columnas:
# 
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/listasn2.png?raw=true"  width=800 >
# 
# 

# Esta misma idea se puede ampliar a tres dimensiones y más, en tres dimensiones podemos todavía visualizar la organización de los datos empleando un cubo, así:
# <img src="https://github.com/CiDExt/Programacion1/blob/master/images/listasn3.png?raw=true" width="600" >
# es decir, es un arreglo de matrices, como por ejemplo:

# In[1]:


Cubo = [[[1,2],[3,4],[5,6]],[[7,8,9],[10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]]]


# In[2]:


Cubo


# In[3]:


Cubo[1]


# In[4]:


Cubo[1][0]


# In[5]:


Cubo[1][0][2]


# # Cierre
# Las listas y las tuplas tienen una gran cantidad de aplicaciones, por eso entender el momento y la forma de usarlas es muy importante, ya que las listas son objetos mutables, mientras que las tuplas no, es por esto que si necesitamos modificar alguna de nuestras entradas luego de haber definido el objeto, se debe emplear una lista, pero si deseamos "proteger" las entradas de nuesto objeto, debemos emplear una tupla.

# In[ ]:




