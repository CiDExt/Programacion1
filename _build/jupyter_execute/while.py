#!/usr/bin/env python
# coding: utf-8

# <div style="padding: -5px;
#   text-align: center;
#   color: white;
#   font-size: 20px;">
#    <img src="images/banner.jpg" alt="MINE-Seminario de programación" style="width:100%;">
#   <h1 style="
#   position: absolute;
#   top: 5%;
#   left: 50%;">While</h1>
# </div>

# En este cuaderno, estudiaremos una estructura de control diseñadas hacer tareas repetitivas y parar cuando una condición deje de cumplirse.
# 
# Mientras se cumpla la condición, se ejecuta un bloque de código.
# 
# ```
# while (condición):
#     instrucción 1
#     instrucción 2
#     
#     instrucción n
# ```
# 
# **Nota:**
# 
# Para esta estructura debemos tener especial cuidado, ya que existe la posibilidad de escribir la condición de tal manera que siempre se cumpla y tendríamos un ciclo infinito, como ocurrirá con el siguiente código.

# In[1]:


while 2!=1:
    print(1, end=' ')
#Reinicia el Kernel.


# Como queremos que el ciclo se detenga en algún momento, se recomienda que en las instrucciones incluyamos un paso en el cual se modifique el elemento que interviene en la condición, de tal modo que, luego de un número finito de iteraciones se detenga la tarea:

# In[3]:


i=0
while i<10:
    i=i+1
    print(i,end=' ')


# Otra forma de detener el ciclo, es incluir una condición con un `if`, así:

# In[5]:


i=0
while i<10:
    i=i+1
    if i==5:
        break
    print(i,end=' ')


# ## Ejercicio
# 
# 1. Utiliza un ciclo `while` para hallar el factorial de un número. Recuerda que el factorial de un número es el producto de todos los enteros positivos hasta él.

# In[15]:


n = 10
i = 1
factorial = 1
while i<=n:
    factorial = i*factorial
    i = i+1 
print(factorial)


# In[ ]:





# In[17]:


n = 100
i = 1
print('Los divisores de {0:1d} son:'.format(n),end=' ')
while i<=n:
    if n%i==0:
        print(i,end=' ')
    i = i+1 


# ## Ejercicio
# 1. Elabora un código para determinar si un cierto número es primo o no.

# una forma de aproximar la raíz cuadrada de un número $a$, es utilizando la aproximación 
# \begin{equation*}
# y=\frac{x^2+a}{2x},
# \end{equation*}
# siendo $x$ cualquier número positivo y $y$ la aproximación obtenida. Si se aplica la aproximación sobre el resultado inmediatamente anterior, se obtendrá una mejora notable, de modo que, emplearemos este hecho para aproximar raíces cuadradas:

# In[26]:


a = 10
x = 1
while abs(x**2-a)>0.001:
    y = (x**2+a)/(2*x)
    x = y
    print(x)

