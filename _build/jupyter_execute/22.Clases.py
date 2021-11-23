#!/usr/bin/env python
# coding: utf-8

# # La programación orientada a objetos
# 
# Una de las características principales de Python es que es un lenguaje multiparadigma, sin embargo, hasta el momento hemos trabajado con las características de programación estructurada *(estructuras de datos y estructuras de control)*. No obstante, también se menciono que Python como lenguaje admite la programación orientada a objetos, y con las **clases** materializamos este paradigma de programación, entendiendolas como *plantillas*  para la creación de objetos.
# 
# Un **objeto**, encapsulará atributos y funciones (o métodos) en una sola entidad. 
# 

# ## Clases
# 
# Una clase es un modelo para crear a partir de ella ciertos Objetos. Contendrá las características y capacidades que tendrá el objeto que sea cree a partir de ella.
# 
# Así a su vez los objetos creados a partir de una clase estarán agrupados en esa misma entidad. Veamos un ejemplo:
# 
# **Clase Fracción**
# 
# Hagamos en python una estructura de datos que luzca como las fracciones. Para ello crearemos una clase que inicialice con los dos componentes que conforman a la fracción el numerador y el denominador.
# 
# 

# In[1]:


3/5


# In[2]:


class Fraccion:
    def __init__(self,numerador,denominador):

        self.num = numerador
        self.den = denominador


# Observe que la clase se inicializa con tres elementos (self, arriba, abajo). self es un parámetro especial que hace referencia al objeto mismo y siempre se pone como el primer parámetro formal. Sin embargo, nunca tendrá un valor real en la ejecución de la clase.
# 
# La notación self.num en el constructor define que el objeto fraccion tenga un objeto de datos interno llamado num como parte de su estado. Del mismo modo, self.den crea el denominador.
# 
# Todas las instancias (objetos construidos a partir de la clase) se definirán con esos dos parámetros formales.

# In[3]:


PrimerFraccion = Fraccion(3,5)


# In[4]:


print(PrimerFraccion)


# El objeto fraccion cuando se muestra imprime la referencia real que se almacena en la variable (la dirección en sí misma). Esto no es lo que queremos. Buscamos una cadena (incluso textual) para identificar la fracción tal y como la conocemos. 
# 
# Entonces podemos definir una función para visualizar la fracción, modificamos la clase incluyendo un método o función nueva:

# In[5]:


class Fraccion:
    def __init__(self,numerador,denominador):

        self.num = numerador
        self.den = denominador
        
    def ver(self):
        print(str(self.num)+"/"+str(self.den))


# In[6]:


PrimerFraccion = Fraccion(6,8)
PrimerFraccion.ver()


# También podemos verla, a partir de un print, definiendolo de una manera directa utilizando un método de nombre `__str__` convierte al objeto en una cadena.

# In[7]:


class Fraccion:
    def __init__(self,numerador,denominador):

        self.num = numerador
        self.den = denominador
        
    def ver(self):
        print(self.num,"/",self.den)
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    


# In[8]:


PrimerFraccion = Fraccion(3,5)
print(PrimerFraccion)


# Hay varios métodos que hacen referencia a esas notaciones estándar, por ejemplo pensemos en la suma (+), veamos que ocurre si intento sumar fracciones: 

# In[9]:


f1=Fraccion(2,5)
f2=Fraccion(1,4)


# In[10]:


f1+f2


# In[ ]:


class Fraccion:
    def __init__(self,numerador,denominador):

        self.num = numerador
        self.den = denominador
        
    def ver(self):
        print(self.num,"/",self.den)
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    def sumar(self,fraccion2):
        sumnum=self.num*fraccion2.den+self.den*fraccion2.num
        sumden=self.den*fraccion2.den
        return  Fraccion(sumnum,sumden)


# In[ ]:


f1=Fraccion(2,5)
f2=Fraccion(1,4)


# In[ ]:


f3=f1.sumar(f2)
print(f3)


# In[ ]:


f1+f2


# Resulta ser una operación no soprtada, la puedo definir usando  el método `__add__`:

# In[ ]:


class Fraccion:
    def __init__(self,numerador,denominador):

        self.num = numerador
        self.den = denominador
        
    def ver(self):
        print(self.num,"/",self.den)
        
    def __str__(self):
        return str(self.num)+"/"+str(self.den)
    
    def __add__(self,fraccion2):
        sumanum = self.num*fraccion2.den + self.den*fraccion2.num
        sumaden = self.den * fraccion2.den
        return Fraccion(sumanum,sumaden)


# In[ ]:


f1=Fraccion(2,5)
f2=Fraccion(1,4)
print(f1+f2)


# Para buscar los operadores definibles en una clase podemos hacer referencia a los deiferentes métodos que emulan los operadores numéricos ver [Referencia Python *(Emulating numeric types)*](https://docs.python.org/3/reference/datamodel.html?highlight=method%20__add__#object.__add__)
# 
# Para ver más métodos especiales ver [Referencia Python *(Special method names )*](https://docs.python.org/3/reference/datamodel.html?highlight=method%20__add__#special-method-names)

# In[ ]:


def mcd(a,b):
    mcd=1
    c=min(a,b)
    d=max(a,b)
    for i in range(1,c+1):
        if c%i==0:
            if d%i==0:
                mcd=i
    return mcd

class Fraccion:
    def __init__(self,numerador,denominador):

        self.num = numerador
        self.den = denominador
        
        
    def __str__(self):
        M=mcd(self.num,self.den)        
        return str(self.num//M)+"/"+str(self.den//M)
    
    def __add__(self,fraccion2):
        sumanum = self.num*fraccion2.den + self.den*fraccion2.num
        sumaden = self.den * fraccion2.den
        return Fraccion(sumanum,sumaden)
    
    def __sub__(self,fraccion2):
        sumanum = self.num*fraccion2.den - self.den*fraccion2.num
        sumaden = self.den * fraccion2.den
        return Fraccion(sumanum,sumaden)
    
    
    ##Multiplicación     
    def __mul__(self,fraccion2):
        multnum = self.num*fraccion2.num
        multden = self.den * fraccion2.den
        return Fraccion(multnum,multden)
    ## Dividir
    
    def __truediv__(self,fraccion2):
        divnum = self.num * fraccion2.den
        divden = self.den * fraccion2.num
        return Fraccion(divnum,divden)
    
    
    ##Negativos 
    
    def __neg__(self):
        negnum=-self.num
        return Fraccion(negnum,self.den)
    
    
    ## Potencias enteras positivas 
    def __pow__(self,intn): 
        if intn > 0:
            potnum=int((self.num)**intn )
            potden=int((self.den)**intn )
            return Fraccion(potnum,potden) 
        elif intn <0:            
            numeradorPEN=int(self.den**abs(intn))
            denominadorPEN=int(self.num**abs(intn))
            return Fraccion(numeradorPEN,denominadorPEN)
        else:
            return Fraccion(1,1)
    


# In[ ]:


f1=Fraccion(2,5)
f2=Fraccion(4,8)


# In[ ]:


print(f1*f2)


# In[ ]:


print(f1/f2)


# In[ ]:


print(-f1)


# In[ ]:


print(f1**(0))


# In[ ]:


f4=Fraccion(12,4)
print(f4)


# In[ ]:


f1=Fraccion(2,5)


# In[ ]:


print(f1/f4)


# In[ ]:


mcd(36,24)


# In[ ]:


f1=Fraccion(2,5)
f2=Fraccion(1,4)
print(f2-f1)


# ## Otro ejemplo
# 
# Recordemos entonces que el objeto, definido por las clases, almacena información de atributos y métodos (funciones) para hacer algunas tareas, una visualización gráfica de las clases es la siguiente:
# 
# ![Clases](https://pythones.net/wp-content/uploads/2019/01/Clases-y-Objetos-min-577x1024-min.png)
# 
# *Tomada de [https://pythones.net/clases-y-metodos-python-oop/](https://pythones.net/clases-y-metodos-python-oop/)*
# 
# Aquí la clase humano tiene como  **atributos:** Fecha de nacimiento; edad; Padres; Genero...
# 
# como **métodos:** Correr; Caminar y Hablar.
# 
# Los objetos Marcos y Elisa pertenecen a la misma Clase; pero tienen diferentes valores para los atributos y sus métodos quizás obtengan diferentes argumentos (valores para sus parámetros).
# 
# Recuerde que la definición de atributos se hace al definir la función `__init__`.

# Veamos un ejemplo:

# In[ ]:




class Humano(): #Creamos la clase Humano
    def __init__(self, edad, nombre, ocupacion): #Definimos el parámetro edad , nombre y ocupación
        self.edad = edad # Definimos que el atributo edad, sera la edad asignada
        self.nombre = nombre # Definimos que el atributo nombre, sera el nombre asig
        self.ocupacion = ocupacion #DEFINIMOS EL ATRIBUTO DE INSTANCIA OCUPACIÓN
        
        #Creación de un nuevo método
    def presentar(self):
        presentacion = ("Hola soy {name}, mi edad es {age} y mi ocupación es {ocu}") #Mensaje
        print(presentacion.format(name=self.nombre, age=self.edad, ocu=self.ocupacion)) #Usamos FORMAT
        
        
        #Creamos un nuevo método para cambiar la ocupación:
        #En caso que esta persona sea contratada
        
    def contratar(self, puesto): #añadimos un nuevo parámetro en el método
        self.puesto = puesto
        print ("{name} ha sido contratado como {vac}".format(name=self.nombre, vac=self.puesto))
        self.ocupacion = puesto #Ahora cambiamos el atributo ocupación


# In[ ]:


Persona1 = Humano(31, "Pedro", "Desocupado") #Instancia

#Llamamos al método

Persona1.presentar() 


# In[ ]:


Persona1.contratar("Obrero")


# In[ ]:


Persona1.presentar()


# ## Módulos
# 
# Como ven, en algunas ocasiones, veamos el ejemplo Fracción, la cantidad de código puede ser inmanejable. Además, con una reinicialización del nucleo o un bloqueo se pueden perder las definiciones previas. Para evitar este problema creamos módulos, archivos externos con extensión .py que podemos importar a nuestros cuadernos.
# 
# Para este ejercicio usaremos el archivo fibo.py y usaremos las funciones alojadas en él, para importar sin problemas el archivo fibo.py debe estar en la misma carpeta del cuaderno:
# 
# 

# In[ ]:


import fibo


# In[ ]:


print(fibo.fib(1000))


# In[ ]:


fibo.fib2(100)


# In[ ]:


fibo.constante


# In[ ]:


dir(fibo)


# In[ ]:


get_ipython().run_line_magic('pinfo', 'fibo.constante')


# In[ ]:




