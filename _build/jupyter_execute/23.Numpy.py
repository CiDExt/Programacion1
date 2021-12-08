#!/usr/bin/env python
# coding: utf-8

# # Paquete Numpy

# :::::{important} Para tener presente
# 
# 
# [Numpy](https://numpy.org/) es la librería central para la computación científica en Python.
# 
# 
# ````{tabbed} ¿Para qué?
# 
# :::{admonition} Importante
# :class: tip
# Permite acceder a una gran cantidad de funciones matemáticas y crear arreglos multidimensionales de alta eficiencia
# :::
# ````
# 
# ````{tabbed} ¿Tiene documentación?
# 
# :::{admonition} Por supuesto:
# :class: tip 
# Es un paquete fácil de utilizar y posee una de las [documentaciones](https://numpy.org/doc/) más robustas de Python, quizás es uno de los paquetes más usados.
# :::
# ````
# 
# ````{tabbed} Sobre su poasado
# 
# :::{admonition}  ¿De dónde viene?
# :class: tip 
# Su ancestro es un paquete llamado Numeric, creado por [Jim Hugunin](https://en.wikipedia.org/wiki/Jim_Hugunin) y en 2005, con la incorporación de Numarray y varias modificaciones, [Travis Oliphant](https://en.wikipedia.org/wiki/Travis_Oliphant) lo transforma en Numpy.
# :::
# ````
# :::::

# En cuadernos anteriores ya hemos trabajado con algunos paquetes, por ejemplo `math`. Cuando se importan los paquetes y no se les asigna ningún alias, para usar una función de dicho paquete debe digitarse el nombre del paquete seguido de un punto y el nombre de la función, constante, etc., como por sigue:

# In[1]:


import math 


# In[2]:


math.pi


# Cuando se le pone un alias al paquete, se debe digitar el alias, seguido del punto y luego la función o constante:

# In[3]:


import math as loquequiera


# In[4]:


loquequiera.pi


# Para conocer la ayuda que tienen las funciones o constantes, podemos emplear el siguiente código:

# In[5]:


get_ipython().run_line_magic('pinfo', 'math.pi')


# Si queremos conocer todos los atributos o métodos que tiene el paquete, empleamos la función `dir`:

# In[6]:


dir(math)


# Ahora que ya recordamos como invocar paquetes, importaremos el paquete `numpy` con su alias `np`:

# In[7]:


import numpy as np


# Si queremos conocer la ayuda del paquete y el contenido del mismo, recuerda utilizar los siguientes comandos:
# ```python
# ?np
# dir(np)
# ```

# ## Conceptos básicos
# 
# El objeto más importante de numpy es el arreglo (`array`) multidimensional homogéneo, es decir, una tabla de elementos del mismo tipo, indexados por una tupla de enteros no negativos. En numpy las dimensiones del arreglo las llamaremos ejes (axes).
# 
# ### Ejemplo
# 
# Un elemento en $\mathbb{R}^n$ es un arreglo $n$-dimensional con un único eje:
# 
# 

# In[8]:


V = np.array([2,1,4])
print(V)


# In[9]:


W = np.array([3,1,2])
W


# Con los arreglos de `numpy` podemos hacer operaciones, como por ejemplo sumarlos y restarlos elemento a elemento:

# In[10]:


print(V+W)


# In[11]:


print(V-W)


# El contenido de los arreglos no necesariamente, debe ser numérico, pueden ser cadenas de texto o variables booleanas, etc.

# In[12]:


np.array(['a',1])


# In[13]:


BV=np.array([True,False,True])
print(BV)


# Cuando vimos listas multidimensionales, definimos lo que es una matriz. En este paquete tenemos un concepto análogo de lo que es una matriz de tamaño $n\times m$, es un arreglo de dos ejes:

# In[14]:


M=np.array([[1,0,1],[0,1,0],[2,1,3]])
print(M)


# Sobre este tipo de arreglos tenemos algunos métodos muy interesantes, como lo son: `dtype`, `shape`, `cumsum()` y `ndim`:

# In[15]:


M.dtype
#Para conocer el tipo de dato con el que estamos trabajando


# In[16]:


M.shape
#Para conocer las dimensiones del arreglo


# In[17]:


CS=M.cumsum()
CS
#Crea un arreglo, en el que la entrada i es la suma de todos los elementos hasta él en el arreglo


# En casos más generales, podríamos trabajar con un arreglo de matrices, o mejor conocido como tensor:

# In[18]:


T=np.array([[[[1,2,1,4],[3,2,4,1],[4,2,3,1]],[[1,2,3,1],[0,1,2,3],[1,4,5,6]]],[[[2,3,4,1],[1,1,2,1],[0,1,1,2]],[[1,2,3,1],[0,1,1,1],[2,1,3,1]]]])
print(T)


# In[19]:


T.shape


# In[20]:


T.dtype


# In[21]:


T.ndim


# La exploración de elementos que conforman al arreglo es similar a la de las listas de Python, con la salvedad de que en la matriz, o el tensor no tenemos una lista de listas, motivo por el cual podemos llamar a los elementos de una manera adicional:

# In[22]:


V


# In[23]:


V[1]


# In[24]:


print(M)


# In[25]:


M[1,1]


# In[26]:


#El comando anterior equivale a:
M[1][1]


# In[27]:


print(T)


# In[28]:


T[1]


# In[29]:


T[1,0]
#T[1][0]


# In[30]:


T[1,0,2]
#T[1][0][2]


# In[31]:


#Los tensores pueden contener texto:
TT=np.array([[[1,0,1],[0,1,0]],[[1,"0",3],[1,2,5]]])


# In[32]:


TT


# In[33]:


TT.shape


# In[34]:


TT[1,1,1]
#TT[1][1][1]


# Para extraer submatrices, podemos usar también índices de sublistas:

# In[35]:


M2 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(M2)


# In[36]:


M2[:2,1:3]
#Tomamos los elementos de las filas 0 y 1
#que estén en las columnas 1 y 2


# In[37]:


T=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]],[[25,26,27,28],[29,30,31,32],[33,34,35,36]]])
print(T)


# Ahora extraeremos de las dos primeras matrices, lo que esté desde la fila 1 en adelante y lo que esté en las columnas 1 y 2.

# In[38]:


T[:2,1:,1:3]


# También podemos extraer elementos utilizando listas así:
# ```python
# nombre_del_arreglo[[índices_de_filas],[índices_de_columnas]]
# ```

# In[39]:


#Recordemos:
print(M2)


# In[40]:


M2[[0,2],[1,3]]


# Ahora extraeremos los valores 1,6,11 y 8 de la matriz M2:

# In[41]:


M2[[0,1,2,1],[0,1,2,3]]


# Los elementos se pueden repetir, por ejemplo:

# In[42]:


M2[:,[0,1,2,2,1,1,2,2]]


# Si deseamos extraer filas:

# In[43]:


M2[np.array([0,2])]


# Si lo que queremos extraer son columnas:

# In[44]:


M2[:,np.array([2,0])]


# Recordemos algunos de los comandos vistos de `numpy`:
# 
# * `.ndim` (número de ejes del arreglo)

# In[45]:


V.ndim


# In[46]:


M.ndim


# In[47]:


T.ndim


# * `.shape` (La dimensión del arreglo. Obtenemos una tupla de enteros)

# In[48]:


V.shape


# In[49]:


M.shape


# In[50]:


T.shape


# * `.size` (El número total de elementos que conforman al arreglo)

# In[51]:


V.size


# In[52]:


T.size


# In[53]:


M.size


# In[54]:


print(M)


# * `.concatenate` (concatena dos matrices, bien sea por filas o columnas)

# In[55]:


np.concatenate((M,M),axis=0)
#Concatena por filas


# In[56]:


np.concatenate((M,M),axis=1)
#Concatena por columnas


# In[57]:


N=np.concatenate((M,np.array([[0],[0],[0]])),axis=1)
N


# Podemos intercambiar filas o columnas, seleccionando el orden que deseamos en la sublista:

# In[58]:


N[:,[0,1,3,2]]


# * `.dtype` (el tipo de lementos en el arreglo)

# In[59]:


M.dtype


# In[60]:


A=np.array([3<2,2<3,4<5])
print(A)


# In[61]:


A.dtype


# In[62]:


TT2=np.array([A,V])
print(TT2)


# In[63]:


TT2.dtype


# ## Creación de algunos arreglos clásicos
# 
# Tenemos la oportunidad de utilizar algunas funciones de Numpy para generar arreglos y matrices ampliamente utilizadas:
# 

# In[64]:


ceros=np.zeros((2,3))
print(ceros)


# In[65]:


unos=np.ones((2,2,3))
print(unos)


# In[66]:


constante=np.full((4,3),5)
print(constante)


# In[67]:


constante2=np.full((4,3),5<2) #Creamos una matriz de 4x3 llena de False
constante2[1,1]=True #Asignamos el valor True a la entrada
print(constante2)


# In[68]:


constante3=np.full((4,3),"Hola")
print(constante3)


# In[69]:


identidad=np.eye(6,5)
print(identidad)


# Unas matrices muy particulares son las que tienen su contenido generado de manera aleatoria:

# In[70]:


aleatoria = np.random.random((2,2))  
print(aleatoria) 


# In[71]:


get_ipython().run_line_magic('pinfo', 'np.random')


# ## Operaciones entre matrices
# Las matrices son un objeto que se abordará profundamente en el curso de Álgebra Lineal, pero te presentaremos algunas de sus operaciones ya que siguen las ideas que hemos visto en las listas y en los arreglos:

# In[72]:


import numpy as np
x = np.array([[1,2,3],[4,5,6]], dtype=np.float64)
y = np.array([[7,8,9],[9,8,7]])
z=np.array([[1,1],[2,1]])


# In[73]:


print(x)
print(y)
print(z)


# La suma entre matrices, se realiza de la misma forma en que se hace con las listas, elemento a elemento:

# In[74]:


print(x + y)


# Del mismo modo ocurre con la resta:

# In[75]:


print(x - y)


# Algunas operaciones no tan comunes son las siguientes:

# In[76]:


print(x*y) #multiplicación elemento a elemento


# In[77]:


print(x / y) #división elemento a elemento


# In[78]:


print(y)
print(np.sqrt(y))  #raíz cuadrada elemento a elemento


# In[79]:


print(np.transpose(y)) #transpuesta (las filas se vuelven columnas)


# In[80]:


print(y.T) #transpuesta


# (m,k) @ (k,n)=(m,n)

# In[81]:


print(x@np.transpose(y)) #multiplicación de matrices


# In[82]:


print(np.transpose(y)@x)


# In[83]:


print(x.dot(y.T)) #multiplicación de matrices


# In[84]:


print(x)


# In[85]:


print(np.sum(x))   #suma de todos los elementos
print(np.sum(x, axis=0))  #suma de elementos por columnas
print(np.sum(x, axis=1))   #suma de elementos por filas


# Mas funciones [aquí](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)

# ## Operaciones especiales
# 
# En ocasiones tenemos que hacer algunas operaciones que no tienen en cuenta la forma de las matrices o que involucran matrices de diferentes tamaños. Aquí algunos ejemplos:

# In[86]:


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(x)


# Para sumar la misma constante a cada elemento del arreglo:

# In[87]:


print(x+10)


# In[88]:


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(x)
v = np.array(np.transpose([[1, 0, 1,1]]))
print(v)


# In[89]:


x+v


# In[90]:


x+1


# * Suma de un vector a una fila

# In[91]:


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(x)
v = np.array([1, 0, 1])
print(v)


# In[92]:


x[0]=x[0]+v
print(x)


# * Multiplicar una fila por un número real (escalar)

# In[93]:


x[0]=x[0]*2
print(x)


# * Intercambiar filas (empleando una variable auxiliar)

# In[94]:


fc=x.copy()
x[1]=x[0]
x[0]=fc[1]
print(x)


# ### Operaciones entre matrices de diferente tamaño (Broadcasting)

# **NumPy** transforma los arreglos involucrados para que tengan el mismo tamaño y, por tanto, puedan someterse a las operaciones por elementos sin generar excepciones.

# In[95]:


a = np.arange(0.2, 40.2, 10.5)
a.shape


# In[96]:


print(a)


# In[97]:


a = a[:, np.newaxis]  #Adicionamos un eje
print(a.shape)
a


# In[98]:


b = np.array([0, 1, 2])
print(b)


# Ahora, sumaremos a cada columna de la matriz *a* el arreglo *b* definido en la línea anterior:

# In[99]:


a+b


# Las siguientes matrices sirven como otro ejemplo para este tipo de operaciones:

# In[100]:


A=np.array([[0,1],[1,2]])
B=np.array([[2,1],[1,2]])


# In[101]:


A.shape


# In[102]:


A= A[:,:, np.newaxis] 


# In[103]:


A.shape


# In[104]:


A


# In[105]:


A+B


# Nota que a la matriz *B* se le ha sumado en cada columna, la columna [0,1] y luego [1,2].

# # Herramientas interactivas `ipywidgets`
# 
# Otro paquete que será transversal en este curso y nos permitira crear interfaces interesantes para nuestros estudiantes es [ipywidgets](https://ipywidgets.readthedocs.io/en/stable/). Para instalar desde el cuaderno escriba:

# In[106]:


get_ipython().system('pip install ipywidgets')


# In[107]:


#Debemos habilitar la extensión en nuestro entorno:
get_ipython().system('jupyter nbextension enable --py widgetsnbextension')


# Importemos el paquete

# In[108]:


from ipywidgets import interact
import ipywidgets as widgets


# La herramienta más básica de este paquete es la función `interact`. En el siguiente ejemplo veremos su utilidad:

# In[109]:


def f(x):
    print("El valor que escogió es", x)
    return x


# In[110]:


f(4)


# In[111]:


interact(f, x=1.2)


# In[112]:


interact(f, x=True)


# In[113]:


interact(f, x={0:'Elemento 1',1:'Elemento 2'})


# In[114]:


interact(f, x='Soy interactivo')


# Notemos que cada vez que se cambia el argumento de la función, el elemento interactivo cambia de inmediato, sin necesidad que nosotros lo indiquemos.
# 
# Veamos otro par de ejemplos:

# In[115]:


def g(x):
    y=x+5
    print(x,"+",5,"=",y)
    return y


# In[116]:


g(8)


# In[117]:


interact(g, x=1.2)
#Objeto interactivo: Slider tipo float


# In[118]:


interact(g, x=1)
#Objeto interactivo: Slider tipo int


# In[119]:


def nombrelargoocorto(t):
    if len(t)>=7:
        print(t+" es un nombre muy largo")
        z="largo"
    else:
        print(t+" es un nombre corto")
        z="corto"
    return z


# In[120]:


nombrelargoocorto("Benjamin")


# In[121]:


interact(nombrelargoocorto, t="Pepito")
#Objeto interactivo: Caja de texto


# In[122]:


interact(nombrelargoocorto, t=["Pepito","Luis","Gustavo","Felipe"])
#Objeto interactivo: Menú desplegable


# Los elementos que permiten la interacción con el usuario son los widgets, una lista completa de ellos se encuentra [aquí.](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html)

# A continuación hacemos un cambio sobre el widget:

# In[123]:


interact(f, x=widgets.IntText(
    value=7,
    description='Escriba un número: ',
    disabled=False
));


# In[124]:


interact()


# ## Una primera aplicación
# 
# Ya que conocemos algo de Numpy y ipywidgets vamos a crear un ejemplo muy sencillo para calcular algunos estadísticos elementales de una lista de valores:

# In[125]:


def estadisticos(x):
    L=x.split()
    L=[float(i) for i in L]        
    x=np.array(list(L))
    print("La media es", np.mean(x))
    print("La mediana es", np.median(x))
    print("La varianza poblacional es", np.var(x))
    print("La varianza muestral es", np.var(x,ddof=1))
    print("La desviación estándar poblacional es", np.std(x))
    print("La desviación estándar muestral es", np.std(x,ddof=1))
    return


# In[126]:


estadisticos("1 2 3")


# Evalue los estadísticos del conjunto de datos [1,1,2,3] y compruebelo con la herramienta:

# In[127]:


estadisticos("1 2 3 4 5 7 8 3 1 3 4 1 3 4 8 0 9")


# In[128]:


interact(estadisticos,x="1 2 3")


# In[129]:


def estadisticos(x):
    try:
        L=x.split()
        L=[float(i) for i in L]        
        x=np.array(list(L))
        print("La media es", np.mean(x))
        print("La mediana es", np.median(x))
        print("La varianza poblacional es", np.var(x))
        print("La varianza muestral es", np.var(x,ddof=1))
        print("La desviación estándar poblacional es", np.std(x))
        print("La desviación estándar muestral es", np.std(x,ddof=1))
    except:
        print("Cuidado con lo que escribe, solo se admiten valores numéricos")
    return


# In[130]:


interact(estadisticos,x="1 2 3")


# ## Ejercicio
# 1. Crea una función, para luego hacer un elemento interactivo con ella, de tal modo que se digite una cantidad que sea el cuadrado de un número entero de datos y esta lo escriba como una matriz del tamaño adecuado, es decir, si se digitan 4 elementos, la respuesta de la función debe ser una matriz de tamaño 2x2.

# In[ ]:




