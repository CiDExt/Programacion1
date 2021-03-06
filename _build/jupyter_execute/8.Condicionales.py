#!/usr/bin/env python
# coding: utf-8

# # Condicionales (if)

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

# ## Programación estructurada
# 
# Volviendo al teorema del programa estructurado o [teorema de Böhm–Jacopini](https://en.wikipedia.org/wiki/Structured_program_theorem) sabemos que toda función computable se puede implementar utilizando tres estructuras lógicas que permiten modificar el orden de ejecución del programa. A dichas estructuras las llamamos  **estructuras de control** y  corresponden a las siguientes:
# 
# *Secuencia:*  Que se entiende como la posibilidad de ejecutar una instrucción tras otra.
# *Selección:* Que ejecuta una de dos o más secuencias acorde al valor de una expresión booleana.
# *Iteración:* Que ejecuta una serie de instrucciones mientras una variable booleana es verdadera.
# 
# Claramente la secuenciación de un programa indica que hay un orden para ejecutar las instrucciones, estudiaremos entonces las estructuras de seleccción, iniciando con la más sencilla de todas: **el condicional**.
# 

# ## Condicional básico `if`

# El `if` se utiliza para evaluar expresiones condicionales, si cierta condición se satisface, se ejecuta un determinado bloque de código, y en caso de no satisfacer la condición puede que ejecute otro bloque de código, evalúe otra condición o simplemente no haga nada. Nosotros abordaremos todos los casos, pero debemos hacerlo desde el caso más sencillo:
# 
# ```
# Si se cumple cierta condición, ejecute un bloque de código, si no se cumple no haga nada.
# ```
# 
# 
# 
# Como debemos verificar la validez o no de una condición, la condición que ingresemos debe arrojar como resultado una variable booleana (`True` o `False`).
# 
# La estructura es la siguiente:
# 
# ```Python
# if (condición):
#     instrucción 1
#     instrucción 2  
#     ...
#     instrucción n 
# ```
# 
# :::{admonition} Importante
# :class: tip
# En la estructura anterior `condición` hace referencia a una sentencia booleana, cuyos resultados pueden ser verdadero (`True`) o falso (`False`). Téngalo en cuenta siempre que establezca igualdad, donde la sintáxis correcta es `x==y`y no `x=y`.
# 
# Otro elemento importante es que en esta estructura de control aparece una característica destacada de Python, **la identación**, como ven, las instrucciones que se ejecutan después de validar la condición se escriben con una sangría a la derecha. Una identación equivocada puede llevar a un error de sintáxis por identación. No hay problema en los comandos utilizados sino un mal manejo de los espacios. Ver los ejemplos siguientes.
# :::

# Veamos que ocurre cuando la condición es verdadera:

# In[1]:


if True:
    print('El valor de verdad de la condición es verdadera')
    


# Cuando no es así:

# In[2]:


if False:
    print('El valor de verdad de la condición es falso')


# note que en el bloque de código anterior no hubo respuesta alguna, esto ocurre porque la condición es falsa. 
# 
# Veamos que ocurre si no respetamos la identación:

# In[3]:


if True:
print('El valor de verdad de la condición es verdadero')


# Aquí tenemos error porque no hay sangría después de los dos puntos que delimitan el final de la condición. 
# 
# Finalmente, comprobemos cómo actúa la sangría en la ejecución de instrucciones según el valor de verdad de la condición:

# In[7]:


if True:
    print('Esta instrucción se ejecuta si la condición es verdadera...')
    print('Esta también...\n')
print('Esta instrucción se ejecuta por fuera del condicional.')


# In[9]:


if False:
    print('Esta instrucción se ejecuta si la condición es verdadera...')
    print('Esta también...\n')
print('Esta instrucción se ejecuta por fuera del condicional.')


# Esta imagen no puede ser más aclaradora:
# 
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 50.00%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1600" height="800" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/6197b7ab39b5540d7ef9d12e" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# **Ejemplo**
# 
# Diseñe un algoritmo que identifique si es de día, necesitará determinar la hora actual y saber que diremos que es de dia si la hora está entre las 6:00am y las 6:00pm. Para obtener la hora actual use del modulo `datetime` en el paquete `datetime` el método `now` como sigue:
# 

# In[13]:


from datetime import datetime
Ahora=datetime.now()
Ahora


# Esa instancia que acabo de obtener le puede dar la hora usando:

# In[14]:


Ahora.hour


# ::::{admonition} **Solución**
# :class: tip, dropdown
# Una solución simple puede ser:
# 
# ```Python
# from datetime import datetime
# Ahora=datetime.now()
# Ahora
# if Ahora.hour<18 or Ahora.hour>=6:
#     print( 'Es de día')
# ```
# 
# ::::

# Dentro de cada bloque en el que se ejucuta un condicional se puede incluir otro. Lo podemos hacer a una profundidad arbitraria y debemos entender que es la sangria la que indica el nivel en el que hemos anidado el condicional. 
# 
# En el siguiente script es evidente que estamos haciendo, apesar de que no definimos `in` es claro a que alude y vemos como la filosofia de Python permite entender el pseudocódigo a partir del script. Después de entender este ejercicio haga un diagrama de flujo o describa el pseudocódigo del algoritmo que estudiamos a continuación:

# In[2]:


# ¿Esta linea se ejecuta?                                   SÍ    NO
#                                                          ---   ---
if 'foo' in ['foo', 'bar', 'baz']:                       #  x
    print('Vale la condición "externa"')                 #  x

    if 10 > 20:                                          #  x
        print('No vale la condición "interna" 1')        #        x

    print('Una sentencia que depende del primer if')     #  x

    if 10 < 20:                                          #  x
        print('Si vale la condición "interna" 2')        #  x

    print('Una sentencia que depende del primer if')     #  x
print('Una sentencia independiente')                     #  x


# ## Condicional de la forma **if ... else:**

# 
# Este es el segundo caso en el que podemos tener en un `if`, la estructura de selección hace lo siguiente verifica una condición, si se cumple ejecuta un bloque de código, si no se cumple, ejecuta otro bloque de código.
# 
# Su esquema es el siguiente:
# 
# ```Python
# if (condición):
#     instrucción_positiva 1
#     instrucción_positiva 2
#     ...
#     instrucción_positiva n
# else:
#     instrucción_negativa 1
#     instrucción_negativa 2
#     ...
#     instrucción_negativa m
# ```
# 
# Ahora verificaremos si un número que nosotros digitemos es positivo o no:

# ```Python 
# n = int(input('Escribe el número que deseas verificar: '))
# ```

# El condicional debe tener una estructura como sigue:
# 

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 50.00%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1000" height="500" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/61948c5ec121b10d88a24d1d" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# ::::{admonition} **Programa Simple**
# :class: tip, dropdown
# Identificar si el número ingresado es positivo:
# 
# ```Python
# n=input('Escriba un número entero: ')
# if n>0:
#     print('El número es positivo')
# else:
#     print('El número no es positivo')
# ```
# 
# ::::

# Para verificar si un número dado es par o no, podemos utilizar el siguiente bloque de código:
# 
# ::::{admonition} **Programa Simple**
# :class: tip, dropdown
# Identificar si el número ingresado es positivo:
# 
# ```Python
# m=input('Escriba un número entero: ')
# if m%2==0:
#     print('{0:1d} es par'.format(m))
# else:
#     print('{0:1d} es impar'.format(m))
# ```
# 
# ::::

# ## Condicional **if...elif...**

# El tercer caso, es el siguiente: si se cumple cierta condición ejecute cierto bloque de código, sino, verifica otra condición si se cumple ejecuta otro bloque de código y si no se cumplen las condiciones anteriores, ejecute otro bloque de código.
# 
# Su estructura es la siguiente:
# 
# ```Python
# if (condición1):
#     instrucción_1 1
#     instrucción_1 2
#     ...
#     instrucción_1 n_1
#     
# elif (condición2):
#     instrucción_2 1
#     instrucción_2 2
#     ...
#     instrucción_2 n_2
# elif (condición3):
#     instrucción_3 1
#     instrucción_3 2
#     ...
#     instrucción_3 n_3
# ...
# else 
#     instrucción_m 1
#     instrucción_m 2
#     
#     instrucción_m n_m
# ```
# 

# Contamos con más opciones:
# 
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 50.00%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1000" height="500" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/61948e24726a1e0dcf416eaa" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# In[10]:


k=0
if k>0:
    print('El número es positivo')
elif k<0:
    print('El número es negativo')
else:
    print('El número es cero')


# Ahora modificaremos ligeramente el código anterior para verificar la ley de tricotomía entre un par de números reales:

# In[11]:


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

# ## Sintáxis de una línea
# 
# En ocasiones, escribir tantas líneas de código resulta abrumador, y hay algunas sentencias simples que para un estilo de escritura de programación (que tiene que ver más con el desarrollador) podrían ser exageradas definidas como bloques con una indentación adecuada, 
# 
# Afortunadamente Python admite que nosotros pongamos condicionales en una línea, escribimos lo siguiente:
# 
# 
# ```Python
# if (condición): instrucción_1; instrucción_2; ...;instrucción_n
# 
# ```

# In[2]:


if 20<100: print('20 es menor que 100'); print('Esta es una sentencia condicional de una línea')


# El punto y coma separa las instrucciones, si la condición no se satisface todo lo que esta al frente de los dos puntos no se ejecuta.

# In[3]:


if 20>100: print('20 es mayor que 100'); print('Esta es una sentencia condicional de una línea')


# Los bloques que dependen de `else`, y `elif` se dejan en líneas aparte:
# ```Python
# if (condición_1): instrucción_1_1; instrucción_1_2; ...;instrucción_1__n;
# elif (condición_2): instrucción_2_1; instrucción_2_2; ...;instrucción_2_m;
# else (condición_3): instrucción_3_1; instrucción_3_2; ...;instrucción_3_k;
# ```

# In[5]:


if 20>100: print('20 es mayor que 100'); print('Esta es una sentencia condicional de la línea if')
elif 20<100: print('20 es menor que 100'); print('Esta es una sentencia condicional de la línea elif')
else: print('20 es igual que 100'); print('Esta es una sentencia condicional de la línea else')


# In[6]:


if 20<100: print('20 es menor que 100'); print('Esta es una sentencia condicional de la línea if')
elif 20==100: print('20 es igual que 100'); print('Esta es una sentencia condicional de la línea elif')
else: print('20 es mayor que 100'); print('Esta es una sentencia condicional de la línea else')


# In[7]:


if 20>100: print('20 es mayor que 100'); print('Esta es una sentencia condicional de la línea if')
elif 20==100: print('20 es igual que 100'); print('Esta es una sentencia condicional de la línea elif')
else: print('20 es menor que 100'); print('Esta es una sentencia condicional de la línea else')


# Usar esta sintáxis no es tan agradable a la vista como la clásica, pero podría ser funcional para condicionales simples.

# ## Operador ternario
# 
# Uno de los elementos interesantes de Python es que permite sugerencias de los usuarios para mejorar su sintáxis en pro de tener una mejora del lenguaje. La documentación de estas mejoras se puede encontrar en los [índices PEP](https://www.python.org/dev/peps/) de la página oficial. Entre ellos hay una que se hizo a los condicionales con el fin de introducir el [operador ternario](https://es.wikipedia.org/wiki/Operador_ternario) de otros lenguajes como C, Java o Perl.
# 
# En este operador la idea es tomar tres argumentos: (condición; valor si la condición es cierta; valor si la condición es falsa) y dar un resultado acorde a la validación. En los lenguajes clásicos ésta se expresaba así:
# 
# ```
# expresión boleana ? valor si cierto : valor si falso
# 
# ```
# 
# En Python, la sintaxis es:
# 
# ```Python
# valor_si_cierto if condición else valor_si_falso
# ```

# Veamos un ejemplo en el cual asignaremos `Pasó` si la nota es mayor o igual que 3 y `Perdió` si la nota es menor que 3:

# In[3]:


nota=2.5
'Pasó' if nota>3 else 'Perdió'


# In[4]:


nota=4.5
'Pasó' if nota>3 else 'Perdió'


# Ese resultado lo podemos asignar a una variable:

# In[7]:


nota=4.5
res='Pasó' if nota>3 else 'Perdió'

print('En esta nota usted: '+res)


# ## Dejemoslo pasar con `pass`
# 
# Hay veces en que usamos un condicional pero no tenemos que hacer nada, por ejemplo:
# 

# In[1]:


if 5>1:
    print('No hago nada')
else:
    print('5 es menor que 1')


# Aunque imprimí  `No hago nada`sí estoy haciendo algo **imprimir `No hago nada`** para resolver este lío podríamos no escribir nada, así:

# In[9]:


if 5>1:
else:
    print('5 es mayor que 1')


# Pero la indentación me lo cobra caro.  Este problema lo arreglamos con `pass`:

# In[10]:


if 5>1:
    pass
else:
    print('5 es mayor que 1')


# Y aquí de verdad que no hicimos nada.

# En las condiciones también podemos tener operadores lógicos, como podremos ver en las siguientes líneas:

# In[12]:


x=2
if (x%2==0 and x%3==0):
    print(x,'es divisible por 2 y 3')


# In[13]:


x=5
if (x%2==0 and not x%3==0):
    print(x,'es divisible por 2 y no por 3')
elif (not x%2==0 and x%3==0):
    print(x,'es divisible por 3 y no por 2')
elif (x%2==0 and x%3==0):
    print(x,'es divisible por 2 y 3')
else:
    print(x,'no se puede dividir ni por 2 ni por 3')


# ## Cierre
# 
# Esta es nuestra primera experiencia con una estructura de control, aquí podemos seleccionar bloques de código e incluso aplicar esa idea en la definición de variables. en lo que sigue trabajaremos con las iteraciones, una estructura que permite repetir varias veces una secuencia de instrucciones. 

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
