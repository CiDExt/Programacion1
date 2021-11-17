#!/usr/bin/env python
# coding: utf-8

# # Variables y funciones básicas

# :::::{important} ¿Cómo vamos?
# 
# 
# Hasta el momento debemos tener claro lo siguiente:
# 
# 
# ````{tabbed} ¿Qué hace un programador?
# 
# :::{warning} 
# 
# **La respuesta es sencilla**
# 
# Convertir **soluciones** en instrucciones que pueda seguir un computador
# :::
# 
# se hace a través de algoritmos procesos libres de ambigüedades y con todos los pasos necesarios para llegar a la dichosa solución. Usamos herramientas de representación de los algoritmos: pseudocódigo o diagramas de flujo, que permiten resumir los pasos de un proceso.
# 
# ````
# 
# ````{tabbed} Consola bash
# 
# :::{admonition} Recordemos...
# :class: tip
# Ya pudimos establecer comunicación directa con la máquina a traves la consola, pudimos crear, mover y modificar archivos. Usamos un algoritmo muy simple para crear un nuevo texto e interactuamos con la consola para descubrir todas las propiedades de sus archivos y directorios.
# :::
# ````
# 
# 
# ````{tabbed} Página en github
# 
# :::{admonition} Recordemos...
# :class: tip
# Seguimos un tutorial detallado para empezar a manejar repositorios locales y en línea. Adicionalmente, vimos elementos básicos para la creación de páginas utilizando una rama adicional de los repositorios. Esperamos que en esas páginas haya una descripción completa de sus perfiles, ilusiones y los que serían sus próximos proyectos.
# :::
# ````
# 
# 
# ````{tabbed} Jupyter
# 
# :::{admonition} Recordemos...
# :class: tip
# Seguimos un tutorial para instalar Anaconda y así usar jupyter. Entendimos que tiene dos tipos de celdas: código y texto, y estudiamos el lenguaje Markdown para poder enriquecer el texto de nuestras celdas de código.
# :::
# 
# ````
# :::::
# 
# 

# Hemos recorrido un largo camino para empezar a programar en Python. Sin embargo, fue necesario para reconocer conceptos, herramientas y hábitos que nos llevarán a un buen puerto con nuestras piezas de código. Empezaremos hablando de algunas instrucciones elementales de Python, crearemos nuestros primeros programas, también llamdos **scripts** que posteriormente serán interpretados. Mencionaremos algunos **tipos elementales de datos** y los guardaremos en un espacio de memoría mediante **variables** para transformarlos y generar nueva información. 

# ## ¡Hola mundo!
# 
# Un ejercicio tradicional de cualquier lenguaje es verificar que funciona, para verlo usaremos una celda de código y escrbiremos `print('¡Hola Mundo!')` oprimimos [Shift]+[Enter] (ejecuta y generará una nueva celda) o [Alt]+[Enter] (ejecuta sin crear una nueva celda) o el ícono run en la parte superior del cuaderno y debe aparecer lo siguiente:

# In[1]:


print('¡Hola Mundo!')


# Puede parecer insignificante pero en este ejercicio estamos haciendo varias cosas:
# 
# 1. Diferenciamos la celda de texto con la celda de código. 
# 2. Identificamos un comando para ejecutar, comentamos que Python es un lenguaje interpretado y que permite correr código sin necesidad de compilar, aún así debemos indicarle a la máquina que corra.
# 3. Identificamos la entrada y salida de una celda de código, en gris estará el código que diseñamos y justo abajo el resultado de la ejecución del código. Hay un par de valores que indican la identificación de la salida y la entrada del cuaderno.

# Otro ejercicio interesante es hacer una sencilla operación matemática, en principio Python soporta las operaciones aritméticas básicas y sin ningun problema podemos hacer lo siguiente:
# 
# | **Operador** | **Descripción** |
# | :---: | :---: |
# |`+`|Suma|
# |`-`|Resta|
# |`*`|Multiplicación|
# |`/`|División|
# |`**`|Potencia|

# Usemos a Python como calculadora simple y hagamos algunas cuentas:

# Una suma:

# In[2]:


2+2


# Una resta:

# In[3]:


1000003-65


# Una multiplicación:

# In[4]:


526563255*454544411121


# Una resta de un número muy grande, solo para demostrar que Python puede usar una gran cantidad de memoria:

# In[5]:


3999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999+1


# Una potencia:

# In[6]:


2**6


# Como se puede apreciar en sus cuadernos, cada operación está debidamente identificada y se distingue claramente la salida y la entrada de la celda.

# **Ejercicio**
# 
# Calcule lo siguiente e interprete el resultado:
# 
# ```Python
# In[2]
# ```

# ## Variables
# 
# Una variable en Python sirve para **guardar un valor específico**, ya sea **numérico**, **texto** u otro [**Tipo de Dato**](https://www.w3schools.com/python/python_datatypes.asp) con un nombre que nosotros escojamos. Debemos escribir una expresión de la forma:
# 
# ```Python
# [Nombre de variable]=[Valor para guardar]
# ```
# 
# 
# Por ejemplo, si queremos guardar el valor ` 1` en la variable ` x`, debemos escribir:
# 
# ```Python
# x=1
# ```
# 
# Si queremos guardar el texto ` 'Python es asombroso'` en la variable ` y`, debemos escribir:
# 
# ```Python
# y='Python es asombroso'
# ```
# 

# Hay variables previamente asignadas en Python, como la que acabamos de ejecutar, esta hace referencia a la variable preasignada en Jupyter `In`, cada vez que se ejecuta, Python llama alguna entrada que está guardada en la memoría de nuestra máquina. Esto lo logramos en **Jupyter Notebook** a través del núcleo, un motor computacional de Jupyter que utiliza los recursos del computador (CPU y RAM) para guardar los cálculos. Cada vez que se reinicia el núcleo se pierden todos los datos guardados. Así mismo `Out` guarda todas las salidas posibles.
# 
# 

# :::{note} Variables predefinidas en Python
# 
# A parte de las variables preasignadas, en Python hay palabras reservadas, que no pueden ser usadas para definir variables. Una forma de verlas es utilizando la **librería** `keywords`, en la siguiente celda **importamos** esa librería y le pedimos a Python que nos muestre una **lista** con las palabras que no se pueden usar. 
# 
# Después entramos en más detalle con los conceptos resaltados en esta nota: 
# 
# * Librería
# * Importar
# * Lista
# 
# :::

# In[7]:


import keyword
print(f'Hay un total de {len(keyword.kwlist)} palabras reservadas: ')
keyword.kwlist


# :::{important} Reglas de Creación de Variables:
# 
# Para crear variables se den seguir algunas reglas elementales y tener en cuenta unas distinciones, basta con seguir las siguientes reglas:
# 
# * El nombre de una variable **debe comenzar** con una letra ó con _ .
# 
# * El nombre de una variable **no puede comenzar con un número**.
# 
# * El nombre de una variable **sólo puede contener** carácteres alfa-numéricos.
# 
# * El nombre de una variable tiene **sensibilidad** a **mayúsculas** y **minúsculas** (x es diferente de X).
# :::

# **Ejemplo**
# 
# Hagamos un código que le diga al computador que imprima los textos **Tengo** *my_age* **años**, donde *my_age* es una variable que tenga asignada una edad.

# In[8]:


my_age=25
print("Tengo",my_age, "años")


# Efectivamente, al ejecutar el script se remplaza `my_age` por el número 25. Veamos un eujemplo un poco más complicado:

# **Ejemplo**
# 
# El siguiente código calcula la longitud del nombre y la presenta en un texto. Observe que en el comando `print()` , `sep=` es un parámetro que separa los valores ingresados dentro de la función `print`. Como se puede apreciar, usamos una nueva función `len()` ¿Puedes deducir qué hace?

# In[9]:


Nombre='Su_nombre'# cambiar 'Su_nombre' por su verdadero nombre
longitud=len(Nombre)
print(Nombre," tiene una longitud de ",longitud, "caractéres", sep=" ")


# ### Múltiples Asignaciones:
# 
# Es posible asignar valores a diferentes variables en una línea de código:

# In[10]:


# Asignación múltiple

w, x, y, z = "Manzana", "Sandía", "Uva", 28;

print(w);
print(x);
print(y);
print(z);
print(w,x,y,z,sep=", ");


# También es posible asignar un **mismo valor** a diferentes variables:

# In[11]:


# Asignación múltiple del mismo valor

x1 = x2 = x3 = 0.5;
print('x1 =',x1);
print('x2 =',x2);
print('x3 =',x3);


# Cuidado con las variables no asignadas. Generan error:

# In[12]:


n # Variable sin asignar


# :::::{important} **Errores en Python**
# 
# Python resulta ser un programa bastante amable con el programador, es muy específico con los problemas que tiene y permite resolver errores de manera muy sencilla. El mensaje de error hace referencia a una excepción, pues tenemos una sintáxis correcta, pero para Python es imposible ejecutar. 
# 
# ````Python
# ---------------------------------------------------------------------------
# NameError                                 Traceback (most recent call last)
# /tmp/ipykernel_4603/2966927032.py in <module>
# ----> 1 n # Variable sin asignar
# 
# NameError: name 'n' is not defined
# ````
# El intérprete reproduce la línea responsable del error y muestra una pequeña “flecha” que apunta al lugar donde se detectó el error. El error ha sido provocado (o al menos detectado) en el elemento que precede a la flecha: en el ejemplo, el error se detecta en la línea 1 puesto que se llama a `n`, una variable sin asignar. También se muestran: el número de línea para que sepas dónde corregir y en la última línea se indica el tipo de error cometido. En este caso, como se comentó anteriormente, es una excepción provocada porque no hay una asignación previa a la variable `n`.
# 
# 
# :::::
# 
# ````{tabbed}  Errores de sintaxis
# 
# :::{admonition} Mala interpretación
# :class: tip
# Son errores provocados por el uso incorrecto del lenguaje Python, por ejemplo en el siguiente el error ocurre porque pedimos imprimir dos variables y no usamos la coma para separar:
# ```Python
#   File "/tmp/ipykernel_4603/2779427628.py", line 1
#     print(Nombre longitud)
#                  ^
# SyntaxError: invalid syntax
# ```
# 
# :::
# ````
# 
# ````{tabbed} Excepciones
# ```{admonition} Problemas en la ejecución
# :class: tip
# Como se explico arriba, hace referencia a un problema corregible siempre y cuando se arreglen los problemas de ejecución, veremos que con `try`se podrían ignorar. De ese tipo tenemos:
# 
# * ZeroDivisionError
# * NameError
# * TypeError
# * NotImplementedError
# * [Entre otras](https://docs.python.org/es/3/library/exceptions.html#concrete-exceptions)
# ```
# 
# ````

# **Ejemplo**
# 
# Vamos a empezar a hacer operaciones con variables, en este caso usaremos el operador `+`. Es claro que Python es tan sencillo e intutivo, que sumar diferentes variables indicará una suma, sin embargo, aquí dependemos del tipo de dato que se guarda en la variable; cuando las variables son numéricas, se **suman matemáticamente** y cuando es texto se **concatenan**.

# In[10]:


# Sumar dos textos

x = "Python is ";
y = "awesome";
z =  x + y;
print(z);

# Sumar dos números

n1 = 1;
n2 = 5;
suma = n1 +n2;
print(suma);

# Escribir texto y números

print(x+"the number",n1);


# ## Tipos de datos
# 
# Los ejemplos anteriores permitieron que interactuara por primera vez con Python, no obstante, las operaciones aritméticas difieren del programa hola_mundo que inicio nuestra travesía programática. Uno de los primeros aspectos son el tipo de dato que se usó, por el lado de hola mundo es una cadena de caractéres, que nosotros conocemos como texto y por el lado de las operaciones números enteros y textos también, antes de iniciar un enredo en la cabeza hablemos de los tipós de datos que admite Python y evitemos aumentar nuestra confusión. 
# 
# :::{note}
# En ocasiones se definen objetos a partir de paquetes y/o módulos que se entenderan como datos en Python. Evidentemente hoy trabajaremos con los que se tienen por defecto, sin embargo, cada vez que se importa una librería habran nuevos tipos de datos.
# :::
# 
# 
# 

# ### Enteros
# 
# Hace referencia a los valores numéricos, positivos o negativos, que no tienen coma decimal. Como cuando estabamos en secundaria, trabajamos aquí con valores que no admiten partes y que se utilizan en un sin fin de operaciones matemáticas. En la siguiente línea definimos un par de variables enteras, usamos la función `type()`para identificar el tipo de dato con el que lidiamos y calculamos una suma, una resta, una multiplicación y una división:

# In[12]:


n1=5
n2=3

print(n1, 'es',type(n1))
print(n2, 'es',type(n2))


# In[13]:


suma=n1+n2
print(suma, 'es',type(suma))


# In[14]:


resta=n2-n1
print(resta, 'es',type(resta))


# In[15]:


mult=n1*n2
print(mult, 'es',type(mult))


# **Otros operadores aritméticos**
# 
# Antes de empezar a dividir, vale la pena hacer mención a un par de operaciones aritméticas que no se han mencionado: la división entera `//` y el cálculo de residuo `%`. Corresponde a la división que usamos en nuestra infancia en el que cada número entero se descomponía en un cociente por un divisor más un residuo.
# 
# Por ejemplo, si dividimos de forma entera a 20 entre 6, el cociente es 3 y su residuo es 2:
# 
# $$
# 20=6\times 3+2
# $$
# 
# La forma de calcular ese cociente es utilizando la división entera (`//`) y la forma de calcular el residuo es utilizando el operador módulo (`%`)
# 
# 

# In[36]:


20//6


# In[37]:


20%6


# De forma, más general:

# In[39]:


n=20
d=6

print(n,'=',n//d,'*',d,'+',n%d)
print(n//d, 'es',type(n//d))
print(n%d, 'es',type(n%d))


# ### Coma flotante
# 
# Hasta ahora se puede ver que todos nuestros cálculos generan enteros, eso es porque al calcular el tipo de dato aparece `<class 'int'>`, *int* proviene de *integer* que es entero en inglés. Sin embargo,  es bien sabido por la comunidad de estudiantes que al momento de dividir es posible que aparezcan decimales, ese tipo de dato debe cambiar:
# 
# 

# In[16]:


divi=n1/n2
print(divi, 'es',type(divi))


# El anterior ejemplo hace referencia a la notación de coma flotante usada en los computadores para representar los números reales. Utiliza la idea detras de la notación científica guardando las cifras significativas del número y el exponente que indica la posición de la coma decimal. Los números en Python que contengan una parte decimal se convierten en número representados en coma flotante, en ingles `float`.

# In[19]:


n1=5.3
n2=8.0
print(n1, 'es',type(n1))
print(n2, 'es',type(n2))


# Conceptualmente 8.0 es un número entero, pero incluir el punto exige que python ubique la como, por eso se convierte en un número flotante.

# ### Boleanos
# 
# Otro tipo de datos utilizado ampliamente en Python, y muchas veces sin que el programador se entere, es el dato booleano. Simplemente indica dos valores `True` (Verdadero) o `False`(Falso). Este tipo de información será bastante útil en algunas estructuras de programación elemental, además se puede entender como la presencia/ausencia de una característica medida en el programa. Su definición es simple, pero se puede ayudar por preguntas que le podemos hacer a python a partir de operadores de comparación o operadores lógicos, similares a los operadores aritméticos pero cuya respuesta es `True`o `False`.

# In[20]:


x=True
print(x,'es',type(x))


# In[21]:


y=False
print(y,'es',type(y))


# **Operadores de comparación:**
# 
# Python es capaz de comparar información, utiliza los operadores habituales que me permiten hacer comparaciones aritméticas: la igualdad (`==`), la diferencia (`!=`), mayor que (`>`), menor que (`<`), mayor o igual que (`>=`) y ,enor o igual que (`<=`).

# In[22]:


4==3 # Preguntamos si 4 es igual a 3


# Podemos guardarlo en una variable, se recomienda usar paréntesis:

# In[24]:


x=(4==3)
print(x,'es',type(x))


# In[25]:


3!=5 #Preguntamos si 3 es diferente de 5


# In[27]:


3<5  #Preguntamos si 3 es menor que 5


# **Operadores lógicos**
# 
# Así como pudimos comparar datos, podemos armar expresiones lógicas complejas formandolas con operadores booleanos. Entre los más conocidos tenemos:
# 
# **Conjunción (AND)**
# 
# Verdadera si ambas sentencias lógicas son verdaderas, en otro caso falsa:

# In[29]:


(4!=3) and (5==5) 


# In[30]:


(4!=4) and (5==5) 


# **Disyunción (OR)**
# 
# Falsa si ambas sentencias lógicas son falsas, en otro caso verdadero:

# In[31]:


(4!=4) or (5==5) 


# In[33]:


(4!=4) or (5!=5) 


# **Negación (NOT)**
# 
# Cambia el valor de la variable booleana:

# In[34]:


not (4==4)


# In[35]:


not (4!=4)


# ### Textos (Strings)
# 
# Los textos son expresiones que representan una cadena de caracteres, utiles para escribir mensajes y combinarlos con valores que generemos en nuestros procesamientos. Para guardar un texto en Python usamos comillas simples: `'...'` o comillas dobles: `"..."`. Es posible utilizar dos tipos de comillas, puesto que en algunas ocasiones la comilla es necesaria para el texto:  

# Usemos los diferentes tipos de comillas para generar texto:

# In[ ]:


a='Texto simple escrito entre comillas simples'
print(a)
a


# In[ ]:


b='Texto simple escrito entre comillas dobles'
print(b)
b


# In[40]:


c='Texto simple escrito entre comillas simples que necesita "adentrico" comillas dobles'
print(c)
c


# In[41]:


d="Texto simple escrito entre comillas dobles que necesita 'adentrico' comillas simples"
print(d)
d


# :::{note}
# No hay diferencia en guardar un texto en comillas simples o dobles. No obstante, para Python un texto que contenga comillas simples es diferente a un texto que contenga comillas dobles.
# :::

# In[43]:


text1="Primer texto"
text2= 'Primer texto'
print(text1==text2)


# In[44]:


text1="'Primer' texto"
text2= '"Primer" texto'
print(text1==text2)


# Como vimos, la función print es la que nos permite imprimir estos mensajes. El texto \n indica una nueva linea en el texto:

# In[ ]:


print("Una línea\notra línea")


# No obstante, a veces necesitamos escribir  \n en un mensaje:

# In[ ]:


print('La ruta del archivo es C:\nombres\archivo.ipynb')


# En este caso la aparición de \ daño el mensaje, para resolver el problema escribimos r antes:

# In[ ]:


print(r'La ruta del archivo es C:\nombres\archivo.ipynb')


# Podemos recorrer los caractéres de la cadena de texto de la siguiente forma:
# 
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 25.00%; padding-top: 0; height: 0;"><iframe frameborder="0" width="800" height="200" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/618a7952e627160d7b52aba1" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>
# 

# En el ejemplo utilizamos el texto `'Hola mundo'` y el número arriba indica la posición o índice de cada caracter:

# In[47]:


texto='Hola mundo'
print(texto)


# Cada número arriba indica la posición, accedemos a esa posición llamando a la variable y con paréntesis cuadrados indicamos el acceso al valor indicado:

# In[48]:


texto[0]


# In[49]:


texto[4]


# In[50]:


texto[9]


# Podemos tomar un subtexto, en Python los rangos se simbolizan con dos puntos y toman desde el índice indicado en el inicio hasta el índice anterior al final.

# In[51]:


texto[0:5]


# Note que el anterior mostro el subtexto que contiene los valores con indice [0], [1], [2], [3] y  [4]. El carcater [5] no apareció.

# In[52]:


texto[5:9]


# claramente el tipo de dato cambia, en python hace referencia a `str` que indica que es una cade de caractéres, `String`.

# In[57]:


print(texto,'es',type(texto))


# ### Repaso
# 
# Como vimos anteriormente, en Python la asignación de valores a variables se hace con el operador `=`, a la variable de la izquierda le asignamos el valor de la derecha.
# 
# :::{admonition} Tip
# :class: tip 
# En pro de hacer amena la lectura del código, es recomendable asignar nombres relacionados con el problema que se está programando. En el ejemplo siguiente se calcula el área de un triángulo. Esplique las diferencias entre los dos códigos.
# :::

# **Código 1**

# In[14]:


base = 1
altura = 2
area = base*altura


# **Código 2**

# In[15]:


a = 1
b = 2
c = a*b


# 
# :::{note}
# Los dos códigos anteriores para Python son iguales, pero para el lector es más fácil identificar el error en el primero que en el segundo, por ello, es mejor utilizar el primer código que el segundo.
# :::
# 

# :::{admonition} Recordemos ...
# Las variables no pueden tener algunos nombres, que son palabras reservadas por Python, estas palabras son:
# *and, as, assert, break, class, continue, def, del, elif, else, except,
# False, finally, for, from, global, if, import, in, is, lambda, nonlocal, None, not, or,
# pass, raise, return, True, try, while, with* y *yield*.
# :::

# :::{admonition} Tip
# :class: tip 
# Si deseamos hacer mucho más fácil la lectura del código, podemos agregar comentarios, los cuales van antecedidos de `#`, es decir, 
# :::
# 

# In[53]:


base = 1 #Base del triángulo
altura = 2 #Altura del triángulo
area = base*altura/2 #Cálculo del área de un triángulo


# Si deseamos definir múltiples variables, aprovechamos las ventajas de Python para este hecho, por ejemplo:

# In[54]:


base, altura= 1,2 #Base y altura del triángulo
area = base*altura/2 #Cálculo del área de un triángulo


# :::{admonition} Recordemos ...
# :class: tip
# Condiciones que deben cumplir los nombres de las variables:
# * El nombre de una variable debe comenzar con una letra ó con _ .
# * El nombre de una variable no puede comenzar con un número.
# * El nombre de una variable sólo puede contener carácteres alfa-numéricos.
# * El nombre de una variable tiene sensibilidad a mayúsculas y minúsculas (x es diferente de X).
# :::

# 
# **Textos**
# 
# Recordemos que un tipo de variables muy utilizadas son las que contienen texto en ellas, como por ejemplo:

# In[18]:


z = "Hola mundo" #El texto también puede ir entre comillas sencillas, así: z = 'Hola mundo'


# Para imprimir los valores de diferentes variables, utilizamos el comando `print`

# In[19]:


print(z)


# In[20]:


print(a,z)


# In[21]:


print(a,z,area)


# In[22]:


print('El valor de a es:',a) #Nota que la separación entre los elementos es un espacio


# In[23]:


print(a,z,area,sep='\n') #Con esta opción podemos nodificar la separación


# Sobre las variables tipo `str`, podemos aplicar la función `len` para medir la cantidad de caracteres que hay en la variable:

# In[24]:


len(z) #El espacio cuenta como un caracter


# In[25]:


w = 'hoy es un gran día'


# Las variables tipo `str` se pueden operar:

# In[26]:


print(z+w)


# In[27]:


print(z+' '+w)


# In[28]:


print(3*z)


# Si deseamos escribir comillas en una variable tipo `str`, debemos definir la variable con comillas dobles y las comillas que deseamos deben ser sencillas, o viceversa. De manera más general, podemos definir la variable con comillas triples:

# In[29]:


z1 = "Así ponemos comillas 'sencillas'"
z2 = 'Así ponemos comillas "dobles"'
z3 = ''' Y así 'podemos' usar cualquier tipo de "comillas"'''
print(z1,z2,z3)


# :::{admonition} Tip
# :class: tip 
# Si tenemos una variable tipo `str` la cual queremos volver una variable de tipo numérico, en caso que su contenido lo permita, tenemos las siguientes funciones:
# :::
# 

# In[55]:


n = '2'


# In[56]:


print('El tipo de n es:',type(n),
      'Si lo queremos volver entero:',int(n),type(int(n)),
      'Si lo queremos volver float:',float(n),type(float(n)),sep='\n')
#Nota que podemos separar las entradas de la función con un salto de línea, para hacer más fácil la lectura o para no perder valores de vista como pasa con este comentario


# **Entrada de texto a la máquina:**
# 
# En muchas oportunidades es de gran utilidad establecer líneas de interacción entre el usuario y la máquina, de tal forma, que el usuario pueda ingresar información a medida que se ejecuta cierto código, para ello tenemos a nuestra disposición la función `input`:
# 
# 

# In[58]:


input('texto que aparece, aclarando la entrada que se pretende modificar: ')


# Como podemos ver, el retorno de la función `input`, es una cadena de caracteres, por lo tanto, si deseamos transformar tales valores debemos utilizar las funciones que mencionamos anteriormente `int` y/o `float`.

# ### Ejercicio
# 
# Ingresar el salario desado:

# In[60]:


salario = float(input(
    'Ingresa el valor del salario que te gustaría ganar cuando termines el pregrado (en pesos sin puntos ni comas): '))


# Muchas veces, a la hora de mostrar los valores que hemos guardado, debemos darles formato, para ello podemos tener en cuenta las siguientes opciones de la función `print`:

# In[64]:


print("El salario al que aspiras es:", salario)
print("Pero se vería mejor con la separación en miles: ${0:8,f}".format(salario))


# `{0:8,f}` En el código anterior0 indica la posición del elemento que imprimiremos, el 8 la cantidad de espacios para reservar e imprimir el  número pero no afectará ya que no tenemos ningún tipo de alineación la `,` indica la separación por miles y por último `f` indica que se imprimirá un float.

# Cambia `{0:8,f}` por ` ${0:,2f}`y comenta los resultados. 

# Podemos prescindir del punto decimal:

# In[65]:


print("Si no queremos el punto decimal: {0:7,d}".format(int(salario)))


# `d` indica que lo que se imprime es un entero (`int`).

# También podemos usar notación científica, en este caso usamos `e`. La `e` indica que se usará notación científica para el resultado, 1 es la cantidad de números antes de la coma y 2 la cantidad de números después de la coma.

# In[68]:


print("O tal vez, sea mejor la notación científica: {0:1.2e}".format(int(salario)))


# Si tenemos diferentes salidas a las cuales darles formato, podemos hacer algo como lo que viene a continuación

# In[69]:


print('Salario mensual: {0:1,d} Salario anual {1:2.2e} '.format(int(salario),salario*12))
#Nota que el 0 es para el salario y el 1 para el salario multiplicado por 12


# ## Cierre
# 
# Hemos empezado a trabajar con Python guardando variables en diferentes tipos de datos. Aunque aún no estamos aplicando procesos muy complicados ya vemos como poco a poco aplicamos una secuencia estructurada de pasos para resolver algunos problemas. Por ejemplo, aunque no fue mencionado, se espera que como estudiante de Python se de cuenta de uqe las variables deben ser asignadas antes de usarse y que para asignarse debe ser ejecutada una celda donde se defina la variables. Así mismo, se espera que reconozca el orden de ejecución, la jerarquía de las operaciones y la importancia de usar paréntesis. 
# 
# En el próximo módulo se empezará a trabajar con estructuras de programación, se estudiaran algunos métodos útiles para la manipulación de texto y se representarán como debe ser algunos algoritmos.
