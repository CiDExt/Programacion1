#!/usr/bin/env python
# coding: utf-8

# ## Excepciones

# :::::{important} ¿Qué aprenderemos?
# 
# 
# Excepciones y errores
# 
# ````{tabbed} Excepciones 
# 
# :::{admonition} ¿Qué son?
# :class: tip
# Cada vez que Python se encuentra con un error este puede ser un error sintáctico o una excepción. Veremos como lidiar con las excepciones y grarantizar que Python continue sus ejecuciones a pesar de encontrar este tipo de problemas.
# :::
# ````
# 
# :::::

# Como lo comentamos a inicio del curso hay varios tipos de errores, pero estos errores se engloban en dos grandes grupos:
# 
# * Errorers sintácticos
# * Errores de excepción
# 
# En el caso del **error sintáctico**, Python intenta mostrar donde se encuentra esa falla sintáctica:

# In[1]:


print('Hola Mundo)


# Observe la flecha mostrando que hace falta. Otro ejemplo es:

# In[4]:


if 1==1:
print('hola')


# En el casdo de **excepciones** nos referimos a errores que provienen de una sintáxis correcta pero el resultado en sí es un error. Generalmente, la última línea indica como fue ese error:

# In[5]:


print(5/0)


# In[6]:


print(x)


# Una lista de las excepciones incorpopradas en Python se puede encontrar [aquí: https://docs.python.org/es/3/library/exceptions.html](https://docs.python.org/es/3/library/exceptions.html) 
# 
# Revisemos esa lista e identifiquemos algunas de las más comunes.

# ## Nuestras propias excepciones
# 
# Si en la mitad de nuestro algoritmo algo que no queremos que ocurra pasa, podemos plantear una excepción con raise, veamos:

# In[7]:


Nota=2.5

if Nota <3:
    raise Exception('La nota debe ser mayor a 3.0 para los chicos pilos...')


# Python detuvo la ejecución y mostró la (d)excepción por tener una nota menor a 3.

# Los mensajes en pantalla también se puede mostrar para condiciones que se satisfacen. Usamos assert y verifica si las condiciones se cumplen:

# In[9]:


Nota=3.5
assert (Nota > 3), "Falta Nota"


# No paso nada porque cumplimos las condiciones, pero si:

# In[10]:


Nota=2.5
assert (Nota > 3), "Falta Nota"


# ## Manejo de excepciones
# 
# En python podemos usar el bloque `try` -> `except` que después de detectar una excepción sigue unas condiciones para realizar en vez de frenar el cálculo. Python ejecuta código siguiendo la declaración `try` y si encuentra un problema ejecutará las instruccione de  `except`:

# In[13]:


Lista=[3,0,5,6,0,1,2]
for i in Lista:
    try:
        print('El inverso de',i,'es',1/i)
    except:
        print('¡Uy! la lista tierne ceros')


# Observe que sin el bloque `try` -> `except` tendriamos problemas en la ejecución del código:

# In[12]:


Lista=[3,0,5,6,0,1,2]
for i in Lista:
    print('El inverso de',i,'es',1/i)
    


# Pues al encontrar excepciones Python suspende la ejecución.

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/61b017dc9395c70d8715984a" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# ##  Clausula else
# 
# En caso de no encontrar excepciones, podemos indicarle a Python que siga unas instrucciones usando `else`:
# 
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 56.25%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="675" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/61b018c689c14a0d7e792a31" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# Veamos un ejemplo:

# In[16]:


Lista=[3,0,5,6,0,1,2]
try:
    for i in Lista:
        print('El inverso de',i,'es',1/i)
except:
        print('¡Uy! la lista tierne ceros')
else:
        print('Este ejercicio se logró')


# Tenga cuidado porque aquí cambiamos el orden de los bloques según el ejemplo anterior. ¿Cómo cambió?

# In[18]:


Lista=[3,5,6,1,2]
try:
    for i in Lista:
        print('El inverso de',i,'es',1/i)
except:
        print('¡Uy! la lista tierne ceros')
else:
        print('Este ejercicio se logró porque es una lista sincera')


# ## Clausula finally
# 
# Finalmente la clausula finally, el código en este bloque simempre se corre, con excepciones o no:

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 83.33%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1200" height="1000" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/61b01a2fdf3d3b0d55e83bcd" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# Veamos un ejemplo:

# In[19]:


Lista=[3,5,6,1,2]
try:
    for i in Lista:
        print('El inverso de',i,'es',1/i)
except:
        print('¡Uy! la lista tierne ceros')
else:
        print('Este ejercicio se logró porque es una lista sincera')
finally:
    print('Este ejercicio terminó')


# In[20]:


Lista=[3,0,5,0,6,1,2]
try:
    for i in Lista:
        print('El inverso de',i,'es',1/i)
except:
        print('¡Uy! la lista tierne ceros')
else:
        print('Este ejercicio se logró porque es una lista sincera')
finally:
    print('Este ejercicio terminó')


# ## Cierre
# 
# Manejar excepciones resulta muy útil cuando no dependemos o no nos fiamos de los datos que utilizamos. Por ejemplo, si estamos leyendo páginmas en internet usando un raspador web, seguramente habrán momentos en que la conexión sufra, en este caso podemos establecer que hacer en ese momento y mantener el código corriendo mientras se recupera la conexión.
