#!/usr/bin/env python
# coding: utf-8

# # Variables y funciones básicas

# Inicio
# Los objetos son los elementos principales que manipulan los programas de Python. Cada objeto tiene definido su tipo y esto permite saber las cosas que los programas pueden hacer con dicho objeto.
# 
# Los tipos son escalares o no escalares. Los objetos escalares son los elementos indivisibles, mientras que, los objetos no escalares, son aquellos con estructura interna.
# 
# Los objetos escalares en Python son los siguientes:
# * **int:** Son los objetos empleados para representar números enteros, por ejemplo, $-30, 0, 1500$.
# * **float:** Objetos que representan números reales. Este tipo de número siempre presenta el punto decimal (así sean números enteros, al $3$ lo representa como $3.0$). También permite emplear la notación científica.
# * **bool:** Se usan para representar los valores de verdad Booleanos, verdadero (`True`) y falso (`False`).
# * **None:** Es un tipo empleado para algunos elementos vacíós, como el retorno de una función.
# 
# **Operador de asignación:** Para asignar un determinado valor a una variable, emplearemos el operador `=`, así:

# In[1]:


x = 1


# En la celda anterior, hemos asignado el valor $1$ a la variable $x$, así que cuando llamemos a tal variable en el futuro, ésta representará el valor indicado. Si deseamos ver el tipo de objeto que hemos almacenado, empleamos la función `type`, así:

# In[2]:


type(x)


# Como vemos, dicha variable es del tipo `int`. Si a $x$ le sumamos `1.6E3`, lo que equivale a $1.6\times10^3$ (y es tipo `float`), obtenemos un elemento `float`

# In[3]:


type(x+1.6E3)


# **Operadores:**
# 
# $x+y$ es la suma de $x$ y $y$. Si ambos números son tipo `int`, el resultado es `int`. Si alguno de los números es tipo `float`, el resultado es tipo `float`.
# 
# $x-y$ es la resta de $x$ y $y$, y los tipos de resultados son iguales a los de la suma.
# 
# $x*y$ es el producto de $x$ y $y$, y los tipos de resultados son iguales a los de la suma.
# 
# $x//y$ regresa la parte entera de la división entre $x$ y $y$, el tipo es `int`.
# 
# $x\%y$ regresa el residuo de dividir $x$ entre $y$, y el tipo es `int`.
# 
# $x**y$ obtenemos el resultado de $x$ elevado a la $y$, el tipo de resultado es igual al de la suma.
# 
# Las operaciones en Python respetan la jerarquía conocida en matemáticas.  
# 
# **Operadores de comparación:**
# 
# En Python tenemos diferentes operadores para comparar elementos, por ejemplo, el de igualdad es:  `==`. El de "no igualdad" es `!=`, mientras que, las desigualdades las notamos con: `>` (mayor que), `<` (menor que), `>=` (mayor o igual), `>=` (menor o igual).
# 
# **Operadores lógicos:**
# 
# $x\ and\ y$ es `True` si tanto $x$ como $y$ son `True`.
# 
# $x\ or\ y$ es `True` si al menos una variable es `True`.
# 
# $not\ x$ cambia el valor de verdad de la variabe.

# In[4]:


5//3


# In[5]:


5%3


# In[6]:


5**3


# In[7]:


5==3


# In[8]:


5!=3


# In[9]:


5>3


# In[10]:


5<3


# In[11]:


5!=3 and 5<3


# In[12]:


5!=3 or 5<3


# In[13]:


not 5<3


# **Variables:**
# 
# Como vimos antes, en Python la asignación de valores a variables se hace con el operador `=`, a la variable de la izquierda le asignamos el valor de la derecha.
# 
# Y en pro de hacer amena la lectura del código, es recomendable asignar nombres relacionados con el problema que se está programando, por ejemplo, para calcular el área de un triángulo:

# In[14]:


base = 1
altura = 2
area = base*altura


# In[15]:


a = 1
b = 2
c = a*b


# Los dos códigos anteriores para Python son iguales, pero para el lector es más fácil identificar el error en el primero que en el segundo, por ello, es mejor utilizar el primer código que el segundo.
# 
# Las variables no pueden tener algunos nombres, que son palabras reservadas por Python, estas palabras son:
# *and, as, assert, break, class, continue, def, del, elif, else, except,
# False, finally, for, from, global, if, import, in, is, lambda, nonlocal, None, not, or,
# pass, raise, return, True, try, while, with* y *yield*.
# 
# Pero si deseamos hacer mucho más fácil la lectura del código, podemos agregar comentarios, los cuales van antecedidos de `#`, es decir, 

# In[16]:


base = 1 #Base del triángulo
altura = 2 #Altura del triángulo
area = base*altura/2 #Cálculo del área de un triángulo


# Si deseamos definir múltiples variables, aprovechamos las ventajas de Python para este hecho, por ejemplo:

# In[17]:


base, altura= 1,2 #Base y altura del triángulo
area = base*altura/2 #Cálculo del área de un triángulo


# Otras condiciones que deben cumplir los nombres de las variables:
# * El nombre de una variable debe comenzar con una letra ó con _ .
# * El nombre de una variable no puede comenzar con un número.
# * El nombre de una variable sólo puede contener carácteres alfa-numéricos.
# * El nombre de una variable tiene sensibilidad a mayúsculas y minúsculas (x es diferente de X).
# 
# **Variables tipo string:**
# 
# Otro tipo de variables muy utilizadas son las que contienen texto en ellas, como por ejemplo:

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


# Si tenemos una variable tipo `str` la cual queremos volver una variable de tipo numérico, en caso que su contenido lo permita, tenemos las siguientes funciones:

# In[30]:


n = '2'


# In[31]:


print('El tipo de n es:',type(n),
      'Si lo queremos volver entero:',int(n),type(int(n)),
      'Si lo queremos volver float:',float(n),type(float(n)),sep='\n')
#Nota que podemos separar las entradas de la función con un salto de línea, para hacer más fácil la lectura o para no perder valores de vista como pasa con este comentario


# **Entrada de texto a la máquina:**
# 
# En muchas oportunidades es de gran utilidad establecer líneas de interacción entre el usuario y la máquina, de tal forma, que el usuario pueda ingresar información a medida que se ejecuta cierto código, para ello tenemos a nuestra disposición la función `input`

# In[32]:


input('texto que aparece, aclarando la entrada que se pretende modificar: ')


# Como podemos ver, el retorno de la función `input`, es una cadena de caracteres, por lo tanto, si deseamos transformar tales valores debemos utilizar las funciones que mencionamos anteriormente `int` y/o `float`.

# In[33]:


salario = float(input(
    'Ingresa el valor del salario que te gustaría ganar cuando termines el pregrado (en pesos sin puntos ni comas): '))


# Muchas veces, a la hora de mostrar los valores que hemos guardado, debemos darles formato, para ello podemos tener en cuenta las siguientes opciones de la función `print`:

# In[34]:


print("El salario al que aspiras es:", salario)
print("Pero se vería mejor con la separación en miles: {0:8,f}".format(salario))
#{0:7,f} El 0 indica la posición del elemento que imprimiremos, el 8 la cantidad de espacios para reservar e imprimir el 
#número pero no afectará ya que no tenemos ningún tipo de alineación
#la , indica la separación por miles y por último f indica que se imprimirá un float
print("Si no queremos el punto decimal: {0:7,d}".format(int(salario)))
#la d indica que lo que se imprime es un int
print("O tal vez, sea mejor la notación científica: {0:1.2e}".format(int(salario)))
#La e indica que se usará notación científica para el resultado,
#1 es la cantidad de números antes de la coma y 2 la cantidad de números después de la coma


# Si tenemos diferentes salidas a las cuales darles formato, podemos hacer algo como lo que viene a continuación

# In[35]:


print('Salario mensual: {0:1,d} Salario anual {1:2.2e} '.format(int(salario),salario*12))
#Nota que el 0 es para el salario y el 1 para el salario multiplicado por 12


# In[ ]:




