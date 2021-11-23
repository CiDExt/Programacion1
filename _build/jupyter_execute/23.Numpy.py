#!/usr/bin/env python
# coding: utf-8

# <h1>Table of Contents<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Conceptos-básicos" data-toc-modified-id="Conceptos-básicos-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Conceptos básicos</a></span></li><li><span><a href="#Creación-de-algunos-arreglos-clásicos" data-toc-modified-id="Creación-de-algunos-arreglos-clásicos-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Creación de algunos arreglos clásicos</a></span></li><li><span><a href="#Operaciones-elementales" data-toc-modified-id="Operaciones-elementales-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Operaciones elementales</a></span></li><li><span><a href="#Operaciones-especiales" data-toc-modified-id="Operaciones-especiales-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Operaciones especiales</a></span><ul class="toc-item"><li><span><a href="#Operaciones-entre-matrices-de-diferente-tamaño-(Broadcasting)" data-toc-modified-id="Operaciones-entre-matrices-de-diferente-tamaño-(Broadcasting)-4.1"><span class="toc-item-num">4.1&nbsp;&nbsp;</span>Operaciones entre matrices de diferente tamaño (Broadcasting)</a></span></li></ul></li><li><span><a href="#Módulo-de-álgebra-lineal" data-toc-modified-id="Módulo-de-álgebra-lineal-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Módulo de álgebra lineal</a></span><ul class="toc-item"><li><span><a href="#Más-matrices-especiales" data-toc-modified-id="Más-matrices-especiales-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Más matrices especiales</a></span></li></ul></li><li><span><a href="#Módulo-linalg" data-toc-modified-id="Módulo-linalg-6"><span class="toc-item-num">6&nbsp;&nbsp;</span>Módulo <code>linalg</code></a></span></li><li><span><a href="#Una-primera-aplicación" data-toc-modified-id="Una-primera-aplicación-7"><span class="toc-item-num">7&nbsp;&nbsp;</span>Una primera aplicación</a></span></li></ul></div>

# # Paquete Numpy
# 
# *Carlos Isaac Zainea Maya*
# 
# 
# [Numpy](https://numpy.org/) es la librería central para la computación científica en Python, nos permite acceder a una gran cantidad de funciones matemáticas y crear arreglos multidimensionales de alta eficiencia. Es un paquete facil de utilizar y posee una de las [documentaciones](https://numpy.org/doc/) más robustas de Python, quizás es uno de los paquetes más usados.  Su ancestro es un paquete llamado Numeric, creado por [Jim Hugunin](https://en.wikipedia.org/wiki/Jim_Hugunin) y en 2005, con la incorporación de Numarray y varias modificaciones, [Travis Oliphant](https://en.wikipedia.org/wiki/Travis_Oliphant) lo transforma en Numpy.

# In[1]:


5**(1/2)


# In[2]:


import math 


# In[3]:


math.pi


# In[4]:


import math as loquequiera


# In[5]:


loquequiera.pi


# In[6]:


get_ipython().run_line_magic('pinfo', 'math.pi')


# In[7]:


dir(math)


# In[8]:


import numpy as np


# In[9]:


get_ipython().run_line_magic('pinfo', 'np')


# In[10]:


dir(np)


# ## Conceptos básicos
# 
# El objeto más importante de numpy es el arreglo multidimensional homogéneo, es decir, una tabla de elementos del mismo tipo, indexados por una tupla de enteros no negativos. En numpy las dimensiones del arreglo las llamaremos ejes (axes).
# 
# **Ejemplo**
# 
# Un elemento en $\mathbb{R}^n$ es un arreglo $n$-dimensional con un solo eje:
# 
# 

# In[11]:


V=np.array([2,1,4])
print(V)


# In[12]:


V=np.array([2,1,4])
W=np.array([3,1,2])


# In[13]:


print(V+W)


# In[14]:


BV=np.array([True,False,True])
print(BV)


# Una matriz de tamaño $n\times m$ es un arreglo de dos ejes:

# In[15]:


M=np.array([[1,0,1],[0,1,0],[2,1,3]])
print(M)


# In[16]:


M.dtype


# In[17]:


M.shape


# In[18]:


CS=M.cumsum()


# En casos más generales podriamos definir un tensor:

# In[19]:


T=np.array([[[[1,2,1,4],[3,2,4,1],[4,2,3,1]],[[1,2,3,1],[0,1,2,3],[1,4,5,6]]],[[[2,3,4,1],[1,1,2,1],[0,1,1,2]],[[1,2,3,1],[0,1,1,1],[2,1,3,1]]]])
print(T)


# In[20]:


T.shape


# In[21]:


T.dtype


# In[22]:


T.ndim


# La exploración de elementos que conforman al arreglo es similar a la de las listas de Python, con la salvedad de que en la matriz, o el tensor no tengo una lista de listas:

# In[23]:


V


# In[24]:


V[1]


# In[25]:


print(M)


# In[26]:


M[1,1]


# In[27]:


M[1][1]


# In[28]:


print(T)


# In[29]:


T[1]


# In[30]:


T[1,0]


# In[31]:


T[1,0,2]


# In[32]:


TT=np.array([[[1,0,1],[0,1,0]],[[1,"0",3],[1,2,5]]])


# In[33]:


TT


# In[34]:


TT.shape


# In[35]:


TT[1][1][1]


# Podemos usar también índices de sublistas

# In[36]:


M2 = np.array([[1,2,3,4], [5,6,7,8], [9,10,11,12]])
print(M2)


# In[37]:


M2[:2,1:3]


# In[38]:


T=np.array([[[1,2,3,4],[5,6,7,8],[9,10,11,12]],[[13,14,15,16],[17,18,19,20],[21,22,23,24]],[[25,26,27,28],[29,30,31,32],[33,34,35,36]]])
print(T)


# In[39]:


T[:2,1:,1:3]


# También podemos extraer elementos utilizando listas

# In[40]:


print(M2)


# In[41]:


M2[[0,2],[1,3]]


# In[42]:


M2


# In[43]:


M2[[0,1,2,1],[0,1,2,3]]


# In[44]:


print(M2)


# In[45]:


M2[:,[0,1,2,2,1,1,2,2]]


# Extraer filas

# In[46]:


M2[np.array([0,2])]


# Extraer columnas

# In[47]:


M2[:,np.array([2,0])]


# Algunos comandos elementales son:
# 
# * `.ndim` (número de ejes del arreglo)

# In[48]:


V.ndim


# In[49]:


M.ndim


# In[50]:


T.ndim


# * `.shape` (La dimensión del arreglo. Obtenemos una tupla de enteros)

# In[51]:


V.shape


# In[52]:


M.shape


# In[53]:


T.shape


# * `.size` (El número total de elementos que conforman al arreglo)

# In[54]:


V.size


# In[55]:


T.size


# In[56]:


M.size


# In[57]:


print(M)


# In[58]:


np.concatenate((M,M),axis=1)


# In[59]:


np.array([[0],[0],[0]])


# In[60]:


np.array([    0,0,0])


# In[61]:


N=np.concatenate((M,np.array([[0],[0],[0]])),axis=1)
N


# In[62]:


N[:,[0,1,3,2]]


# * `.dtype` (el tipo de lementos en el arreglo)

# In[63]:


M.dtype


# In[64]:


A=np.array([3<2,2<3,4<5])
print(A)


# In[65]:


A.dtype


# In[66]:


TT2=np.array([A,V])
print(TT2)


# In[67]:


TT2.dtype


# ## Creación de algunos arreglos clásicos
# 
# Tenemos la oportunidad de utilizar algunas funciones de Numpy para generar arreglos y matrices conocidas:
# 

# In[68]:


ceros=np.zeros((2,3))
print(ceros)


# In[69]:


unos=np.ones((2,2,3))
print(unos)


# In[70]:


constante=np.full((4,3),5)
print(constante)


# In[71]:


constante2=np.full((4,3),5<2)
constante2[1,1]=True
print(constante2)


# In[72]:


constante3=np.full((4,3),"Hola")
print(constante3)


# In[73]:


identidad=np.eye(6,5)
print(identidad)


# In[74]:


aleatoria = np.random.random((2,2))  
print(aleatoria) 


# In[75]:


get_ipython().run_line_magic('pinfo', 'np.random')


# ## Operaciones elementales
# 
# Podemos hacer operaciones matriciales elementales:

# In[76]:


import numpy as np
x = np.array([[1,2,3],[4,5,6]], dtype=np.float64)
y = np.array([[7,8,9],[9,8,7]])
z=np.array([[1,1],[2,1]])


# In[77]:


print(x)
print(y)
print(z)


# In[78]:


print(x + y)


# In[79]:


print(x - y)


# In[80]:


print(x*y) #multiplicación elemento a elemento


# In[81]:


print(x / y) #división elemento a elemento


# In[82]:


print(y)
print(np.sqrt(y))  #raíz cuadrada elemento a elemento


# In[83]:


print(np.transpose(y)) #transpuesta


# In[84]:


print(y.T) #transpuesta


# (m,k) @ (k,n)=(m,n)

# In[85]:


print(x@np.transpose(y)) #multiplicación de matrices


# In[86]:


print(np.transpose(y)@x)


# In[87]:


print(x.dot(y.T)) #multiplicación de matrices


# In[88]:


print(x)


# In[89]:


print(np.sum(x))   #suma de todos los elementos
print(np.sum(x, axis=0))  #suma de elementos por columnas
print(np.sum(x, axis=1))   #suma de elementos por filas


# Mas funciones [aquí](https://numpy.org/doc/stable/reference/routines.array-manipulation.html)

# ## Operaciones especiales
# 
# En ocasiones tenemos que hacer algunas operaciones que no tienen en cuenta la forma de las matrices o que involucran matrices de diferentes tamaños. Aquí algunos ejemplos:

# In[90]:


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(x)


# In[91]:


print(x+10)


# In[92]:


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(x)
v = np.array(np.transpose([[1, 0, 1,1]]))
print(v)


# In[93]:


x+v


# In[94]:


x+1


# * Suma de un vector a una fila

# In[95]:


x = np.array([[1,2,3], [4,5,6], [7,8,9], [10, 11, 12]])
print(x)
v = np.array([1, 0, 1])
print(v)


# In[96]:


x[0]=x[0]+v
print(x)


# * Multiplicar una fila por escalar

# In[97]:


x[0]=x[0]*2
print(x)


# * Intercambiar filas

# In[98]:


fc=x.copy()
x[1]=x[0]
x[0]=fc[1]
print(x)


# ### Operaciones entre matrices de diferente tamaño (Broadcasting)

# NumPy transforma los arreglos involucrados para que tengan el mismo tamaño y, por tanto, puedan someterse a las operaciones por elementos sin generar excepciones.

# In[99]:


a = np.arange(0.2, 40.2, 10.5)
a.shape


# In[100]:


print(a)


# In[101]:


a = a[:, np.newaxis]  #Adicionamos un eje
print(a.shape)
a


# In[102]:


b = np.array([0, 1, 2])
print(b)


# In[103]:


a+b


# In[104]:


A=np.array([[0,1],[1,2]])
B=np.array([[2,1],[1,2]])


# In[105]:


A= A[:,:, np.newaxis] 


# In[106]:


A


# In[107]:


A+B


# ## Módulo de álgebra lineal
# 
# 

# ### Más matrices especiales
# 
# Tenemos la posibilidad de buscar más matrices interesantes en Numpy.
# 
# * Matriz triangular

# In[108]:


A=np.random.random((5,5))
print(A)


# In[109]:


np.triu(A)


# In[110]:


np.triu(A,1)


# In[111]:


np.triu(A,-1)


# In[112]:


np.triu(np.ones((3,3)),2)


# In[113]:


M3=(a+b).T
print(M3)


# In[114]:


np.triu(M3)


# In[115]:


np.tril(M3)


# In[116]:


np.tril(M3,-1)


# * Matriz diagonal

# In[117]:


np.diag([1,2,3,4])


# In[118]:


print(A)


# In[119]:


A.diagonal()


# ## Módulo `linalg` 
# 
# Numpy tiene un módulo especializado en funciones de [álgebra lineal](https://numpy.org/doc/stable/reference/routines.linalg.html)

# * Potencias de matrices

# In[120]:


N = np.array([[1, 0, 1], [2, -1, 3], [4, 3, 2]])
print(N)
np.linalg.matrix_power(N,2)


# * Determinantes
# 
# 

# In[121]:


np.linalg.det(N)


# * Valores y vectores propios

# In[122]:


np.linalg.eig(N)


# * Rango

# In[123]:


np.linalg.matrix_rank(N)


# * Solución de sistemas de ecuaciones lineales

# In[124]:


np.linalg.solve(N, [1,2,3])


# In[125]:


print(N)


# * Matrices Inversas
# 
# 

# In[126]:


Ninv=np.linalg.inv(N)
Ninv


# Comprobamos este resultado:

# In[127]:


Ninv @ N


# Observe que la anterior es la matriz idéntica.

# In[128]:


dir(np.linalg)


# In[129]:


get_ipython().run_line_magic('pinfo', 'np.trace')


# # Herramientas interactivas `ipywidgets`
# 
# Otro paquete que será transversal en este curso y nos permitira crear interfaces interesantes para nuestros estudiantes es [ipywidgets`](https://ipywidgets.readthedocs.io/en/stable/). Para instalar desde el cuaderno escriba:

# In[130]:


get_ipython().system('pip install ipywidgets')


# In[131]:


pip install seaborn


# In[132]:


get_ipython().system('jupyter nbextension enable --py widgetsnbextension')


# Importemos el paquete

# In[133]:


from ipywidgets import interact
import ipywidgets as widgets


# La herramienta más básica de este paquete es la función `interact`. En el siguiente ejemplo veamos su utilidad:

# In[134]:


def f(x):
    print("El valor que escogió es", x)
    return x


# In[135]:


f(4)


# In[136]:


def f(x):
    y=x+5
    print(x,"+",5,"=",y)
    return y


# In[137]:


f(8)


# In[138]:


def nombrelargoocorto(t):
    if len(t)>=7:
        print(t+" es un nombre muy largo")
        z="largo"
    else:
        print(t+" es un nombre corto")
        z="corto"
    return z


# In[139]:


nombrelargoocorto("Benjamin")


# In[140]:


def f(x):
    y=x+5
    print(x,"+",5,"=",y)
    return y


# In[141]:


interact(f, x=1.2)


# In[142]:


interact(nombrelargoocorto, t="Isaac")


# In[143]:


def f(x):
    print("El valor que escogió es", x)
    return x


# In[144]:


interact(f, x=True)


# In[145]:


interact(f, x={0:'Elemento 1',1:'Elemento 2'})


# In[146]:


interact(f, x='Soy interactivo')


# Los elementos que permiten la interacción con el usuario son los widgets, una lista completa de ellos se encuentra [aquí.](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html)

# A continuación hacemos un cambio sobre el widget:

# In[147]:


interact(f, x=widgets.IntText(
    value=7,
    description='Escriba un número: ',
    disabled=False
));


# ## Una primera aplicación
# 
# Ya que conocemos algo de Numpy y ipywidgets vamos a crear un ejemplo muy sencillo para calcular algunos estadísticos elementales de una lista de valores:

# In[148]:


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


# In[149]:


estadisticos("1 2 3")


# Evalue los estadísticos del conjunto de datos [1,1,2,3] y compruebelo con la herramienta:

# In[150]:


estadisticos("1 2 3 4 5 7 8 3 1 3 4 1 3 4 8 0 9")


# In[151]:


interact(estadisticos,x="1 2 3")


# In[152]:


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


# In[153]:


interact(estadisticos,x="1 2 3")


# In[154]:


def txttomtx(x):
    L=x.split()
    L=[float(i) for i in L]
    e=np.sqrt(len(L))
    d=int(e)
    k=0
    M=np.zeros((d,d))
    for i in range(d):
        for j in range(d):
            M[i,j]=L[k]
            k=k+1
    return M


# In[155]:


txttomtx("1 2 3 4")


# In[156]:


M=txttomtx("1 2 3 4")


# In[157]:


M


# In[158]:


np.linalg.det(M)


# In[159]:


def matrizopun(x,y):
    try:
        M=txttomtx(x)
        M2=txttomtx(y)
        SM=M+M2
        print("La suma es:",SM)
    except:
        print("Cuidado con lo que escribe, solo se admiten valores numéricos")
    return


# In[160]:


interact(matrizopun,x="1 2 3 4",y="1 2 3 4")

