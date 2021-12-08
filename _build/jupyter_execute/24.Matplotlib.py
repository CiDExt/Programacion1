#!/usr/bin/env python
# coding: utf-8

# # Matplotlib - Gráficos en Python

# :::::{important} Para tener presente
# 
# 
# El paquete para construir gráficos por excelencia en Python es [Matplotlib](https://matplotlib.org/3.2.2/index.html), una de las librerías más usadas para crear todo tipo de visualizaciones.
# 
# ````{tabbed} ¿Para qué?
# 
# :::{admonition} Importante
# :class: tip
# Para nosotros es muy importante manejar esta herramienta ya que en múltiples ocasiones la dificultad de muchas explicaciones se resuelven fácilmente con un buen gráfico.
# :::
# ````
# 
# ````{tabbed} ¿Qué haremos?
# 
# :::{admonition} Lo que vamos a aprender:
# :class: tip 
# En este cuaderno veremos algunos componentes básicos de la graficación con Matplotlib, las partes del gráfico, la definición de `figure()`, unas configuraciones simples y algunas personalizaciones elementales.
# :::
# ````
# :::::

# ## ¿Cómo funciona?
# 
# Matplotlib grafica sus datos sobre una instancia llamada `Figure`, cada una de estas contendrá uno o más `Axes` (un área en la que los puntos tienen coordenadas). Usualmente se utiliza la interfaz [pyplot](https://matplotlib.org/3.2.2/api/pyplot_summary.html) basada en algunos estilos y comandos de MATLAB. 
# 
# Veamos un sencillo ejemplo:

# In[1]:


import matplotlib.pyplot as plt
import numpy as np
get_ipython().run_line_magic('matplotlib', 'inline')
fig, ax = plt.subplots()  # Creamos una figura con un sistema de ejes.
ax.plot([1, 2, 3, 4], [1, 4, 2, 3])  # Pintamos algunos datos.


# :::::{important} Para tener presente
# 
# IPython tiene un conjunto de "funciones mágicas" predefinidas a las que puede llamar con una sintaxis de estilo de línea de comandos. Hay dos tipos de magia, orientada a líneas y orientada a celdas.
# 
# ````{tabbed} Orientada a líneas
# 
# :::{admonition} Para no olvidar...
# :class: tip
# Tienen el prefijo `%` y funcionan de manera muy similar a las llamadas de línea de comandos del sistema operativo: obtienen como argumento el resto de la línea, donde los argumentos se pasan sin paréntesis ni comillas. La magia de líneas puede devolver resultados y se puede utilizar en el lado derecho de una asignmación.
# :::
# ````
# 
# ````{tabbed} Orientado a celdas
# 
# :::{admonition} Para no olvidar...
# :class: tip 
# La magia en las celdas tiene el prefijo `%%`, son funciones que obtienen como argumento no solo el resto de la línea, sino también las líneas debajo de ella en un argumento separado.
# :::
# ````
# :::::

# Sin necesidad de fijar los ejes de una figura podemos hacer el mismo gráfico:

# In[2]:


plt.plot([1, 2, 3, 4], [1, 4, 2, 3]) 


# ## Partes de una figura
# 
# Veamos los componentes de una figura de Matplotlib:
# 
# ![figure](https://matplotlib.org/3.2.2/_images/anatomy.png)
# 
# *Tomado de [https://matplotlib.org/3.2.2/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py](https://matplotlib.org/3.2.2/tutorials/introductory/usage.html#sphx-glr-tutorials-introductory-usage-py)*

# Sin necesidad de definir nuevas figuras veremos un ejemplo con algunos elementos descritos en la figura:

# In[3]:


x=np.linspace(0, 10, 101)


# In[4]:


np.sin(x)


# In[5]:


x = np.linspace(0, 10, 101)

plt.plot(x, np.sin(x),'r-', label='sin(x)')#1
plt.plot(x, np.cos(x), 'y-',label='cos(x)')#1
plt.legend()#2
plt.grid()#3
plt.title("Una figura simple")#4
plt.xlabel('Eje x')#5
plt.ylabel('Eje y')#6
plt.show()#7


# En el bloque de código anterior hemos agregado unos comentarios en forma de número para aclararlos en seguida:
# 1. 
# ```python
# plt.plot(x, np.sin(x),'r-', label='sin(x)')
# ```
# `x` los valores de éste argumento serán tenidos en cuenta para el eje horizontal.
# `np.sin(x)` son los valores resultantes de aplicar la función seno a cada elemento del arreglo x.
# `'r-'` este argumento hace que la gráfica sea de color rojo y su trazo sea continuo.
# `label='sin(x)'` agrega a la leyenda 'sin(x)'.
# 2. Hace que se "pinte" la leyenda sobre la gráfica.
# 3. Agrega la grilla a la gráfica.
# 4. Agrega el título a la gráfica.
# 5. Agrega el nombre del eje x.
# 6. Agrega el nombre del eje y.
# 7. Muestra la gráfica elaborada.
# 
# Podemos hacer un elemento interactivo con algunas de las funciones trigonométricas:

# In[6]:


from ipywidgets import interact
from numpy import *


# In[7]:


def graficadoradefuncionestrigonometricas(t):
    x=np.linspace(-10,10,500)
    y=eval(t)
    plt.plot(x,y,label=t)
    plt.legend()
    return


# In[8]:


graficadoradefuncionestrigonometricas('sin(x)')


# In[9]:


lista=["sin(x)","cos(x)","tan(x)"]

interact(graficadoradefuncionestrigonometricas,t=lista)


# ### Ejercicio
# 1. Modifica el código anterior para que se grafiquen los monomios x, x^2, ..., x^10.

# ## Figura y ejes como variables
# Podemos usar instancias para expresar tanto a la figura como los ejes sobre la figura:

# In[10]:


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen')
ax.set_xlim(-1, 6)
ax.set_ylim(6, 31)
plt.show()


# En este ejemplo utilizamos `plt.figure()` para definir la figura y `fig.add_subplot(111)` para crear la *'zona de dibujo'*. 
# 
# En Matplotlib se puiede definir sobre una misma figura varias zonas de dibujo:

# In[11]:


x=np.linspace(0,10,100)
fig = plt.figure(figsize=(20,20))

ax = fig.add_subplot(221)

ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3,label="línea")
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^',label="marker")
ax.legend()
plt.title("Primera 'zona de dibujo'")

ax2 = fig.add_subplot(222)

ax2.plot(x, x, label='línea')
ax2.legend()
plt.title("Segunda 'zona de dibujo'")

ax3 = fig.add_subplot(223)
ax3.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3,label="línea")
ax3.legend()
plt.title("Tercera 'zona de dibujo'")

ax4 = fig.add_subplot(224)
ax4.plot(x, x, label='línea')
ax4.legend()
plt.title("Cuarta 'zona de dibujo'")
plt.show()


# Las líneas que contienen `fig.add_subplot(221)` nos indican que las gráficas estarán distribuidas en una parrilla 2x2 y estamos modificando la primera de ellas.
# 
# Las zonas de dibujo (`Axes`) siempre deben vincularse a una Figura. Podemos fijar un título para cada zona usando `set_title()`. Por cada `Axes` tenemos 2 o tres ejes (`Axis`), entre sus funcioes útiles tenemos:
# 
# **Para controlar el límite de los ejes:**
# * `axes.Axes.set_xlim()`
# * `axes.Axes.set_ylim()`
# 
# **Para fijar una etiqueta en el eje**
# 
# * `set_xlabel()`
# * `set_ylabel()`
# 
# 
# Veamos un ejemplo:

# In[12]:


fig = plt.figure(figsize=(10,5))
ax = fig.add_subplot(121)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3,label="línea")
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen', marker='^',label="marker")
ax.set_xlim(0, 4.5)
ax.set_ylim(0, 31)
ax.set_ylabel("Eje y")
ax.set_xlabel("Eje x")
ax.legend()
ax.set_title("Primera 'zona de dibujo'")
ax2 = fig.add_subplot(122)
ax2.plot(x, x, label='línea')
ax2.legend()
ax2.set_title("Segunda 'zona de dibujo'")
plt.show()


# ## Diferentes tipos de gráficos
# 
# Veamos ahora una galería de gráficos utilizados en diferentes contextos. Según los ejemplos anteriores tenemos la posibilidad de graficar puntos sobre el plano utilizando `plt.plot()`

# ### El commando `plt.plot()`

# In[13]:


plt.plot([1,2,4,3,1,2,8,7])
plt.ylabel('Una lista de valores')
plt.show()


# Notemos que el índice del valor aparece en el eje horizontal y el valor en el eje vertical.

# In[14]:


plt.plot([1,2,4,3,1,2,8,7])
plt.xticks(ticks=range(0,8),labels=['L','M','Mc','J','V','S','D','L'])
plt.show()


# In[15]:


plt.plot([1,2,3],[[1,2,3,4], [1,4,9,16],[3,4,2,16]]) 
plt.ylabel('Un arreglo en x, un arreglo en y')
plt.grid()
plt.show()
#El 1 esta asociado con el 1,2,3 y 4
#El 2 con 1,4,9  y 16
#El 3 con 3,4,2 y 16


# In[16]:


x=np.arange(-10,10,0.1)
y=np.sin(x)
plt.plot(x,y) 
plt.ylabel('Un gráfico de sen(x)')
plt.show()


# No obstante podemos graficar sin unir los puntos:

# In[17]:


#Gráfica de una lista de puntos:
plt.plot([1, 2, 3, 4], [1, 4, 9, 16], '^y')
plt.axis([0, 6, 0, 20])#ajuste de valores de los ejes
plt.show()


# In[18]:


#Gráfico de una función aplicada a una lista
x=np.arange(-10,10,0.1)
y=np.sin(x)
plt.plot(x,y,'g*') 
plt.ylabel('Un gráfico de sen(x)')
plt.show()


# **Varias funciones en un mismo gráfico:**

# In[19]:


plt.plot(x,np.sin(x)+np.cos(x) , 'r--', x, np.sin(x), 'bs', x, np.cos(x), 'g^')
plt.show()


# In[20]:


x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()  # Creamos una instancia de figura y una zona de dibujo.
ax.plot(x, x, label='Función lineal')  #Agregamos función por función
ax.plot(x, x**2, label='Función cuadrática')  
ax.plot(x, x**3, label='Función cúbica') 
ax.set_xlabel('eje x') #Ajustamos títulos de ejes
ax.set_ylabel('eje y')  
ax.set_title("Tres funciones") #Ponemos título a la gráfica
ax.legend()  


# ## ¿Qué estilos podemos agregar a las líneas?
# Las líneas, como hemos visto, tienen muchas propiedades que podemos modificar, entre ellas están: el color, el tipo de trazado, el grosor, etc. Con las siguientes líneas de comando veremos otras propiedades y las posibles modificaciones a realizar:

# In[21]:


line,=plt.plot([1,2,3])
plt.setp(line)


# ## Gráficos de dispersión 
# Son gráficos en los que se grafican con coordenadas cartesianas los valores de dos variables en un conjunto de datos.
# 
# Para dar un buen ejemplo, iniciemos definiendo una base de datos aleatoria:

# In[22]:


data={}
data = {'Eje x': np.arange(50),
        'Tamaño': np.random.randn(50),
        'Color': np.random.randint(0, 50, 50)}
data['Eje y'] = data['Eje x'] + 10 * np.random.randn(50)
data['Tamaño'] = np.abs(data['Tamaño']) * 100


# In[23]:


import pandas as pd
data=pd.DataFrame(data)
data


# In[24]:


data['Eje x']


# In[25]:


data['Eje y']


# In[26]:


plt.scatter('Eje x', 'Eje y',data=data)
plt.xlabel('Valores guardados en "Eje x"')
plt.ylabel('Valores guardados en "Eje y"')
plt.grid()
plt.show()


# En los gráficos de dispersión, podemos agregar más variables al gráfico sin aumentar su dimensión. Introduzcamos una variable, el tamaño:

# In[27]:


plt.scatter('Eje x', 'Eje y',s='Tamaño',data=data)#1
plt.xlabel('Valores guardados en a')
plt.ylabel('Valores guardados en b')
plt.show()


# 1. El argumento `s`, permite modificar el tamaño del punto según el valor dado en la variable (`s`=`size`).

# Además podemos agregar una cuarta variable, por ejemplo, usemos colores:

# In[28]:


plt.scatter('Eje x', 'Eje y',s='Tamaño',c='Color',cmap='inferno',data=data)#1
plt.xlabel('Valores guardados en a')
plt.ylabel('Valores guardados en b')
plt.show()


# 1. El argumento `c` (`c` de `color`) permite asignar un color por cada valor en la variable. El argumento `cmap` (*colormap*) es para seleccionar la paleta de colores a utilizar (para ver la gama completa de colores visite [Colores](https://matplotlib.org/stable/tutorials/colors/colormaps.html)).
# 
# En resumen, hemos graficado en un plano cartesiano cuatro variables, una representada por el eje horizontal, otra por el eje vertical, una más representada por el tamaño y la última representada por el color.

# ## Gráficos para variables categóricas
# 
# Con `Matplotlib` también podemos hacer gráficos de variables categóricas. Un ejemplo simple:

# In[29]:


x=["María", "Pedro", "Juan"]
y=[10,12,8]
plt.bar(x,y)


# Si deseamos las barras horizontales y cambiar el color:

# In[30]:


x=["María", "Pedro", "Juan"]
y=[10,12,8]
plt.barh(x,y,color='y')


# También podemos unir los puntos con líneas como hicimos al principio:

# In[31]:


x=["María", "Pedro", "Juan"]
y=[10,12,8]
plt.plot(x,y)


# O también podríamos realizar el gráfico de dispersión para las categorías, aunque no es muy utilizado:

# In[32]:


x=["María", "Pedro", "Juan"]
y=[10,12,8]
plt.scatter(y,x)


# En algunas oportunidades, las variables que tratemos se prestan para realizar un gráfico de barras apilado, es decir, una barra sobre la otra separando los colores por categoría:

# In[33]:


#Definamos los elementos con los que trabajaremos:
labels = ['G1', 'G2', 'G3', 'G4', 'G5']#Nombres de los grupos
hombres = [24, 26, 30, 35, 17]#Puntajes de los hombres
mujeres = np.array([22, 31, 44, 18, 30])#Puntajes de las mujeres
width = 0.9#Ancho de la barra

fig, ax = plt.subplots()
ax.barh(labels, mujeres, width, left=hombres,label='Mujeres')
ax.barh(labels, hombres, width, label='Hombres')
ax.set_ylabel('Puntuaciones')
ax.set_title('Puntuaciones por grupo y género')
ax.legend()


# Ahora, vamos a realizar la gráfica con los datos agrupados:

# In[34]:


x = np.arange(len(labels)) 
x


# In[35]:


width=0.35
x = np.arange(len(labels)) 
fig, ax = plt.subplots()
rects1 = ax.barh(x - width/2, hombres, width, label='Hombres')
rects2 = ax.barh(x+width/2, mujeres, width, label='Mujeres')
ax.set_yticks(x)
ax.set_yticklabels(labels)

ax.set_xlabel('Puntuaciones')
ax.set_title('Puntuaciones por grupo y género')
ax.legend()


# ## Histogramas
# Son gráficos empleados para dar un primer vistazo del comportamiento de la variable. Se hace mediante barras, y la altura de cada barra depende de la frecuencia de los valores representados:

# In[36]:


#Generamos valores aleatorios:
mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 10, density=True, facecolor='y', alpha=0.5)

plt.xlabel('Puntaje')
plt.ylabel('Probabilidad')
plt.title('Histograma')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


# In[37]:


#Valor de la probabilidad
n


# In[38]:


#Valores de los extremos de las barras
bins


# In[39]:


#Son los contenedores que se utilizan para crear el histograma
patches


# Vamos a definir una función en la que podamos controlar dos aspectos: el primero será la cantidad de barras que se graficarán y el segundo la intensidad del color:

# In[40]:


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)
def histograma(n,a):
    plt.hist(x, n, density=True, facecolor='y', alpha=a)
    plt.xlabel('Puntaje')
    plt.ylabel('Probabilidad')
    plt.title('Histograma')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()
    return


# In[41]:


histograma(5,0.5)


# Ahora agregaremos los componentes de interactividad vistos en el cuaderno anterior:

# In[42]:


import ipywidgets as widgets
from ipywidgets import interact
interact(histograma,n=widgets.IntSlider(value=30,min=1,max=50,description="Intervalos"),
         a=widgets.FloatSlider(value=0.5,min=0,max=1,description="Transparencia"))


# Importaremos el paquete `math` para hacer un ejercicio muy interesante:

# In[43]:


from math import sqrt
x=25
eval("sqrt(x)")


# ## Graficador de funciones
# Haremos un graficador de funciones, cuyas variables serán: el nombre de la función (`nf`), los valores mínimo y máximo en el eje x (`xmin`, `xmax`) y también los valores mínimo y máximo en el eje y (`ymin`, `ymax`):

# In[44]:


def graffun(nf,xmin,xmax,ymin,ymax):
    try:
        x = np.linspace(xmin, xmax, 100)
        y=eval(nf)
        plt.plot(x,y)
        plt.axis([xmin,xmax,ymin,ymax])
        plt.grid(True)
    except:
        print('Error!!')


interact(graffun,nf='(x-3)**2',xmin=-10,xmax=2*np.pi,ymin=-1,ymax=1)  


# ## Texto en las gráficas
# 
# Si necesitamos introducir elementos aclaratorios en nuestras gráficas, podemos usar el comando `plt.text()` o el comando `plt.annotate()`:

# In[45]:


ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.text(0.7,1.12,'Un máximo\nlocal ')#1
plt.ylim(-2, 2)
plt.show()


# 1. Las primeras entradas son las coordenadas del texto y la tercera es el texto que se desea agregar.
# 

# In[46]:


ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
#Se pueden agregar códigos Latex
plt.text(0.7,1.12,r'$\left(2\cdot\pi\cdot\frac{\pi}{2},1\right)$')
plt.title(r"Función $\cos(2\pi x)$ y un máximo local")
plt.ylim(-2, 2)
plt.show()


# Ahora con una anotación:

# In[47]:


ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('Máximo local', xy=(1, 1), xytext=(3, 1.5),
             arrowprops=dict(edgecolor='green',facecolor='blue'),
             )#1

plt.ylim(-2, 2)
plt.show()


# In[48]:


get_ipython().run_line_magic('pinfo', 'plt.annotate')


# In[49]:


ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('Máximo local', xy=(1, 1), xytext=(3, 1.5),
             arrowprops=dict(edgecolor='green',facecolor='red', shrink=0.05),)

plt.ylim(-2, 2)
plt.show()


# Veámos los diferentes tipos de flecha que podemos emplear en nuestras anotaciones:

# In[50]:


def estiloflecha(l):
    ax = plt.subplot(111)

    t = np.arange(0.0, 5.0, 0.01)
    s = np.cos(2*np.pi*t)
    line, = plt.plot(t, s, lw=2)

    plt.annotate('Máximo local', xy=(1, 1), xytext=(3, 1.5),
                 arrowprops=dict(edgecolor='green',facecolor='red', arrowstyle=l),)

    plt.ylim(-2, 2)
    plt.show()
    return


# In[51]:


interact(estiloflecha,l=['-','->','-[','|-|','-|>','fancy','simple','wedge'])


# ## Backends
# 
# Al usar Jupyter nosotros estamos pidiendo que el gráfico se pueda visualizar en el entorno web en el cual se está mostrando las salidas de Python. Sin embargo, es posible visualizar estos mismos gráficos en otras interfaces gráficas más potentes y con más herramientas. 
# 
# Matplotlib permite utilizar las diferentes interfáces haciendo modificación en su backend, entendiendo al backend como el motor gráfico que genera las diferentes imagenes que imaginamos.
# 
# Para modificar el backend usado en Jupyter usamos un comándo mágico `%matplotlib`. Veamos algunos ejemplos:

# In[52]:


import matplotlib


# In[53]:


import matplotlib
import matplotlib.pyplot as plt
import numpy as np


# In[54]:


get_ipython().run_line_magic('matplotlib', 'notebook')
ax = plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
plt.text(0.7,1.12,'Un máximo\nlocal ')
plt.ylim(-2, 2)
#plt.show()
line


# In[55]:


#!pip install mpld3


# In[56]:


#Reiniciar el Kernel
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import mpld3
mpld3.enable_notebook()
ax = plt.subplot(111)
t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)
plt.text(0.7,1.12,'Un máximo\nlocal ')
plt.ylim(-2, 2)
plt.show()
#mpld3.show()


# In[ ]:




