#!/usr/bin/env python
# coding: utf-8

# <h1>Computación simbólica con Sympy<span class="tocSkip"></span></h1>
# <div class="toc"><ul class="toc-item"><li><span><a href="#Computación-simbólica" data-toc-modified-id="Computación-simbólica-1"><span class="toc-item-num">1&nbsp;&nbsp;</span>Computación simbólica</a></span></li><li><span><a href="#Conceptos-básicos" data-toc-modified-id="Conceptos-básicos-2"><span class="toc-item-num">2&nbsp;&nbsp;</span>Conceptos básicos</a></span><ul class="toc-item"><li><span><a href="#Símbolos" data-toc-modified-id="Símbolos-2.1"><span class="toc-item-num">2.1&nbsp;&nbsp;</span>Símbolos</a></span></li><li><span><a href="#Sustitución" data-toc-modified-id="Sustitución-2.2"><span class="toc-item-num">2.2&nbsp;&nbsp;</span>Sustitución</a></span><ul class="toc-item"><li><span><a href="#Convertir-cadenas-a-expresiones-SymPy" data-toc-modified-id="Convertir-cadenas-a-expresiones-SymPy-2.2.1"><span class="toc-item-num">2.2.1&nbsp;&nbsp;</span>Convertir cadenas a expresiones SymPy</a></span></li><li><span><a href="#Obtener-el-valor-en-punto-flotante" data-toc-modified-id="Obtener-el-valor-en-punto-flotante-2.2.2"><span class="toc-item-num">2.2.2&nbsp;&nbsp;</span>Obtener el valor en punto flotante</a></span></li></ul></li><li><span><a href="#Ecuaciones" data-toc-modified-id="Ecuaciones-2.3"><span class="toc-item-num">2.3&nbsp;&nbsp;</span>Ecuaciones</a></span></li></ul></li><li><span><a href="#Igualdad-de-expresiones-y-simplificación" data-toc-modified-id="Igualdad-de-expresiones-y-simplificación-3"><span class="toc-item-num">3&nbsp;&nbsp;</span>Igualdad de expresiones y simplificación</a></span><ul class="toc-item"><li><span><a href="#Simplificación-de-funciones-polinómicas-racionales" data-toc-modified-id="Simplificación-de-funciones-polinómicas-racionales-3.1"><span class="toc-item-num">3.1&nbsp;&nbsp;</span>Simplificación de funciones polinómicas racionales</a></span></li></ul></li><li><span><a href="#Cálculo" data-toc-modified-id="Cálculo-4"><span class="toc-item-num">4&nbsp;&nbsp;</span>Cálculo</a></span></li><li><span><a href="#Solucionar-ecuaciones" data-toc-modified-id="Solucionar-ecuaciones-5"><span class="toc-item-num">5&nbsp;&nbsp;</span>Solucionar ecuaciones</a></span><ul class="toc-item"><li><span><a href="#Sistemas-de-ecuaciones-lineales" data-toc-modified-id="Sistemas-de-ecuaciones-lineales-5.1"><span class="toc-item-num">5.1&nbsp;&nbsp;</span>Sistemas de ecuaciones lineales</a></span></li><li><span><a href="#Sistemas-no-lineales" data-toc-modified-id="Sistemas-no-lineales-5.2"><span class="toc-item-num">5.2&nbsp;&nbsp;</span>Sistemas no lineales</a></span></li><li><span><a href="#Ecuaciones-diferenciales" data-toc-modified-id="Ecuaciones-diferenciales-5.3"><span class="toc-item-num">5.3&nbsp;&nbsp;</span>Ecuaciones diferenciales</a></span></li></ul></li></ul></div>

# ## Computación simbólica
# 
# Hasta el momento hemos trabajado con varios elementos matemáticos que en ocasiones se toman de manera aproximada, por ejemplo, la raíz cuadrada de un número entero. Aunque hay algunos números cuya raíz es entera la mayoría tiene raices cuadradas irracionales y la máquina nos ofrece apenas una aproximación a esos valores. El paquete [`Sympy`](https://docs.sympy.org/latest/index.html) nos ofrece la posibilidad de usar expresiones aproximadas de manera simbólica privilegiando el símbolo frente a la evaluación. 

# In[1]:


import numpy as np
np.sqrt(8)


# In[2]:


np.sqrt(8)*np.sqrt(8)


# In[3]:


import sympy
sympy.sqrt(8)


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
# El poder real de un sistema de cálculo simbólico como SymPy es la capacidad de hacer todo tipo de cálculos simbólicamente. SymPy puede simplificar expresiones, calcular derivadas, integrales y límites, resolver ecuaciones, trabajar con matrices y mucho, mucho más, y hacerlo todo simbólicamente. Incluye módulos para trazar, imprimir (como salida impresa en 2D de fórmulas matemáticas, LATEX), generación de código, física, estadística, combinatoria, teoría de números, geometría, lógica y más. 
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

# In[6]:


import sympy as sp


# In[11]:


x=sp.symbols("x")


# In[12]:


x


# In[15]:


sp.expand((x+1)**2)


# In[16]:


(3*x-5)*(2*x+7)-x


# In[17]:


x+2*x-8+5*x+7


# In[18]:


comoescribo=sp.symbols("comoveo")
comoescribo+8 


# ### Sustitución
# 
# Para remplazar valores en una expresión usamos `subs`

# In[19]:


expr=(3*x-5)*(2*x+7)-x


# In[20]:


expr


# In[21]:


expr.subs(x,1)


# In[22]:


expr.subs(x,0)


# También se pueden sustituir expresiones

# In[23]:


y=sp.symbols("y")


# In[24]:


expr = x**y


# In[25]:


expr


# In[26]:


expr = expr.subs(y, x**y)
expr


# In[27]:


from sympy import *


# In[29]:


expr = sin(2*x)

expand_trig(expr)


# In[30]:


expr.subs(sin(2*x), 2*sin(x)*cos(x)).subs(cos(2*x),2*cos(x)**2-1)


# In[31]:


z=symbols("z")
expr = x**3 + 4*x*y - z
expr


# In[32]:


expr.subs([(x, 2), (y, 4), (z, 0)])


# #### Convertir cadenas a expresiones SymPy 
# 
# Usamos sympify para convertir cadenas en expresiones:
# 

# In[30]:


str_expr = "x**2 + 3*x - 1/2"
print(str_expr)
expr = sympify(str_expr)
expr


# In[33]:


import ipywidgets as widgets
from ipywidgets import interact


# In[42]:


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

# In[43]:


expr = sqrt(8)
expr


# In[44]:


expr.evalf()


# subsy evalf son buenos si desea hacer una evaluación simple, pero si tiene la intención de evaluar una expresión en muchos puntos, hay formas más eficientes. Por ejemplo, si desea evaluar una expresión en mil puntos, usar SymPy sería mucho más lento de lo necesario, especialmente si solo le importa la precisión de la máquina. En su lugar, debe usar bibliotecas como NumPy y SciPy .
# 
# La forma más fácil de convertir una expresión SymPy en una expresión que puede evaluarse numéricamente es usar la lambdifyfunción. lambdifyactúa como una lambdafunción, excepto que convierte los nombres de SymPy a los nombres de la biblioteca numérica dada, generalmente NumPy. Por ejemplo

# In[45]:


import numpy as np
a = np.arange(10) 
a


# In[46]:


expr = sin(x)


# In[47]:


f = lambdify(x, expr, "numpy") 


# In[48]:


f(a) 


# In[51]:


f = lambdify(x, expr, "math")
f(5)


# ### Ecuaciones 
# Como sabemos `=` y `==` ya fueron usado en el lenguaje para unas operaciones específicas.
# 
# 

# In[50]:


x+1==4


# In[52]:


sp.Eq(x + 1, 4)


# ## Igualdad de expresiones y simplificación
# 
# Ahora saltemos y hagamos algunas matemáticas interesantes. Una de las características más útiles de un sistema de manipulación simbólica es la capacidad de simplificar expresiones matemáticas. 
# 
# 
# SymPy tiene docenas de funciones para realizar varios tipos de simplificación. También hay una función general llamada simplify()que intenta aplicar todas estas funciones de manera inteligente para llegar a la forma más simple de una expresión. Aquí hay unos ejemplos

# Es importante tener esta definición en cuenta cuando se presentan igualdades entre expresiones.

# In[53]:


simplify(sin(x)**2 + cos(x)**2)


# In[54]:


(x**3 + x**2 - x - 1)/(x**2 + 2*x + 1)


# In[55]:


simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))


# In[56]:


simplify(gamma(x)/gamma(x - 2))


# In[57]:


simplify (x**2+2*x+1 - (x+1)**2)


# Un problema de simplify()es que puede ser innecesariamente lento, ya que intenta muchos tipos de simplificaciones antes de elegir la mejor. Si ya sabe exactamente qué tipo de simplificación está buscando, es mejor aplicar las funciones de simplificación específicas que aplican esas simplificaciones.
# 
# 

# ### Simplificación de funciones polinómicas racionales
# 
# expand()es una de las funciones de simplificación más comunes en SymPy. Aunque tiene muchos ámbitos, por ahora, consideraremos su función en la expansión de expresiones polinómicas. Por ejemplo:
# 
# 

# In[57]:


expand((x+2)**3)


# factor()toma un polinomio y lo factoriza en factores irreducibles sobre los números racionales. Por ejemplo:

# In[58]:


factor(x**3-x**2+x-1)


# In[59]:


factor_list(x**3-x**2+x-1)


# cancel() tomará cualquier función racional y la pondrá en la forma canónica estándar, 𝑝𝑞, dónde 𝑝 y 𝑞 son polinomios expandidos sin factores comunes, y los coeficientes principales de 𝑝 y 𝑞 no tienen denominadores (es decir, son enteros).

# In[60]:


cancel((x**2 + 2*x + 1)/(x**2 + x))


# In[61]:


expr = (x*y**2 - 2*x*y*z + x*z**2 + y**2 - 2*y*z + z**2)/(x**2 - 1)
expr


# In[62]:


cancel(expr)


# apart() realiza una descomposición de fracción parcial en una función racional.

# In[63]:


expr = (4*x**3 + 21*x**2 + 10*x + 12)/(x**4 + 5*x**3 + 5*x**2 + 4*x)
expr


# In[64]:


apart(expr)


# Para simplificar expresiones usando identidades trigonométricas, use trigsimp().

# In[65]:


trigsimp(sin(x)*tan(x)/sec(x))


# In[66]:


cancel(sin(x)*tan(x)/sec(x))


# Para expandir las funciones trigonométricas, es decir, aplicar la suma o las identidades de doble ángulo, use expand_trig().

# In[67]:


expand_trig(sin(x + y))


# In[68]:


expand_trig(tan(2*x))


# powsimp() permite simplificaciones con leyes de exponentes.

# In[69]:


x, y = symbols('x y', positive=True)

a, b = symbols('a b', real=True)

z, t, c = symbols('z t c')


# In[70]:


powsimp(x**a*x**b)


# In[71]:


powsimp(z**t*z**c)


# **rewrite()**
# Podemos reescribir algunas funciones especiales en términos de otra:

# In[72]:


tan(x).rewrite(sin)


# In[73]:


factorial(x).rewrite(gamma)


# In[74]:


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

# In[78]:


L=[1,2,3]
L.reverse()
L


# In[86]:


def lista_a_fraccion(L):
    L.reverse()
    expr=Integer(0)
    for i in L:
        expr=1/(expr+i)
    return expr


# In[87]:


lista_a_fraccion([x,y,z])


# In[88]:


lista_a_fraccion([1,2*x,3])


# ## Cálculo
# 
# SymPy también permite realizar tareas básicas del cálculo diferencial e integral. 

# In[90]:


from sympy import *
x, y, z = symbols('x y z')


# In[91]:


diff(cos(x),x) #derivadas en una sola variable


# In[92]:


diff(exp(4*x**2+5*x),x) #derivadas en una sola variable


# In[93]:


diff(y*exp(4*x**2+5*y),x) #derivadas parciales


# In[94]:


diff(cos(x),x,x)  #derivadas de orden superior


# In[95]:


diff(cos(x),x,x,x)


# In[96]:


diff(cos(x),x,3) 


# In[97]:


diff(y*exp(4*x**2+5*y),x,y) #derivadas de orden superior


# Como en las ecuaciones, a veces requerimos derivadas expresadas, sin evaluarse:

# In[98]:


deriv = Derivative( exp (x * y * z), x, y, y, z)
deriv


# Para evaluarla:

# In[99]:


deriv.doit()


# In[100]:


diff( exp (x * y * z), x, y, y, z)


# In[100]:


integrate(cos(x),x) # Integrales


# In[101]:


integrate(exp (-x), (x, 0, oo))


# In[102]:


Integral(exp (-x), (x, 0, oo))


# In[103]:


Integral(exp (-x), (x, 0, oo)).doit()


# In[105]:


integrate(x**2, (x, 0,1))


# In[104]:


Integral(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))


# In[105]:


integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))


# In[109]:


Integral(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo)).doit()


# Y ¿si la integral no es posible de calcular?

# In[106]:


integrate(x**x, x)


# Para expresar una integral no evaluada usamos `Integral`:

# In[107]:


integ=Integral((x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x -exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1)), x)
integ


# In[108]:


integ.doit()


# In[109]:


limit(sin(x)/x, x, 0) #Límites


# In[110]:


expr = sin(x)/x
expr.subs(x, 0)


# In[111]:


limit(expr, x, 0)


# In[113]:


expr = Limit((cos(x) - 1)/x, x, 0,"-") #Límites sin evaluar
expr


# In[114]:


expr.doit()


# In[115]:


expr = exp(sin(x)) 
expr.series(x,0, 10)  # Series


# In[116]:


exp(x - 6).series(x, 6,10) # Series no centradas en 0


# ## Solucionar ecuaciones
# 
# Ahora hagamos una rápida exploración por las diferentes ecuaciones que se resuelven en Sympy.

# In[58]:


Eq(x**2,1)


# In[59]:


solveset(Eq(x**2,1),x)


# In[60]:


solveset(Eq(x**2,1),x)[0]


# In[62]:


list(solveset(Eq(x**2,1),x))[0]


# In[63]:


solveset(x ** 2 - x, x) # Raices


# In[64]:


solveset(x - x, x)


# In[67]:


solveset(x - x, x,domain=sp.Integers)


# In[68]:


solveset(x - x, x,domain=Interval(0,10))


# In[69]:


solveset(x - x, x,domain=Interval.Ropen(0,10))


# In[70]:


solveset(x - x, x,domain=Interval.Lopen(0,10))


# In[133]:


solveset(x - x, x,domain=Interval.open(0,10))


# In[71]:


solveset(x - x, x,domain=FiniteSet(0,1,2,3))


# In[73]:


solveset(sin(x) - 1, x, domain=sp.Reals)


# In[74]:


solveset(sin(x) - 1, x, domain=Interval.open(5,34))


# In[75]:


solveset(exp(x), x)     # Cuando la solución no existe


# In[76]:


solveset(cos(x) - x, x)  # Cuando es incapaz de encontrar una solución


# ### Sistemas de ecuaciones lineales
# 
# Usamos `linsolve` para encontrar las soluciones:

# In[77]:


linsolve([x + y + z - 1, x + y + 2*z - 3 ], (x, y, z))


# In[78]:


linsolve([x + y + z - 1, x - y + z - 3,x+y+1 ], (x, y, z))


# In[141]:


linsolve([x + y + z - 1, x + y + z - 3,x+y+1 ], (x, y, z))


# ### Sistemas no lineales
# 
# Usaremos `nonlinsolve`

# In[82]:


a, b, c, d = symbols('a, b, c, d', real=True)


# In[83]:


nonlinsolve([a**2 + a, a - b], [a, b])


# In[84]:


nonlinsolve([x*y - 1, x - 2], x, y)


# ### Ecuaciones diferenciales
# 
# 
# 

# In[85]:


f, g, h = symbols('f g h', cls=Function)


# In[86]:


diffeq = Eq(f(x).diff(x, x) - 2*f(x).diff(x) + f(x), sin(x))
diffeq


# In[87]:


dsolve(diffeq, f(x))


# In[88]:


dsolve(f(x).diff(x)*(1 - sin(f(x))) - 1, f(x))


# In[89]:


f(x).diff(x)*(1 - sin(f(x))) - 1


# In[ ]:




