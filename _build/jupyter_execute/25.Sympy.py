#!/usr/bin/env python
# coding: utf-8

# # Computación simbólica con Sympy

# :::::{important} Para tener presente
# 
# 
# El paquete `sympy` nos brinda la posibilidad de usar expresiones aproximadas de manera simbólica privilegiando el símbolo frente a la evaluación. 
# 
# ````{tabbed} ¿Para qué?
# 
# :::{admonition} Importante
# :class: tip
# Para realizar cálculo simbólico y así apoyar el proceso de enseñanza-aprendizaje de las matemáticas y además solucionar algunos percances computacionales.
# :::
# ````
# 
# ````{tabbed} ¿Tiene documentación?
# 
# :::{admonition} Por supuesto:
# :class: tip 
# En la página del paquete [`Sympy`](https://docs.sympy.org/latest/index.html) podemos encontrar toda la información relevante.
# :::
# ````
# 
# :::::

# ## Computación simbólica
# 
# Hasta el momento hemos trabajado con varios elementos matemáticos que en ocasiones se toman de manera aproximada, por ejemplo, la raíz cuadrada de un número entero. Aunque hay algunos números cuya raíz es entera la mayoría tiene raices cuadradas irracionales y la máquina nos ofrece apenas una aproximación a esos valores. 

# In[1]:


import numpy as np
np.sqrt(8)


# In[2]:


np.sqrt(8)*np.sqrt(8)


# In[3]:


import sympy
sympy.sqrt(8)


# In[4]:


sympy.sqrt(8)*sympy.sqrt(8)


# ```
# Nota: para obtener una salida estética de sympy usamos la orden:
# 
# from sympy import init_printing
# 
# init_printing() 
# 
# ```

# **El poder de la computación simbólica**
# 
# El poder real de un sistema de cálculo simbólico como **SymPy** es la capacidad de hacer todo tipo de cálculos simbólicamente. SymPy puede simplificar expresiones, calcular derivadas, integrales y límites, resolver ecuaciones, trabajar con matrices y mucho, mucho más, y hacerlo todo simbólicamente. Incluye módulos para trazar, imprimir (como salida impresa en 2D de fórmulas matemáticas, LATEX), generación de código, física, estadística, combinatoria, teoría de números, geometría, lógica y más. 
# 
# *Tomado de* [https://docs.sympy.org/latest/tutorial/intro.html](https://docs.sympy.org/latest/tutorial/intro.html)

# ## Conceptos básicos
# 
# Para iniciar el trabajo con la librería sympy debemos aclarar rutinas que son fundamentales para iniciar cualquier trabajo con este paquete. En primer lugar, por ejemplo, hay que aclarar que vamos a usar un símbolo así mismo, las ecuaciones tienen que poder expresarse y no podemos usar ni `=` ni  `==`. Veamos algunos de estos conceptos básicos.
# 
# 

# ### Símbolos
# 
# Para usar variables simbólicas debemos definirlas, usamos la función symbols:

# In[5]:


import sympy as sp


# In[6]:


x = sp.symbols("x")


# In[7]:


x


# Notemos que las operaciones las realiza de manera análoga a lo que solemos hacer con lápiz y papel:

# In[10]:


(x+1)**2


# In[8]:


sp.expand((x+1)**2)


# In[9]:


(3*x-5)*(2*x+7)-x


# In[17]:


x+2*x-8+5*x+7


# In[11]:


comoescribo = sp.symbols("comoveo")
comoescribo+8 


# ### Sustitución
# 
# Para remplazar valores en una expresión usamos `subs`

# In[12]:


expr = (3*x-5)*(2*x+7)-x


# In[13]:


expr


# In[14]:


expr.subs(x,1)


# In[15]:


expr.subs(x,0)


# También se pueden sustituir expresiones

# In[16]:


y=sp.symbols("y")


# In[17]:


expr = x**y


# In[18]:


expr


# In[19]:


expr = expr.subs(y, x**y)
expr


# In[20]:


from sympy import *


# In[21]:


expr = sin(2*x)
expand_trig(expr)


# In[24]:


expr.subs(sin(2*x), 2*sin(x)*cos(x)).subs(cos(2*x),2*cos(x)**2-1)


# In[25]:


z = symbols("z")
expr = x**3 + 4*x*y - z
expr


# In[32]:


expr.subs([(x, 2), (y, 4), (z, 0)])


# #### Convertir cadenas a expresiones SymPy 
# 
# Usamos sympify para convertir cadenas en expresiones:
# 

# In[26]:


str_expr = "x**2 + 3*x - 1/2"
print(str_expr)
expr = sympify(str_expr)
expr


# In[27]:


import ipywidgets as widgets
from ipywidgets import interact


# In[28]:


def modulo1(t,n):
    z="Error"
    n=sympify(n)
    try:
        t=sympify(t)
        z=sp.expand(t**n)
    except:
        print('Error!!')
    return z
widn=widgets.IntSlider(min=0,max=10,value=1)
interact(modulo1, t="sin(x)",n=widn)


# #### Obtener el valor en punto flotante
# 
# Usamos `evalf` para obtener el valor en punto flotante.

# In[29]:


expr = sqrt(8)
expr


# In[30]:


expr.evalf()


# `subs` y `evalf` son buenos si desea hacer una evaluación simple, pero si tiene la intención de evaluar una expresión en muchos puntos, hay formas más eficientes. Por ejemplo, si desea evaluar una expresión en mil puntos, usar SymPy sería mucho más lento de lo necesario, especialmente si solo le importa la precisión de la máquina. En su lugar, debe usar librerías como NumPy y SciPy .
# 
# La forma más fácil de convertir una expresión SymPy en una expresión que puede evaluarse numéricamente es usar la `lambdify`función. `lambdify` actúa como una función lambda, excepto que convierte los nombres de SymPy a los nombres de la biblioteca numérica dada, generalmente NumPy. Por ejemplo:

# In[31]:


import numpy as np
a = np.arange(10) 
a


# In[32]:


expr = sin(x)


# In[33]:


f = lambdify(x, expr, "numpy") 


# In[34]:


f(a) 


# In[35]:


f = lambdify(x, expr, "math")
f(5)


# ### Ecuaciones 
# Como sabemos `=` y `==` ya fueron usado en el lenguaje para unas operaciones específicas.
# 
# 

# In[36]:


x+1==4


# In[37]:


sp.Eq(x + 1, 4)


# ## Igualdad de expresiones y simplificación
# 
# Ahora saltemos y hagamos algunas matemáticas interesantes. Una de las características más útiles de un sistema de manipulación simbólica es la capacidad de simplificar expresiones matemáticas. 
# 
# 
# SymPy tiene docenas de funciones para realizar varios tipos de simplificación, pero hay una función general llamada `simplify()` que intenta aplicar todas estas funciones de manera inteligente para llegar a la forma más simple de una expresión. Aquí hay unos ejemplos:

# Es importante tener esta definición en cuenta cuando se presentan igualdades entre expresiones.

# In[38]:


simplify(sin(x)**2 + cos(x)**2)


# In[39]:


(x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)


# In[40]:


simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))


# In[41]:


simplify(gamma(x)/gamma(x - 2))


# In[42]:


simplify (x**2+2*x+1 - (x+1)**2)


# Un problema de `simplify()` es que puede ser innecesariamente lento, ya que intenta muchos tipos de simplificaciones antes de elegir la mejor. Si ya sabe exactamente qué tipo de simplificación está buscando, es mejor aplicar las funciones de simplificación específicas que aplican esas simplificaciones.
# 
# 

# ### Simplificación de funciones polinómicas racionales
# 
# `expand()` es una de las funciones de simplificación más comunes en SymPy. Aunque tiene muchos ámbitos, por ahora, consideraremos su función en la expansión de expresiones polinómicas. Por ejemplo:
# 
# 

# In[43]:


expand((x+2)**3)


# `factor()` toma un polinomio y lo factoriza en factores irreducibles sobre los números racionales. Por ejemplo:

# In[58]:


factor(x**3-x**2+x-1)


# In[59]:


factor_list(x**3-x**2+x-1)


# `cancel()` tomará cualquier función racional y la pondrá en la forma canónica estándar, 𝑝/𝑞, dónde 𝑝 y 𝑞 son polinomios expandidos sin factores comunes, y los coeficientes principales de 𝑝 y 𝑞 no tienen denominadores (es decir, son enteros).

# In[44]:


cancel((x**2 + 2*x + 1)/(x**2 + x))


# In[45]:


expr = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)
expr


# In[46]:


cancel(expr)


# `apart()` realiza una descomposición en fracciones parciales de una función racional.

# In[47]:


expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
expr


# In[48]:


apart(expr)


# Para simplificar expresiones usando identidades trigonométricas, es recomendable el uso de `trigsimp()`.

# In[49]:


trigsimp(sin(x)*tan(x)/sec(x))


# In[50]:


cancel(sin(x)*tan(x)/sec(x))


# Para expandir las funciones trigonométricas, es decir, aplicar la suma o las identidades de doble ángulo, usamos `expand_trig()`.

# In[51]:


expand_trig(sin(x + y))


# In[52]:


expand_trig(tan(2*x))


# `powsimp()` permite simplificaciones con leyes de exponentes.

# In[53]:


x, y = symbols('x y', positive=True)

a, b = symbols('a b', real=True)

z, t, c = symbols('z t c')


# In[54]:


powsimp(x**a*x**b)


# In[55]:


powsimp(z**t*z**c)


# Con `rewrite()` podemos reescribir algunas funciones especiales en términos de otra:

# In[56]:


tan(x).rewrite(sin)


# In[57]:


factorial(x).rewrite(gamma)


# In[58]:


exp(I*x).rewrite(sin)


# 
# **Fracciones Continuas**
# 
# Una fracción continua es una expresión de la forma:
# 
# $$a_0 + \cfrac{1}{a_1 + \cfrac{1}{a_2 + \cfrac{1}{ \ddots + \cfrac{1}{a_n}
# }}}$$
# 
# Realizar una función en sympy que admita una lista $[a_0,a_1,a_2,\cdots,a_n]$ y que retorne el valor obtenido por la fracción. 

# In[59]:


L=[1,2,3]
L.reverse()
L


# In[60]:


def lista_a_fraccion(L):
    L.reverse()
    expr=Integer(0)
    for i in L:
        expr=1/(expr+i)
    return expr


# In[61]:


lista_a_fraccion([x,y,z])


# In[62]:


lista_a_fraccion([1,2*x,3])


# ## Cálculo
# 
# SymPy también permite realizar tareas básicas del cálculo diferencial e integral. 

# In[63]:


from sympy import *
x, y, z = symbols('x y z')


# ### Derivadas

# In[64]:


diff(cos(x),x) #derivadas en una sola variable


# In[65]:


diff(exp(4*x**2+5*x),x) #derivadas en una sola variable


# In[66]:


diff(y*exp(4*x**2+5*y),x) #derivadas parciales


# In[67]:


diff(cos(x),x,x)  #derivadas de orden superior


# In[68]:


diff(cos(x),x,x,x)


# In[69]:


diff(cos(x),x,3) 


# In[70]:


diff(y*exp(4*x**2+5*y),x,y) #derivadas de orden superior


# Como en las ecuaciones, a veces requerimos derivadas expresadas, sin evaluarse:

# In[71]:


deriv = Derivative( exp (x * y * z), x, y, y, z)
deriv


# Para evaluarla:

# In[72]:


deriv.doit()


# In[73]:


diff( exp (x * y * z), x, y, y, z)


# ### Integrales

# In[74]:


integrate(cos(x),x) # Integrales


# In[75]:


integrate(exp (-x), (x, 0, oo))


# In[76]:


Integral(exp (-x), (x, 0, oo))


# In[77]:


Integral(exp (-x), (x, 0, oo)).doit()


# In[78]:


integrate(x**2, (x, 0,1))


# In[79]:


Integral(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))


# In[80]:


integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))


# In[81]:


Integral(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)).doit()


# Y ¿si la integral no es posible de calcular?

# In[82]:


integrate(x**x, x)


# Para expresar una integral no evaluada usamos `Integral`:

# In[83]:


integ = Integral((x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x -exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1)), x)
integ


# In[84]:


integ.doit()


# ### Límites

# In[85]:


limit(sin(x)/x, x, 0) #Límites


# In[86]:


expr = sin(x)/x
expr.subs(x, 0)


# In[87]:


limit(expr, x, 0)


# In[88]:


expr = Limit((cos(x) - 1)/x, x, 0,"-") #Límites sin evaluar
expr


# In[89]:


expr.doit()


# In[90]:


expr = exp(sin(x)) 
expr.series(x,0, 10)  # Series


# In[91]:


exp(x - 6).series(x, 6,10) # Series no centradas en 0


# ## Solucionar ecuaciones
# 
# Ahora hagamos una rápida exploración por las diferentes ecuaciones que se resuelven en Sympy.

# In[92]:


Eq(x**2,1)


# In[93]:


solveset(Eq(x**2,1),x)


# In[94]:


solveset(Eq(x**2,1),x)[0]


# In[95]:


list(solveset(Eq(x**2,1),x))[0]


# In[96]:


solveset(x ** 2 - x, x) # Raices


# In[97]:


solveset(x - x, x)


# In[98]:


solveset(x - x, x,domain=sp.Integers)


# In[99]:


solveset(x - x, x,domain=Interval(0,10))


# In[100]:


solveset(x - x, x,domain=Interval.Ropen(0,10))


# In[101]:


solveset(x - x, x,domain=Interval.Lopen(0,10))


# In[102]:


solveset(x - x, x,domain=Interval.open(0,10))


# In[103]:


solveset(x - x, x,domain=FiniteSet(0,1,2,3))


# In[104]:


solveset(sin(x) - 1, x, domain=sp.Reals)


# In[105]:


solveset(sin(x) - 1, x, domain=Interval.open(5,34))


# In[106]:


solveset(exp(x), x)     # Cuando la solución no existe


# In[107]:


solveset(cos(x) - x, x)  # Cuando es incapaz de encontrar una solución


# ### Sistemas de ecuaciones lineales
# 
# Usamos `linsolve` para encontrar las soluciones:

# In[108]:


linsolve([x + y + z - 1, x + y + 2*z - 3 ], (x, y, z))


# In[109]:


linsolve([x + y + z - 1, x - y + z - 3,x+y+1 ], (x, y, z))


# In[110]:


linsolve([x + y + z - 1, x + y + z - 3,x+y+1 ], (x, y, z))


# ### Sistemas no lineales
# 
# Usaremos `nonlinsolve`

# In[111]:


a, b, c, d = symbols('a, b, c, d', real=True)


# In[112]:


nonlinsolve([a**2 + a, a - b], [a, b])


# In[113]:


nonlinsolve([x*y - 1, x - 2], x, y)

