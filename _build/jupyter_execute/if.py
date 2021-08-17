#!/usr/bin/env python
# coding: utf-8

# # Condicionales

# El `if` se utiliza para evaluar expresiones condicionales, si cierta condición se satisface, se ejecuta un determinado bloque de código, y en caso de no satisfacer la condición puede que ejecute otro bloque de código, evalúe otra condición o simplemente no haga nada. Nosotros abordaremos todos los casos, pero debemos hacerlo desde el caso más sencillo:
# 
# Si se cumple cierta condición, ejecute un bloque de código, si no se cumple no haga nada.
# 
# Como debemos verificar la validez o no de una condición, la condición que ingresemos debe arrojar como resultado una variable booleana (`True` o `False`).
# 
# La estructura es la siguiente:
# 
# ```
# if (condición):
#     instrucción 1
#     instrucción 2
#     
#     instrucción n
# ```

# In[1]:


if True:
    print('El valor de verdad de la condición es verdadero')
    


# In[2]:


if False:
    print('El valor de verdad de la condición es falso')


# note que en el bloque de código anterior no hubo respuesta alguna, esto ocurre porque la condición es falsa. 
# 
# **if ... else:**
# 
# Este es el segundo caso que podemos tener en un `if`, y es: verifique una condición, si se cumple ejecute un bloque de código, si no se cumple, ejecute otrobloque de código.
# 
# Su estructura es la siguiente:
# 
# ```
# if (condición):
#     instrucción 1
#     instrucción 2
#     
#     instrucción n
# else:
#     instrucción 1
#     instrucción 2
#     
#     instrucción m
# ```
# 
# Ahora verificaremos si un número que nosotros digitemos es positivo o no:

# In[3]:


n = int(input('Escribe el número que deseas verificar: '))


# In[4]:


if n>0:
    print('El número es positivo')
else:
    print('El número no es positivo')


# Para verificar si un número dado es par o no, podemos utilizar el siguiente bloque de código:

# In[5]:


m = 4
if m%2==0:
    print('{0:1d} es par'.format(m))
else:
    print('{0:1d} es impar'.format(m))


# **if ... elif:**
# 
# El tercer caso, es el siguiente:
# si se cumple cierta condición ejecute cierto bloque de código, sino, verifica otra condición si se cumple ejecuta otro bloque de código y si no se cumplen las condiciones anteriores, ejecute otro bloque de cpodigo.
# 
# Su estructura es la siguiente:
# 
# ```
# if (condición1):
#     instrucción 1
#     instrucción 2
#     
#     instrucción n
# elif (condición2):
#     instrucción 1
#     instrucción 2
#     
#     instrucción m
# else 
#     instrucción 1
#     instrucción 2
#     
#     instrucción l
# ```
# 
# Pero si deseamos verificar si el número es positivo negativo o cero, 

# In[6]:


k=0
if k>0:
    print('El número es positivo')
elif k<0:
    print('El número es negativo')
else:
    print('El número es cero')


# Ahora modificaremos ligeramente el código anterior para verificar la ley de tricotomía entre un par de números reales:

# In[7]:


a=3
b=-4
if a>b:
    print('{mayor} es mayor que {menor}'.format(mayor=a,menor=b))
elif a<b:
    print('{mayor} es mayor que {menor}'.format(mayor=b,menor=a))
else:
    print('Los números son iguales')


# **Nota:**
#     
# Podemos anidar múltiples `elif`, dependiendo de la cantidad de condiciones que necesitemos imponer.

# ## Ejercicios
# 
# Una materia se evaluó con 5 notas con los siguientes porcentajes: *Nota 1:* $10%$, *Nota 2:* $15%$, *Nota 3:* $20%$, *Nota 4:* $25%$ y *Nota 5:* $30%$.
# 
# 1. Escriba un bloque de código que le permita al usuario introducir sus 5 notas y que calcule su definitiva.
# 2. Si se desea dejar un comentario en el sistema, dependiendo de la nota obtenida, haga un bloque de código de tal forma que clasifique a los estudiantes según su definitiva, como sigue: 
# * Rendimiento deficiente $0\leq definitiva \leq 1.5$.
# * Rendimiento insuficiente $1.5< definitiva < 3$.
# * Rendimiento aceptable $3\leq definitiva \leq 3.8$.
# * Rendimiento sobresaliente $3.8< definitiva \leq 4.5$.
# * Rendimiento sobresaliente $4.5< definitiva \leq 5$.
# 

# En las condiciones también podemos tener operadores lógicos, como podremos ver en las siguientes líneas:

# In[8]:


x=2
if (x%2==0 and x%3==0):
    print(x,'es divisible por 2 y 3')


# In[9]:


x=5
if (x%2==0 and not x%3==0):
    print(x,'es divisible por 2 y no por 3')
elif (not x%2==0 and x%3==0):
    print(x,'es divisible por 3 y no por 2')
elif (x%2==0 and x%3==0):
    print(x,'es divisible por 2 y 3')
else:
    print(x,'no se puede dividir ni por 2 ni por 3')

