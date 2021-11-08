#!/usr/bin/env python
# coding: utf-8

# # Introducción a la programación
# **Pregrado - Ciencia de Datos**
# ***Universidad Externado de Colombia***
# 
# *Miguel Angel Rippe Espinoza* 
# [miguel.rippe@uexternado.edu.co](mailto:miguel.rippe@uexternado.edu.co)
# 
# *Carlos Isaac Zainea Maya* 
# [carlos.zainea@uexternado.edu.co](mailto:carlos.zainea@uexternado.edu.co)
# 
# Quizás los grandes avances que ha tenido la ciencia hasta estos días no se hubieran alcanzado sin las computadoras, una idea que empezó a tener forma a eso de 1936 cuando Alan Turing en su mente formalizaba la idea de algoritmo y creaba una máquina hipotética que representaba la posibilidad del cálculo mecánico, posteriormente en EE.UU., Alemania e Inglaterra se crearon dichas máquinas de computo  inspirados en esta idea (los primeros computadores). 
# 

# |**Primera computadora creada por IBM 1944**|
# |:--|
# |[![Harvard Mark I Computer - Right Segment.JPG](https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Harvard_Mark_I_Computer_-_Right_Segment.JPG/1200px-Harvard_Mark_I_Computer_-_Right_Segment.JPG)](https://commons.wikimedia.org/wiki/File:Harvard_Mark_I_Computer_-_Right_Segment.JPG#/media/Archivo:Harvard_Mark_I_Computer_-_Right_Segment.JPG)|
# |[Creative Commons Attribution-Share Alike 3.0](http://creativecommons.org/licenses/by-sa/3.0/)|
# |[Enlace Wikipedia](https://commons.wikimedia.org/w/index.php?curid=601387)|
# 

# Sin embargo, el acceso a esas máquinas requerían un lenguaje muy diferente al que estamos acostumbrados, era necesario un alto grado de formalidad y crear instrucciones capaces de reconocer, sin ambigüedades, las ordenes que le proponemos a la máquina, en ese sentido, la comunicación con la dicha máquina de computo se convirtió en el problema de los programadores y hasta hoy se constituye como el reto de hacer que las máquinas hagan los trabajos por nosotros. El día de hoy iniciaremos ese camino para enseñarle al computador, aprenderemos ese lenguaje libre de ambigüedades y nos especializaremos en la creación de algoritmos, uno de los eslabones entre el hombre y la máquina.
# 
# **¡Bienvenidos a su curso de programación!**

# ## ¿Qué hace un programador?
# 
# La tarea se puede describir fácilmente:
# 
# ***
# *Convertir **soluciones** en instrucciones que pueda seguir un computador*
# ***
# 
# Dejamos la palabra soluciones resaltada porque hay una gran cantidad de tareas que se pueden enmarcar como una solución y debemos ser cuidadosos porque las soluciones aquí planteadas deben llevarse a cabo por computadores. Por ejemplo, si la solución es buscar la paz mundial seguramente no habrá una máquina que pueda llevarla a cabo y un programador que sea capaz de desarrollar una solución a esa tarea...¿o no?

# |  |
# |:--|
# |[![Ultron2013.jpg](https://upload.wikimedia.org/wikipedia/en/4/4f/Ultron2013.jpg)](https://en.wikipedia.org/wiki/File:Ultron2013.jpg#/media/File:Ultron2013.jpg)|
# |*Ultron*|
# |[Fair use of copyrighted material in the context of Ultron](https:///en.wikipedia.org/wiki/File:Ultron2013.jpg)|
# |[Enlace Wikipedia](https://en.wikipedia.org/w/index.php?curid=40339454)|
# 
# 

# Volviendo al tema, esas soluciones son planteadas como una sucesión de reglas bien escritas y sin ningún tipo de ambigüedades. Las conocemos como algoritmos (que de aquí en adelante serán nuestro principal objeto de estudio) y los describiremos, principalmente, en el lenguaje de programación Python, sin embargo iniciaremos con ejemplos de la vida diaria, porque esos algoritmos son más empleados de lo que ustedes creen.

# ## Algoritmos entre nosotros
# 
# Casi todas las actividades que realizamos, las reglas que seguimos o los hábitos que tenemos son tareas que hacen parte de un algoritmo. Una definición formal de algoritmo puede llevarnos mucho tiempo y quizás debemos entender un poco más de matemáticas para comprenderla. No obstante, una definición intuitiva que podría ser de gran utilidad es la siguiente:
# 
# ***
# Un algoritmo es una sucesión de tareas (procedimiento) bien definido que permite resolver un problema.  
# ***
# 
# Así:
# 
# * Identificar la ropa sucia de mi cuarto es un proceso algorítmico, que si bien puede llevarse a cabo de diferentes maneras, una de ellas podría ser la siguiente:
# 
#     1. Dejar toda la ropa a inspeccionar en un solo lugar.
#     2. Decidir según su olor, color y textura si está sucia o no.
#     3. Empaquetar la ropa sucia en un contenedor adecuado y hacer un proceso similar con la ropa limpia, es claro que los contenedores deben ser diferentes.
#     4. Entregar la ropa sucia a las personas que lo han requerido.
#     
#     
# * Una **receta de cocina** podría ser una forma de registrar un proceso algorítmico, tenga cuidado con las ambigüedades, porque esas frases como: *sal al gusto*, *una taza de harina (sin especificar una referencia en capacidad adecuada)*, son las que dañan las preparaciones. 
# * Los **métodos de factorización** esos procesos lindísimos del álgebra elemental para poder expresar un tipo de polinomios en la multiplicación de polinomios de menor grado son algoritmos completos y coherentes sin ambigüedades y fáciles de ejecutar.
# 
# * Entre muchos otros ejemplos ¿Identificas algoritmos en tu rutina?

# ## Cierre
# 
# En esencia estudiaremos en este curso tres aspectos fundamentales:
# 
# - Los *algoritmos*, algunas consideraciones y herramientas que deben considerarse para diseñar una solución adecuada.
# - La *codificación*, particularmente usamos el lenguaje de programación Python para expresar los algoritmos que pueden solucionarse en los computadores.
# - Las *buenas prácticas*: una serie de recomendaciones y reglas que deben seguirse para crear buenas piezas de código, bien documentadas y con sus muestras de eficiencia y eficacia en su ejecución.
