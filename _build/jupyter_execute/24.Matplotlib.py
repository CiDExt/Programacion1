#!/usr/bin/env python
# coding: utf-8

# <h1>Matplotlib - Gráficos en Python<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Introducción-Matplotlib" data-toc-modified-id="Introducción-Matplotlib-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Introducción Matplotlib</a></span><ul class="toc-item"><li><span><a href="#¿Cómo-funciona?" data-toc-modified-id="¿Cómo-funciona?-1.1"><span class="toc-item-num">1.1&nbsp;&nbsp;</span>¿Cómo funciona?</a></span></li><li><span><a href="#Partes-de-una-figura" data-toc-modified-id="Partes-de-una-figura-1.2"><span class="toc-item-num">1.2&nbsp;&nbsp;</span>Partes de una figura</a></span></li><li><span><a href="#Diferentes-tipos-de-gráficos" data-toc-modified-id="Diferentes-tipos-de-gráficos-1.3"><span class="toc-item-num">1.3&nbsp;&nbsp;</span>Diferentes tipos de gráficos</a></span><ul class="toc-item"><li><span><a href="#El-commando-plt.plot()" data-toc-modified-id="El-commando-plt.plot()-1.3.1"><span class="toc-item-num">1.3.1&nbsp;&nbsp;</span>El commando <code>plt.plot()</code></a></span></li><li><span><a href="#Gráficos-de-dispersión" data-toc-modified-id="Gráficos-de-dispersión-1.3.2"><span class="toc-item-num">1.3.2&nbsp;&nbsp;</span>Gráficos de dispersión</a></span></li><li><span><a href="#Gráficos-para-variables-categóricas" data-toc-modified-id="Gráficos-para-variables-categóricas-1.3.3"><span class="toc-item-num">1.3.3&nbsp;&nbsp;</span>Gráficos para variables categóricas</a></span></li><li><span><a href="#Graficador-de-funciones" data-toc-modified-id="Graficador-de-funciones-1.3.4"><span class="toc-item-num">1.3.4&nbsp;&nbsp;</span>Graficador de funciones</a></span></li><li><span><a href="#Texto-en-las-gráficas" data-toc-modified-id="Texto-en-las-gráficas-1.3.5"><span class="toc-item-num">1.3.5&nbsp;&nbsp;</span>Texto en las gráficas</a></span></li></ul></li><li><span><a href="#Backends" data-toc-modified-id="Backends-1.4"><span class="toc-item-num">1.4&nbsp;&nbsp;</span>Backends</a></span></li></ul></li><li><span><a href="#Herramientas-interactivas-ipywidgets" data-toc-modified-id="Herramientas-interactivas-ipywidgets-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Herramientas interactivas <code>ipywidgets</code></a></span><ul class="toc-item"><li><span><a href="#Una-primera-aplicación" data-toc-modified-id="Una-primera-aplicación-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Una primera aplicación</a></span></li></ul></li></ul></div>

# # Introducción Matplotlib
# 
# El paquete para construir gráficos por excelencia en Python es [Matplotlib](https://matplotlib.org/3.2.2/index.html), una de las librerías más usadas para crear todo tipo de visualizaciones  . Para nosotros es muy importante manejar esta herramienta ya que en múltiples ocasiones la dificultad de muchas explicaciones se resuelven fácilmente con un buen gráfico. En este cuaderno veremos algunos componentes básicos de la graficación con Matplotlib, las partes del gráfico, la definición de `figure()`, unas configuraciones simples y algunas personalizaciones elementales. 

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

# Sin necesidad de definir nuevas figuras veamos un ejemplo con algunos elementos descritos en la figura:

# In[3]:


x=np.linspace(0, 10, 101)


# In[4]:


np.sin(x)


# In[5]:


x = np.linspace(0, 10, 101)

plt.plot(x, np.sin(x),'r-', label='sin(x)')
plt.plot(x, np.cos(x), 'y-',label='cos(x)')
plt.legend()
plt.grid()
plt.title("Una figura simple")
plt.xlabel('Eje x')
plt.ylabel('Eje y')
plt.show()


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


# No obstante, recordemos que podemos usar instancias para expresar tanto a la figura como los ejes sobre la figura:

# In[10]:


fig = plt.figure()
ax = fig.add_subplot(111)
ax.plot([1, 2, 3, 4], [10, 20, 25, 30], color='lightblue', linewidth=3)
ax.scatter([0.3, 3.8, 1.2, 2.5], [11, 25, 9, 26], color='darkgreen')
ax.set_xlim(-1, 6)
ax.set_ylim(6, 31)
plt.show()


# En este ejemplo utilizamos `plt.figure()` para definir la figura y `fig.add_subplot(111)` para crear la *'zona de dibujo'*. Definamos sobre una misma figura varias zonas de dibujo:

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


# In[14]:


plt.plot([1,2,4,3,1,2,8,7])
plt.xticks(ticks=range(0,8),labels=['L','M','Mc','J','V','S','D','L'])
plt.show()


# In[15]:


np.array([[1, 2, 3,4], [1, 4, 9, 16],[3,4,2,16]])


# In[16]:


plt.plot([1,2,3],[[1, 2, 3,4], [1, 4, 9, 16],[3,4,2,16]]) 
plt.ylabel('Un arreglo en x, un arreglo en y')
plt.grid()
plt.show()


# In[17]:


import numpy as np

x=np.arange(-10,10,0.1)
y=np.sin(x)
plt.plot(x,y) 
plt.ylabel('Un gráfico de sen(x)')
plt.show()


# No obstante podemos graficar sin unir los puntos:

# In[18]:


plt.plot([1, 2, 3, 4], [1, 4, 9, 16], '^y')
plt.axis([0, 6, 0, 20])
plt.show()


# In[19]:


x=np.arange(-10,10,0.1)
y=np.sin(x)
plt.plot(x,y,'g*') 
plt.ylabel('Un gráfico de sen(x)')
plt.show()


# **Varias funciones en un mismo gráfico:**

# In[20]:


plt.plot(x,np.sin(x)+np.cos(x) , 'r--', x, np.sin(x), 'bs', x, np.cos(x), 'g^')
plt.show()


# In[21]:


x = np.linspace(0, 2, 100)
fig, ax = plt.subplots()  # Creamos una instancia de figura y una zona de dibujo.
ax.plot(x, x, label='Función lineal')  
ax.plot(x, x**2, label='Función cuadrática')  
ax.plot(x, x**3, label='Función cúbica') 
ax.set_xlabel('eje x')  
ax.set_ylabel('eje y')  
ax.set_title("Tres funciones")  
ax.legend()  


# Usamos estilos y colores para lineas, para mayor información usar: 

# In[22]:


line,=plt.plot([1,2,3])
plt.setp(line)


# ### Gráficos de dispersión 
# Iniciemos definiendo una base de datos aleatoria:

# In[23]:


data={}
data = {'Eje x': np.arange(50),
        'Tamaño': np.random.randn(50),
        'Color': np.random.randint(0, 50, 50)}
data['Eje y'] = data['Eje x'] + 10 * np.random.randn(50)
data['Tamaño'] = np.abs(data['Tamaño']) * 100


# In[24]:


import pandas as pd
data=pd.DataFrame(data)
data


# In[25]:


data['Eje x']


# In[26]:


data['Eje y']


# In[27]:


plt.scatter('Eje x', 'Eje y',data=data)
plt.xlabel('Valores guardados en a')
plt.ylabel('Valores guardados en b')
plt.grid()
plt.show()


# Introduzcamos variación de tamaños

# In[28]:


plt.scatter('Eje x', 'Eje y',s='Tamaño',data=data)
plt.xlabel('Valores guardados en a')
plt.ylabel('Valores guardados en b')
plt.show()


# Finalmente usemos colores:

# In[29]:


plt.scatter('Eje x', 'Eje y',s='Tamaño',c='Color',cmap='inferno',data=data)
plt.xlabel('Valores guardados en a')
plt.ylabel('Valores guardados en b')
plt.show()


# ### Gráficos para variables categóricas
# 
# Con Matplotlib también podemos hacer gráficos de variables categóricas. Un ejemplo simple:

# In[30]:


x=["María", "Pedro", "Juan"]
y=[10,12,8]
plt.bar(x,y)


# In[31]:


x=["María", "Pedro", "Juan"]
y=[10,12,8]
plt.barh(x,y,color='y')


# In[32]:


x=["María", "Pedro", "Juan"]
y=[10,12,8]
plt.plot(x,y)


# In[33]:


x=["María", "Pedro", "Juan"]
y=[10,12,8]
plt.scatter(y,x)


# Un gráfico de barras apilado

# In[34]:


labels = ['G1', 'G2', 'G3', 'G4', 'G5']
hombres = [24, 26, 30, 35, 17]
mujeres = np.array([22, 31, 44, 18, 30])
width = 0.9   

fig, ax = plt.subplots()
ax.barh(labels, mujeres, width, left=hombres,label='Mujeres')
ax.barh(labels, hombres, width, label='Hombres')
ax.set_ylabel('Puntuaciones')
ax.set_title('Puntuaciones por grupo y género')
ax.legend()


# Ahora agrupados:

# In[35]:


x = np.arange(len(labels)) 
x


# In[36]:


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


# **Histogramas**

# In[37]:


mu, sigma = 100, 15
x = mu + sigma * np.random.randn(10000)

n, bins, patches = plt.hist(x, 10, density=True, facecolor='y', alpha=0.5)

plt.xlabel('Puntaje')
plt.ylabel('Probabilidad')
plt.title('Histograma')
plt.axis([40, 160, 0, 0.03])
plt.grid(True)
plt.show()


# In[38]:


n


# In[39]:


bins


# In[40]:


patches


# In[41]:


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


# In[42]:


import ipywidgets as widgets
from ipywidgets import interact
interact(histograma,n=widgets.IntSlider(value=30,min=1,max=50,description="Intervalos"),
         a=widgets.FloatSlider(value=0.5,min=0,max=1,description="Transparencia"))


# In[43]:


from math import sqrt
x=25
eval("sqrt(x)")


# ### Graficador de funciones

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


# ### Texto en las gráficas
# 
# Ahora usaremos el comando `plt.text()` y `plt.annotate()` para adicionar texto en el gráfico:

# In[45]:


ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.text(0.7,1.12,'Un máximo\nlocal ')

plt.ylim(-2, 2)
plt.show()


# In[46]:


ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

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
             )

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
# Al usar Jupyter nosotros estamos pidiendo que el gráfico se pueda visualizar en el entorno web en el cual se está mostrando las salidas de Python. Sin embargo, es posible visalizar estos mismos gráficos en otras interfáces gráficas más potentes ycon más herramientas. 
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
plt.show()


# In[55]:


get_ipython().system('pip install mpld3')


# In[56]:


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


# # Herramientas interactivas `ipywidgets`
# 
# Otro paquete que será transversal en este curso y nos permitira crear interfaces interesantes para nuestros estudiantes es [ipywidgets`](https://ipywidgets.readthedocs.io/en/stable/). Para instalar desde el cuaderno escriba:

# In[57]:


get_ipython().system('pip install ipywidgets')


# In[58]:


get_ipython().system('pip install seaborn')


# In[59]:


get_ipython().system('jupyter nbextension enable --py widgetsnbextension')


# Importemos el paquete

# In[60]:


from ipywidgets import interact
import ipywidgets as widgets


# La herramienta más básica de este paquete es la función `interact`. En el siguiente ejemplo veamos su utilidad:

# In[61]:


def f(x):
    print("El valor que escogió es", x)
    return x


# In[62]:


f(7)


# In[63]:


def f(x):
    y=x+5
    print(x,"+",5,"=",y)
    return y


# In[64]:


f(8)


# In[65]:


def nombrelargoocorto(t):
    if len(t)>=7:
        print(t+" es un nombre muy largo")
        z="largo"
    else:
        print(t+" es un nombre corto")
        z="corto"
    return z


# In[66]:


nombrelargoocorto("Isaac")


# In[67]:


def f(x):
    y=x+5
    print(x,"+",5,"=",y)
    return y


# In[68]:


interact(f, x=1.2)


# In[69]:


interact(nombrelargoocorto, t="Isaac")


# In[70]:


def f(x,y):
    print(y," ganó", x)
    return x,y


# In[71]:


inttext=widgets.IntText(
    value=1000,
    description='Gana:'
)
interact(f, y=['Hugo','Paco','Luis'],x=inttext)


# In[72]:


from sklearn import datasets
import pandas as pd
iris=datasets.load_iris()
IrisDF=pd.DataFrame(iris.data)
IrisDF['Target']=iris.target
IrisDF


# In[73]:


def mostrarbase(t):
    DFres=IrisDF[IrisDF['Target']==t]
    plt.hist(DFres[0])
    plt.show()
    return 


# In[74]:


interact(mostrarbase,t=IrisDF['Target'].unique())


# Los elementos que permiten la interacción con el usuario son los widgets, una lista completa de ellos se encuentra [aquí.](https://ipywidgets.readthedocs.io/en/stable/examples/Widget%20List.html)

# A continuación hacemos un cambio sobre el widget:

# In[75]:


def f(x):
    return x
interact(f, x=widgets.IntText(
    value=7,
    description='Escriba un número: ',
    disabled=False
));


# ## Una primera aplicación
# 
# Ya que conocemos algo de Numpy y ipywidgets vamos a crear un ejemplo muy sencillo para calcular algunos estadísticos elementales de una lista de valores:

# In[76]:


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


# In[77]:


estadisticos("1 2 3")


# Evalue los estadísticos del conjunto de datos [1,1,2,3] y compruebelo con la herramienta:

# In[78]:


estadisticos("1 2 3 4 5 7 8 3 1 3 4 1 3 4 8 0 9")


# In[79]:


interact(estadisticos,x="1 2 3")


# In[80]:


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


# In[81]:


interact(estadisticos,x="1 2 3")


# In[82]:


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


# In[83]:


txttomtx("1 2 3 4")


# In[84]:


M=txttomtx("1 2 3 4")


# In[85]:


M


# In[86]:


np.linalg.det(M)


# In[87]:


def matrizopun(x,y):
    try:
        M=txttomtx(x)
        M2=txttomtx(y)
        SM=M+M2
        print("La suma es:",SM)
    except:
        print("Cuidado con lo que escribe, solo se admiten valores numéricos")
    return


# In[88]:


interact(matrizopun,x="1 2 3 4",y="1 2 3 4")


# In[89]:


import ipywidgets as widgets
from ipywidgets import interact, Layout


# In[90]:


widgets.Textarea(
    value='Hello World',
    placeholder='Type something',
    description='Una descripción muy laaaarga:')


# In[91]:


style = {'description_width': 'initial'}
l = Layout( height='80px', width='auto')
widgets.Textarea(
    value='Hello World',
    placeholder='Type something',
    description='Una descripción muy laaaarga:',
    style=style,
    layout=l)


# In[92]:


style = {'description_width': 'initial'}
l = Layout( height='80px', width='auto')
def convertidodematrices(A):
    B=A.split("\n")
    Matriz=[]
    for i in B:
        Matriz.append([int(j) for j in i.split()])
    print(Matriz)
    
    
A=widgets.Textarea(
    value='1 2 3',
    placeholder='Type something',
    description='Una descripción muy laaaarga:',
    style=style,
    layout=l)

interact(convertidodematrices,A=A)

