#!/usr/bin/env python
# coding: utf-8

# # Bucles
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
# 

# Python permite utilizar ordenes que pueden interrumpir los búcles:
# 
# * **break**: Una sentencia de Python que termina inmediatamente un ciclo por completo. El programa procede a la primera instrucción que sigue después de `break`.
# * **continue**: Una sentencia de Python que termina inmediatamente una iteración del ciclo. El programa procede a la primera instrucción que sigue después de `break`.
