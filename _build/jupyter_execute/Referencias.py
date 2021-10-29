#!/usr/bin/env python
# coding: utf-8

# # Referencias (Apuntadores):
# En Python, el usuario relaciona las variables y su contenido mediante una referencia, la cual es a la dirección en la cual se encuentra alojado dicho objeto en la memoria del computador, esto en otros lenguajes se conoce como apuntador. Por ejemplo, en una asignación como la siguiente: `x = 1`, `x` no contiene el valor 1, pero sí información de un objeto en la memoria, en el cual se se encuentra alojado tal valor. En otras palabras, podríamos afirmar que `x` "apunta" o "se refiere" a un objeto en el cual se halla alojado el 1.
# 
# Algo que debemos tener claro es que dos objetos diferentes no pueden estar alojados en la misma dirección, es decir, cada objeto tiene una única dirección en la memoria. No nos es posible acceder a la dirección de los objetos, pero podemos acceder al identificador único que ellos poseen, mediante la función `id(x)`, así:

# In[1]:


x = 1


# In[2]:


id(x)


# Muy probablemente, este número entero que obtuvimos, conocido como la **identidad** del objeto, sea diferente en cada máquina y en cada oportunidad que reiniciemos el kernel. El siguiente es un ejempo muy claro en el cual podremos ver que la identidad de cada objeto es única:

# In[3]:


def cuadrado(x):
  print('El valor es:',x,'su identidad es:',id(x))
  print('Su cuadrado es:',x**2,'y su identidad es:',id(x**2))
  return x**2


# In[4]:


cuadrado(1)


# In[5]:


cuadrado(x)


# Notemos que la función `cuadrado` regresa el mismo valor de identidad para 1, su cuadrado, $x$ y su cuadrado, ya que en ambos casos hablamos del mismo objeto, mientras que para el siguiente caso el valor de la identidad del parámetro y de su cuadrado cambian:  

# In[6]:


cuadrado(2)


# Para comprobar que dos elementos tienen la misma identidad empleamos la función `is`, así:

# In[7]:


x is 1


# In[8]:


2 is x+1


# Notemos que, la función puede recibir la referencia a un objeto inmutable o inmodificable, y por más cálculos que se hagan sobre dicho objeto, éste no se podrá afectar, por ejemplo: 

# In[9]:


y = 2


# In[10]:


def cuadrado(x):
  print('El valor es:',x,'su identidad es:',id(x))
  x = x**2
  print('Su cuadrado es:',x,'y su identidad es:',id(x))
  return y


# In[11]:


cuadrado(y)


# In[12]:


y


# Cabe resaltar que si no hacemos uso de la referencia del valor original, se estará almacenando un poco de *basura* en nuestra memoria.

# In[ ]:




