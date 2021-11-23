#!/usr/bin/env python
# coding: utf-8

# # Funciones: Argumentos

# :::::{important} ¿Qué sabemos de las funciones?
# 
# En el cuaderno anterior, aprendimos a definir y a invocar funciones. Ahora aprenderemos a manera de manipular los argumentos de las funciones que creemos.
# 
# ````{tabbed} ¿El orden importa?
# 
# :::{admonition} Recordemos...
# :class: tip
# En las funciones que definimos ocurre lo mismo que en las funciones matemáticas, **el orden es fundamental**.
# :::
# ````
# 
# ````{tabbed} Ejemplo
# 
# :::{admonition} La resta
# :class: tip
# Sabemos que 2-3 es diferente a 3-2.
# :::
# ````
# 
# 
# ````{tabbed} Ejemplo
# 
# :::{admonition} Al vestirse
# :class: tip
# Si primero nos ponemos las medias y luego los zapatos, generará un resultado distinto a ponerse primero los zapatos y luego las medias.
# :::
# ````
# 
# :::::

# ## Argumentos por defecto:
# 
# En la función que calculaba el valor, con y sin impuestos, de una cuenta en un cierto restaurante nos hizo falta incluir el valor de la propina, ajuste que realizaremos en este momento:

# In[1]:


def costos(comensales,propina=10):
    Cuenta = round(comensales*50000,2)
    CuentaSinImp = round(Cuenta*100/108,2)
    CuentaConProp = round(Cuenta*(1+propina/100),2)
    x = '''    Valor Neto: '''+str(CuentaSinImp)+'''
    Total sin propina: '''+ str(Cuenta)+ '''
    Total con propina: '''+ str(CuentaConProp)
    print(x)


# In[2]:


costos(1)


# Nota que en la función anterior el segundo argumento tiene un valor predeterminado `propina=10`, esto quiere decir que, si no modificamos su valor, la función asumirá éste como el valor predeterminado, es decir, las propinas serán del $10\%$ salvo que se indique algún otro valor. Por ejemplo si deseamos calcular el total de la cuenta con una propina del $7\%$, ejecutamos las siguientes líneas de código:

# In[3]:


costos(1,7)
#Estamos considerando los argumentos posicionalmente


# In[4]:


costos(propina=7,comensales=1)
#Estamos haciendo referencia directa al valor de los argumentos


# Lo presentado en la línea anterior suele emplearse únicamente cuando se tienen diferentes variables predeterminadas y no con las variables obligatorias, esto con el fin de evitar malas interpretaciones de las entradas.

# ## Argumentos de longitud variable:
# En diversos lenguajes de programación existe dos tipos de argumentos ampliamente utilizados `args` y `kwargs` (**arg**ument**s** y **k**ey**w**ord**arg**ument**s** ), en Python los `args` son tuplas y los `kwargs` son diccionarios (estructuras que estudiaremos en profundidad más adelante), estos argumentos permiten agregar cualquier cantidad de entradas a las funciones como podemos ver en las siguientes funciones:

# In[5]:


def f1(*args):
    return sum(args)


# In[6]:


f1(1,2,3,4,5)


# In[7]:


f1(1,2.3)


# In[8]:


#Note que si se introduce un argumento no numérico la función generará un error
f1('hola')


# Este tipo de argumentos nos permite definir, entre muchas otras, una función que calcule el promedio de una lista de números dados
# 

# In[9]:


def promedio(*args):
    return sum(args)/len(args)


# In[10]:


promedio(1,2,3,4,5.2,3.1,4)


# Es importante que note que en la definición de la función, el argumento que será una tupla de tamaño indefinido lleva un `*` antes, esto es lo que le indica a Python el tipo de variable que es, y dentro de la función se utiliza la variable sin el `*`. El nombre puede ser cualquiera pero por convención suele emplearse `args`.
# 
# Los tipos de entrada de éstas variables pueden ser diversos, por ejemplo:

# In[11]:


def imprime(*args):
    if len(args)==0:
        print('No hubo argumentos de entrada.')
    else:
        for i in range(len(args)):
            print('En la entrada {0} se almacenó: {1} y es del tipo {2}'.format(i,args[i],type(args[i])))


# In[12]:


imprime()


# In[13]:


imprime('hola',1)


# También podemos combinar las variables bien sean obligatorias u opcionales con éste tipo de argumentos, por ejemplo:

# In[14]:


def f2(arg1, *argv):
    print ("Primer argumento :", arg1)
    for arg in argv:
        print("Siguiente argumento en la tupla *argv :", arg)


# In[15]:


f2('Hola', 'bienvenido', 'a', 'la', 'Universidad','Externado','de', 'Colombia')


# Si intentamos escribir primero las variables de tamaño indefinido y luego las que necesitamos realmente obtendremos un error, ya que el Python no sabrá en qué momento debe parar de llenar la tupla y seguir con los argumentos fijos, salvo que se especifiquen sus valores como vimos anteriormente:

# In[16]:


def f3(*argv,argn):
    print ("Último argumento :", argn)
    for arg in argv:
        print("Siguiente argumento en la tupla *argv :", arg)


# In[17]:


f3('Hola', 'bienvenido', 'a', 'la', 'Universidad','Externado','de', 'Colombia')


# In[18]:


f3('Hola', 'bienvenido', 'a', 'la', 'Universidad','Externado','de', argn='Colombia')


# ### Ejercicios:
# 1. Crea una función que permita hallar la mediana en una lista de números ingresados en orden ascendente.
# 2. Crea una función que calcule la varianza muestral de los valores ingresados.$$\text{varianza} = \sigma^2 = \frac{1}{n-1}\sum_{i=1}^{n}(x_i-\bar{x})^2,$$ $n=\text{tamaño de la muestra} $  
# $\bar{x} = promedio$  
# $x_i = i-\text{ésimo elemento de la muestra} $
# 3. Cree una función que halle el mínimo de una lista de números dados.
# 4. Cree una función que halle el máximo de una lista de números dados.

# Para introducir los `kwargs` es necesario en el argumento de la función a dicha variable antecederla de `**`, por ejemplo:

# In[19]:


def fkw1(**kwargs):
    for nombre, valor in kwargs.items():
        print("{0} = {1}".format(nombre, valor))


# In[20]:


fkw1(nota1=1.0,nota2=3.5,nota3=5)


# ### Ejercicio:
# 1. Modifica el código anterior para que el programa calcule el promedio de las notas ingresadas.
# 
# En una función de Python podemos tener variables de todo tipo involucradas, como por ejemplo:

# In[21]:


def superfuncion(a,b=5,*args,**kwargs):
    print('El valor del único parámetro obligatorio es: ',a)
    print('El valor del único parámetro con valor predeterminado es: ',b)
    print('Los valores ingresados en la tupla args son: ',args)
    print('Los valores ingresados en el diccionario **kwargs son: ',kwargs)


# In[22]:


superfuncion(1)


# In[23]:


superfuncion(1,2)


# In[24]:


superfuncion(1,2,0,1,2,3)


# In[25]:


superfuncion(1,2,0,1,2,3,val0=0,val1=1,val2=2)


# En este ejemplo podemos ver la clara diferencia entre la tupla almacenada en `args` y el diccionario almacenado en `kwargs`, su manipulación será objeto de cuadernos posteriores, pero es bueno que desde ya tengamos presente su existencia, ya que posteriormente nos serán de gran utilidad.

# ### Ejercicio:
# 1. Cree una función que dado un monto y una lista de personas con sus correspondientes invitados, calcule cuánto debe pagar cada uno si la cuenta se divide en partes iguales.
# 2. Haga un programa que le permita ingresar las notas obtenidas por un estudiante y los porcentajes asociados a ellas, si el porcentaje es del $100\%$ debe arrojar la nota definitiva de la materia y si el porcentaje es inferior debe informarle el valor de la nota acumulada y cuánto debería sacar en el resto de la materia para aprobarla.

# ## Comentarios finales:
# Recuerda que para evitar confusiones en la ejecución de la función los parámetros de ésta deben ir así: variables, variables con asignaciones predeterminadas, args y kwargs
# ```python
# def nombre_de_la_función(v1,...,vn,vp1='algo',...,vpm='algo',*args,**kwargs):
#     lista_de_instrucciones
#     return resultado
# ```
