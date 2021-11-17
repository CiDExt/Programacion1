#!/usr/bin/env python
# coding: utf-8

# # Intermezzo - Paradigmas de programación

# :::::{important} **Sección intermezzo**
# 
# En esta sección nos daremos un respiro para estudiar conceptos importantes en el mundo de la programación, la idea es aclarar un concepto muy general, que ha sido ampliamente utilizado en diversas fuentes académicas, pero que muy frecuentemente es tergiversado porque no se entiende muy bien. 
# 
# Los **paradigmas de programación** constituyen el conjunto de reglas y guías que se siguen para montar los diferentes estilos de solución que pueden ocurrir para ciertos problemas, veremos los más importantes, en que consisten y el tipo de problemas que resuelven.
# :::::
# 
# 
# 
# 

# Antes de definir a que nos referimos pensemos en el siguiente problema:
# 
# 

# :::::{note} **Paradigmas de programación**
# 
# Según las diferentes necesidades de los desarrolladores se ve conveniente diseñar ciertos tipos de solución, claramente, las soluciones pueden tomar diferentes caminos y regirse por varias reglas. Dichos diseños y reglas que rigen a la forma de solucionar el problema los llamaremos **paradigma de programación**. Más aún,
# 
# ---
# Un **paradigma de programación** indica las guías y métodos de realizar cálculos y la manera en que se deben estructurar y organizar las tareas que debe llevar a cabo un programa. Se asocian a cierto estilo de programación y al modelo de computación (operaciones permitidas) admitido en nuestro sistema.
# 
# ---
# 
# 
# Por ejemplo, si yo quisiera acceder a una lista con los primeros 5 enteros positivos y guardarlos en la variable `Lista` tendría por lo menos estas dos opciones:
# 
# ````{tabbed} Opción 1
# Declarar la lista de forma directa:
# ```Python
# Lista=list(range(1,6))
# ```
# ````
# 
# ````{tabbed} Opción 2
# Crear una rutina que la genere:
# 
# ```Python
# Lista=[]
# contador=1
# ## Usamos while, ejecutalo en una celda y trata de identificar de que se trata.
# ## Si no lo comprendes no te preocues, lo veremos más adelante.
# while contador <6:
#     Lista.append(contador)
#     contador=contador+1
#  
# ```
# ````
# 
# Ambos casos produjeron una lista con los primeros 5 enteros positivos. No obstante, la forma de solucionar este problema fue diferente, en la opción uno se indicó *qué* se iba a calcular. La solución se obtiene al **declarar** lo que requerimos y guardarlos en la variable `Lista`. Por otro lado, en la opción 2 fuimos muy explicitos con la generación de la lista, practicamente se indico *como* se iba a construir la lista guardada en `Lista` paso a paso, ayudados por un `while`.
# 
# 
# Estos enfoques hacen referencia a diferentes paradigmas de programación, pues estructuramos y organizamos las instrucciones para generar la Lista de manera muy diferente. 
# 
# :::::

# ## Tipos de paradigmas
# 
# Si bien hay una cantidad considerable de paradigmas de programación, podemos identificar dos enfoques destacados:
# 
# **Programación imperativa**
# 
# Enfocada en explicar el cómo debe realizarse el cálculo, sigue una serie de instrucciones inmersas en un control de flujo explicito. En este caso, las variables *son constantemente modificadas* y representan el desarrollo del cálculo. Entre los diferentes paradigmas que se rigen según este enfoque se encuentran **paradigma de programación estructurada** y **paradigma de programación modular**: 
# 
# ````{tabbed} Programación Estructurada
# 
# Parte de un hermoso resultado de la teoría de lenguajes de programación conocido como el [teorema de Böhm–Jacopini](https://en.wikipedia.org/wiki/Structured_program_theorem) que afirma que toda función computable puede implementarse utilizando únicamente tres estructuras lógicas **(estructuras de control)**: secuenciación, selección e iteración.
# 
# 
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 50.00%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1000" height="500" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/61944099c121b10d88a24212" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>
# 
# 
# 
# ````
# ````{tabbed} Programación Modular
# 
# Usa el principio de que un problema se puede dividir en subproblemas, permite dividir un programa en módulos (programas más simples), con el fin de hacerlo más legible y manejable. Los elementos modulares más básicos pueden verse como funciones que admiten entradas y producen salidas.
# 
# <div style="width: 100%;"><div style="position: relative; padding-bottom: 50.00%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1000" height="500" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/61945398c5d9760d8b0ea779" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>
# 
# ````
# 
# ````{tabbed} Programación Orientada a Objetos
# 
# Los programas se modelan en torno a objetos, entidades que encapsulan atributos y funciones (o métodos) en una sola entidad. Para dar más claridad pensemos un objeto como una persona, que se distingue por los atributos que la describen pero que puede ejecutar varias acciones (o métodos).
# 
# ![Clases](https://pythones.net/wp-content/uploads/2019/01/Clases-y-Objetos-min-577x1024-min.png)
# 
# *Tomada de [https://pythones.net/clases-y-metodos-python-oop/](https://pythones.net/clases-y-metodos-python-oop/)*
# 
# ````
# 
# 
# **Programación declarativa**
# 
# Describe **que** se debe calcular, no hace referencia a métodos de evaluación y cada vez que se *instancia* una variable se vuelve inmutable. No requiere sentencias de asignación y el flujo se asocia a composición funcional, recursividad,reescritura y unificación. Entre estas se destacan el **paradigma de programación funcional** y el **paradigma de programación lógica**.
# 
# ````{tabbed} Programación Lógica
# 
# Basada en la [lógica de predicados (o lógica de primer orden)](https://es.wikipedia.org/wiki/L%C3%B3gica_de_primer_orden), busca resolver problemas a partir de la posibilidad de plantear problemas como conjuntos de sentencias expresadas en forma lógica que, a partir de reglas de inferencia (deducciones), permiten automatizar la solución. Se basa en la idea:
# 
# ![Tomado de https://ferestrepoca.github.io/paradigmas-de-programacion/proglogica/logica_teoria/proglogica.html](https://ferestrepoca.github.io/paradigmas-de-programacion/proglogica/logica_teoria/img/001.png)
# 
# Qué en otras palabras indica que cada programa es una deducción controlada.
# 
# ![Tomado de https://ferestrepoca.github.io/paradigmas-de-programacion/proglogica/logica_teoria/proglogica.html](https://ferestrepoca.github.io/paradigmas-de-programacion/proglogica/logica_teoria/img/prolog004.PNG)
# 
# Imágenes tomadas de [https://ferestrepoca.github.io/paradigmas-de-programacion/proglogica/logica_teoria/proglogica.html](https://ferestrepoca.github.io/paradigmas-de-programacion/proglogica/logica_teoria/proglogica.html)
# 
# ````
# ````{tabbed} Programación Funcional
# 
# Podría considerarse como una ampliación del [cálculo lambda](https://en.wikipedia.org/wiki/Lambda_calculus), admite a las funciones como elementos primitivos. El objetivo es identificar qué resolver y para lograrlo se utiliza una forma explicita de la función que resolvería el problema.
# 
# 
# ```Python
# def reverse(s):
#     return s[::-1]
# reverse("I am a string")
# animals = ["gato", "perro", "buho", "conejo"]
# iterator = map(reverse, animals)
# for i in iterator:
#     print(i)
# iterator = map(reverse, animals)
# list(iterator)
# 
# ```
# 
# 
# ````

# ## Cierre
# 
# Si bien existen paradigmas como tipos de soluciones y parece que hay lenguajes enfocados a trabajar mejor con un paradigma dado, es el modelo de computación, la eficiencia del programa y las condiciones del **problema** lo que determina cual de estos paradigmas es más conveniente. Afortunadamente Python es multiparadigma y permite que trabajemos con diferentes diseños de solución. En el siguiente módulo estudiaremos elementos de la programación estructurada, en particular definiremos las estructuras de control en Python y haremos algunos ejemplos.
