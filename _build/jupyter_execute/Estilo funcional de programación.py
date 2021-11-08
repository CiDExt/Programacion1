#!/usr/bin/env python
# coding: utf-8

# # Estilo funcional de programación

# En los casos en los cuales nuestras funciones tengan una gran cantidad de tareas para abordar, lo mejor es distribuir éstas en diferentes funciones, para que así podamos identificar los fallos en alguna parte del código de manera más eficiente y también para hacer mucho más fácil la lectura del código para otros e incluso para nosotros mismos.

# In[1]:


def suma(a,b):
    return a+b

def resta(a,b):
    return a-b
  
def producto(a,b):
    return a*b

def cociente(a,b):
    return a/b

def operaciones(a,b):
    s = suma(a,b)
    r = resta(a,b)
    p = producto(a,b)
    c = cociente(a,b)
    return 'suma: {}, resta: {}, producto: {}, cociente: {}'.format(s,r,p,c)


# In[2]:


operaciones(1,2)


# Lo anterior nos muestra algo que debemos tener presente, y es que en las funciones se maneja el concepto del *Último en Entrar es el Primero en Salir* (*UEPS*), es decir, la última función que se llama es la primera sobre la cual se termina el cálculo, para así poder utilizar su respuesta en los cálculos posteriores.
# 
# Este concepto del UEPS es muy familiar en programación, y lo usamos casi que a diario sin darnos cuenta, por ejemplo, en nuestro navegador cuando vamos de una página a otra y pulsamos el botón `atrás` éste nos regresa al más reciente de todos los sitios que visitamos.

# In[3]:


operaciones(2,3)


# In[4]:


s


# Como podemos ver, las variabes `s`, `r`, `p` y `c` son variables locales dentro de la función `operaciones`, por ello no se almacenan en nuestra memoria.
# 
# Un riesgo que podemos correr al tener una función con demasiadas tareas, es quedarmos sin memoria, ya que ésta no se liberará hasta no terminar los cálculos de la función en la cual estamos, por ello, el estilo funcional es muy propicio para evitar este tipo de errores, claro, esto también podría ocurrir si tenemos alguna función que no termine nunca su ejecución.
# 
# Este estilo de programación es particularmente útil, ya que, permite al lector del código entender de una manera más fácil *qué* se pretende hacer con las funciones elaboradas, sin tener que esforzarse mucho con el *cómo* se hace, ya que casi siempre ésto viene cubierto por las diferentes librerías que tenemos a la mano. Otra ventaja que tenemos al emplear este tipo de programación es permitir la *inmutabilidad* de variables, pues esto evita errores que se pueden introducir de manera involuntaria al *mutar* o cambiar alguna variable, que afectará otras y posiblemente el resultado que deseamos calcular, como pasa en la función `operaciones`, ya que ésta función no puede modificar ninguna de las asignaciones que se realizan en las funciones `suma`, `resta`, `producto` y `cociente`.

# ## Ejercicios
# 1. Crea una función que le permita calcular el peso de una nota en la definitiva de una materia, es decir, que dada una nota y el porcentaje que ella vale, arroje como resultado el valor que ésta aporta a la definitiva (nota * porcentaje).
# 2. Continuando con el ejercicio anterior, crea una función que reciba dos, una en la cual se halla cada nota y otra en la que se encuentran almacenados los porcentajes que valen cada una de éstas notas y arroje como resultado la definitiva de la materia. Ten en cuenta que el porcentaje debe ser exactamente el 100% y que las listas deben tener la misma longitud.
# 3. Crea una función que calcule el MCD de dos números por el método de Euclides. Éste método siguiente:
# 
#  * Se divide el número mayor entre el menor.
#  * Si la división es exacta, el divisor es el MCD.
#  * Si la división no es exacta, dividimos el divisor entre el resto obtenido y se continúa de esta forma hasta obtener una división exacta, siendo el último divisor el MCD.
# 
# 4. En este ejercicio crearemos diferentes funciones para trabajar con fracciones:
#  * Crea la función `LeerFracciones` que reciba como entrada la fracción `a/b`, cuyo resultado sea la fracción simplificada.
#  * Crea la función `SimplificarFracciones` que se encargue de simplificar la fracción de entrada `a/b`, recuerda que si el denominador es 1, la respuesta debería ser únicamente el numerador.
#  * Crea la función `SumaFracciones` la cual reciba como entrada dos fracciones (`n1/d1`,`n2/d2`) y su retorno sea la suma de dichas fracciones simplificada (`numerador = n1*d2+n2*d1`,`denominador = d1*d2`).
#  * Crea la función `RestaFracciones` la cual reciba como entrada dos fracciones (`n1/d1`,`n2/d2`) y su retorno sea la resta de dichas fracciones simplificada (`numerador = n1*d2-n2*d1`,`denominador = d1*d2`).
#  * Crea la función `MultiplicaFracciones` la cual reciba como entrada dos fracciones (`n1/d1`,`n2/d2`) y su retorno sea el producto de dichas fracciones simplificada (`numerador = n1*n2`,`denominador = d1*d2`).
#  * Crea la función `DivideFracciones` la cual reciba como entrada dos fracciones (`n1/d1`,`n2/d2`) y su retorno sea el cocioente de dichas fracciones simplificada (`numerador = n1*d2`,`denominador = d1*n2`).
