#!/usr/bin/env python
# coding: utf-8

# # Bucles (while)
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

# ## Iteración
# 
# Una iteración consiste en una secuencia de instrucciones que se repiten cierta cantidad de veces, dicha operación puede depender de una condición de verdad (`while`), o recorrer una lista definida (`for`). 
# 
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 50.00%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1000" height="500" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/61944099c121b10d88a24212" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# ## Bucle while
# 
# Es similar al condicional, porque revisará si una condición es cierta o falsa, y se ejecutará mientras esa condición sea cierta. Es muy importante que la condición en while cambié a medida que avanza la iteración, porque si no el programa ejecutará indefinidamente las operaciones. Su sintáxis es:
# 
# ```Python
# while (condición):
#     instrucción_1
#     instrucción_2
#     ...
#     instrucción_n
# ```
# 
# :::{warning}
# ¡Cuidado con la condición! Existe la posibilidad de escribir la condición de tal manera que siempre se cumpla y tendríamos un ciclo infinito.
# :::

# **Ejemplo**
# 
# Mientras una variable a la que inicialmente se le asigno el valor 0 sea menor que 10 que el programa imprima  `Python es maravilloso`:

# In[1]:


n=0
while n<10:
    n=n+1 # esta operación es fundamental, si no la incluimos el ciclo sería infinito...
    print(n)
    print('Python es maravilloso')
    
    


# ¿Qué pasaría si escribimos el siguiente código?
# 
# ```Python
# n=0
# while n<10:
#     #n=n+1 # esta operación es fundamental, si no la incluimos el ciclo sería infinito...
#     print(n)
#     print('Python es maravilloso')
# ```
# Si ejecutó estas instrucciones y su computador se quedó ejecutando entonces oprima [Ctrl]+[C] para cancelar la ejecución, si no el computador ejecutará la orden infinitamente.

# Python permite utilizar ordenes que pueden interrumpir los búcles:
# 
# * **break**: Una sentencia de Python que termina inmediatamente un ciclo por completo. El programa procede a la primera instrucción que sigue después de `break`.
# * **continue**: Una sentencia de Python que termina inmediatamente una iteración del ciclo. El programa procede a la primera instrucción que sigue después de `break`.

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 116.67%; padding-top: 0; height: 0;"><iframe frameborder="0" width="600" height="700" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/6197bf60b2eaa20dad025cd1" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# Veamos un ejemplo:

# In[2]:


n = 0
while n < 5:
    n += 1
    if n == 2:
        break     
    print(n)
print('Bucle terminado.')


# In[3]:


n = 0
while n < 5:
    n += 1
    if n == 2:
        continue     
    print(n)
print('Bucle terminado.')


# ## Bucle `while:...  else:... `
# 
# Esta es una propiedad caracterpística de Python, permite mostrar un resultado si y solo si un bucle termina. Si el bucle no pudo terminar no se mostrará:

# In[4]:


n = 0
while n<5:
    n += 1
    print(n)
else:
    print('Bucle terminado')


# In[5]:


n = 0
while n<5:
    n += 1
    print(n)
    if n==4:
        print('Bucle roto')
        break    
else:
    print('Bucle terminado')
print('Como no dice "Bucle terminado", el else no se ejecutó')


# Un ejemplo más interesante puede ser para buscar elementos en una lista:

# In[6]:


FV = ['Papa', 'Limón', 'Cebolla', 'Arroz']
s = 'Chocolate'

i = 0
while i < len(FV):
    if FV[i] == s:
        print(s, 'fue encontrado en la lista.')
        break
    i += 1
else:
    print(s, 'no fue encontrado en la lista.')


# In[7]:


FV = ['Papa', 'Limón', 'Cebolla', 'Arroz','Chocolate']
s = 'Chocolate'

i = 0
while i < len(FV):
    if FV[i] == s:
        print(s, 'fue encontrado en la lista.')
        break
    i += 1
else:
    print(s, 'no fue encontrado en la lista.')
    


# ## Bucles anidados
# 
# En general, las estructuras de control de Python se pueden anidar, es decir, poner unas dentro de otras. Por ejemplo:

# In[8]:


su_edad=20
genero='M'
if su_edad < 10:
    if genero == 'M':
        print('Niño')
    else:
        print('Niña')
elif su_edad >= 10 and su_edad < 18:
    if genero == 'M':
        print('chico')
    else:
        print('chica')
else:
    if genero == 'M':
        print('Señor')
    else:
        print('Señora')


# En el caso de while podemos hacer algo muy parecido, por ejemplo:

# In[9]:


n=0
while n<5: 
    m=10 #---> esto se ejecuta el primer while     
    while  m>5:
        print(n,'+',m,'=',n+m) #---> solo se ejecuta el segundo while 
        m-=1
    n+=1  #---> esto se ejecuta el primer while 


# Podemos combinar `if` y  `while`

# In[10]:


su_edad=8
genero='F'
while su_edad<25:
    if su_edad < 10:
        if genero == 'M':
            print('Tiene',su_edad,'años. Es un niño.')
        else:
            print('Tiene',su_edad,'años. Es una niña.')
    elif su_edad >= 10 and su_edad < 18:
        if genero == 'M':
            print('Tiene',su_edad,'años. Es un chico.')
        else:
            print('Tiene',su_edad,'años. Es una chica.')
    else:
        if genero == 'M':
            print('Tiene',su_edad,'años. Es un señor.')
        else:
            print('Tiene',su_edad,'años. Es una señora.')
    su_edad+=1


# Como vemos, todas las estructuras de control de Python se pueden combinar en la medida que sea necesario. Esto hace que Python sea un lenguaje aclamdo, fácil y flexible. Usaremos muchos trucos de este estilo en diversos ejemplos.

# ## Bucles de una línea
# 
# Como `if` también puedo definir bucles de while en una sola línea:
# 
# ```Python
# while (condición): instrucción_1;instrucción_2
# ```
# 
# 

# In[11]:


n=0
while n<5:n+=1;print(n);


# Esto funciona solo para expresiones simples, si, por ejemplo, busamos anidar en una sola línea tendremos problemas. 

# In[12]:


while n < 5: n -= 1; if True: print(n)


# ## Cierre

# Avanzamos en el mundo de la iteración utilizando while, nos enfrentamos a varios ejerciciocios que conforme vamos avanzando se vuelven más complejos. No dejes que la fuerza se termine, aún debemos hacer muchas cosas más.

# ## Ejercicio 1
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


# In[17]:


n = 100
i = 1
print('Los divisores de {0:1d} son:'.format(n),end=' ')
while i<=n:
    if n%i==0:
        print(i,end=' ')
    i = i+1 


# ## Ejercicio 2
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

