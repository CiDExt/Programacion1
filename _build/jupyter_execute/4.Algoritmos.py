#!/usr/bin/env python
# coding: utf-8

# # Algoritmos, Python y Jupyter
# 
# 
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
# se hace a través de algoritmos procesos libres de ambigüedades y con todos los pasos necesarios para llegar a la dichosa solución.
# 
# ````
# 
# ````{tabbed} Consola bash
# :::{admonition} Recordemos...
# :class: tip
# Ya pudimos establecer comunicación directa con la máquina a traves la consola, pudimos crear, mover y modificar archivos. Usamos un algoritmo muy simple para crear un nuevo texto e interactuamos con la consola para descubrir todas las propiedades de sus archivos y directorios.
# :::
# ````
# 
# 
# ````{tabbed} Página en github
# :::{admonition} Recordemos...
# :class: tip
# Seguimos un tutorial detallado para empezar a manejar repositorios locales y en línea. Adicionalmente, vimos elementos básicos para la creación de páginas utilizando una rama adicional de los repositorios. Esperamos que en esas páginas haya una descripción completa de sus perfiles, ilusiones y los que serían sus próximos proyectos.
# :::
# ````
# 
# 
# :::::
# 
# Estudiaremos hoy herramientas que me permiten diagramar o representar los algoritmos y hablaremos un poco del lenguaje de programnación que estudiaremos hoy. También de Jupyter, el aplicativo web en el que trabajaremos nuestros cuadernos y documentaremos nuestras experiencias.

# ## Algoritmos
# 
# Aunque nos hemos referido a los algoritmos y hemos citados algunos ejemplos, se ha dicho que no se dará una definición formal, sin embargo, vale la pena mencionar diferentes herramientas que utilizaremos en este curso para tener claro los pasos que se llevarán a cabo antes de empezar a codificar. Hablaremos de pseudocódigo y diagramas de flujo.
# 
# ### Pseudo-código
# 
# Se trata de una descripción de un algoritmo de una manera plana y compacta. Utiliza diversas normas y reglas estructurales de un lenguaje de programación pero se escribe en lenguaje natural. Particularmente en español resulta bastante útil puesto que la mayoría de lenguajes se escriben en inglés, en ese caso podríamos entenderlo como la traducción apropiada de un código al lenguaje natural.
# 
# 
# **Ejemplos de pseudocódigo**
# 
# En el estudio de bash creamos un algoritmo para crear un nuevo archivo, el pseudocódigo que equivale a esa acción es el siguiente:
# 
# ````{prf:algorithm} Crear un archivo
# :label: Crear un archivo
# 
# **Input** La información a guardar:
# 
# ```console
# día ganancia                                               
# 01  $5000                                                   
# 02  $8000                                                   
# 03  $9000   
# ```
# 
# **Output** Archivo testfile.txt con esa información
# 
# 1. Identificar carpeta de trabajo
# 2. Si estamos en el directorio, 
#         crear carpeta prueba;   
#    si no, 
#        dirigirse al directorio base y crear la carpeta de prueba.
#        
# 3. Ingresar a la carpeta prueba.
# 
# 4. Crear testfile.txt.
# 
# 5. Ingresar la siguiente información en  testfile.txt
# 
# 6. **Guardar y salir**
# 
# ```` 
# 
# Como se puede apreciar, se ha descrito detalladamente el ejercicio de esa sección pero no se ha mencionado ningún lenguaje de programación, ni la sintáxis de la consola. En este caso, el algoritmo se puede presentar libre del lenguaje y basta con una sucesión clara, ordenada y detallada del proceso que soluciona nuestro problema.
# 
# Usaremos esta estructura constantemente para describir algunas soluciones para los ejercicios propuestos de este curso.
# 
# 

# ### Diagramas de flujo
# 
# Esta es una representación gráfica de un procedimiento o de un algoritmo. Se utiliza en diversas ramas y no solo para progamación de computadores, verás estos diagramas en asignación de actividades, descripción de procesos, investigación de operaciones, entre otros.
# 
# Dicho diagrama sigue unas convenciones para cada node del grafo, dicho nodo expresa una situación o concepto y se mueve de acuerdo a las flechas del diagrama, veamos las convenciones:
# 
# ```{tabbed} Línea de flujo
# 
# ![flecha](https://upload.wikimedia.org/wikipedia/commons/thumb/6/6c/Flowchart_Line.svg/100px-Flowchart_Line.svg.png)
# 
# Indica la dirección del flujo.
# 
# ```
# 
# ```{tabbed} Terminal
# ![terminal](https://support.content.office.net/es-es/media/022c8ba9-01e8-4fd1-9967-170e82450352.gif)
# 
# Indica el inicio o final del proceso.
# 
# ```
# 
# ```{tabbed} Proceso
# ![proceso](https://support.content.office.net/es-es/media/0f129ef2-5081-4d99-98b1-e288211dbd0d.gif)
# 
# Representa un paso del proceso en el que se cambian valores, formas o ubicaciones de datos. Se entiende como un paso típico del procedimiento.
# 
# ```
# 
# ```{tabbed} Decisión
# ![decisión](https://support.content.office.net/es-es/media/d4c68a25-77e1-43eb-be3c-9a5ea2b75d8b.gif)
# 
# Hace referencia a una parte del proceso en el que se pueden tomar varios cáminos. Por ejemplo si se evalúa una condición generalmente la respuesta es sí o no.
# 
# ```
# 
# ```{tabbed} Documento
# ![decisión](https://support.content.office.net/es-es/media/908189d1-3723-4671-8a75-da38f163e608.gif)
# 
# Hace referencia a una parte del proceso en el que se obtiene un documento como salida.
# ```
# 
# ```{tabbed} Datos
# ![datos](https://support.content.office.net/es-es/media/5036f7e8-c5c5-4cf1-a927-9b6593ae7640.gif)
# 
# Indica que entra o sale algo del proceso (datos, materiales, etc.)
# ```
# 
# ```{tabbed} Referencia
# ![Referencia](https://support.content.office.net/es-es/media/dc191c39-e01f-474c-8c81-1230e60e3a07.gif)
# 
# Indica que un paso siguiente (o anterior) que se encuentra en otra parte del dibujo. Se usa cuando tenemos diagramas bien complejos.
# ```

# Para el ejercicio anterior usamos un diagrama de flujo, verifica que dicho diagrama corresponde con las convenciones del diagrama:

# <div style="width: 100%;"><div style="position: relative; padding-bottom: 141.40%; padding-top: 0; height: 0;"><iframe frameborder="0" width="1000" height="1414" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;" src="https://view.genial.ly/61899ad1607edd0d489c209f" type="text/html" allowscriptaccess="always" allowfullscreen="true" scrolling="yes" allownetworking="all"></iframe> </div> </div>

# ## Python
# 
# Python es un lenguaje multiparadigma y de alto nivel cuya filosofia se sustenta en la sencillez de código. Resulta ser uno de los lenguajes más flexibles de la actualidad en el que se destacan sus usos en:
# 
# * Desarrollo web en servidores,
# * Desarrollo de Software,
# * Cálculos Matemáticos,
# * Desarrollo de Scripts.
# 
# Por ser de código abierto es gratuito y funciona en diferentes plataformas (Windows, Mac, Linux, etc). Resulta tener una sintaxis simple, similar al idioma inglés, ha aumentado su popularidad desde hace pocos años y hoy es el lenguaje de mayor crecimiento y más consultado en el mundo. Permite crear programas en muy pocas líneas, respecto a otros lenguajes de programación.
# 
# Pyhton se ejecuta en un sistema interpretado. Es decir, que los códigos se pueden correr justo después de ser escritos; en otras palabras, no necesitan compilación previa. Se puede usar como un lenguaje clásico, como un lenguaje orientado a objetos, o como un lenguaje funcional. Es el principal lenguaje de la Ciencia de Datos. De hecho, uno de los complementos especiales de Python para los científicos de datos es Jupyter, una aplicación web que permite crear cuadernos interactivos: documentos web editados con texto enriquecido y celdas de ejecución de código.
# 
# La posibilidad de ejecutar código y texto en un mismo documento nos permitirá definir algoritmos y explicarlos de manera adecuada, procesar datos y visualizar resultados inmediatamente, establecer una documentación adecuada de los procedimientos y recursos que usamos, entre otros.

# :::{admonition} Ver también
# :class: seealso
# ![Python logo](https://www.python.org/static/community_logos/python-logo.png) [Python ](https://www.python.org/)
# :::

# ### Instrucciones de instalación y uso de Jupyter
# 
# 

# Sigue los siguientes pasos para instalar jupyter en tu pc:
# 
# 1. Descargar Anaconda de (https://www.anaconda.com/distribution/), verifica que la descarga corresponda a Python 3.7 y a las condiciones específicas de tu equipo (Windows x64, Windows x32, macOS o Linux)
# 
# 
# 2. Despúes de instalar Anaconda abrelo y lanza el aplicativo de Jupyter:
# 
# <img src="https://raw.githubusercontent.com/Izainea/MCG2/master/AnacondaOpen.png" width="720" >
# 
# 3. Jupyter abrirá una pestaña de tu navegador predeterminado, verás algo así:
# 
# <img src="https://github.com/Izainea/MCG2/blob/master/jupyterOpen.png?raw=true" width="720" >
# 
# 
# 4. En el boton NEW puedes crear un archivo nuevo en Python 3:
# 
# <img src="https://github.com/Izainea/MCG2/blob/master/jupyterNew.png?raw=true" width="320" >
# 
# 5. Veras un panel como el siguiente, selecciona en la casilla tipo de celda selecciona Markdown, para titular el cuaderno que vas a crear, tambien puedes oprimir [Esc]+[M]:
# 
# <img src="https://github.com/Izainea/MCG2/blob/master/jupyterCode.png?raw=true" width="720" >
# 
# 6. Después de cambiar el tipo de celda usa el formato Markdown para hacer encabezados del documento, escribes ___# Título___ para el encabezado principal y ___## Subtítulo___ para el encabezado secundario:
# 
# <img src="https://github.com/Izainea/MCG2/blob/master/jupyterFirstCell.png?raw=true" width="720" >
# 
# 7. Después de escribir oprimes [Shift]+[Enter] para ejecutar la celda y visualizar el resultado final de tu escrito, obtienes:
# 
# <img src="https://github.com/Izainea/MCG2/blob/master/jupyterFirstCell2.png?raw=true" width="720" >
# 
# 8. Finalmente, para terminar este ejercicio haremos una operación muy simple para verificar el buen funcionamiento del programa, escribimos en la siguiente celda 5+8 y ejecutamos nuevamente con [Shift]+[Enter]:
# 
# <img src="https://github.com/Izainea/MCG2/blob/master/jupyterFirstRun.png?raw=true" width="720" >

# ## Markdown
# 
# Markdown es un lenguaje de marcado ligero escrito por John Gruber (https://daringfireball.net/projects/markdown/) que permite convertir texto plano en HTML. Aunque suene muy complicado es un lenguaje muy senciullo de utilizar y está inspirado en la forma de escritura de los correos electrónicos.
# 
# Veremos a continuación algunas convenciones sencillas de este lenguaje y las aplicaremos en nuestro cuaderno guía:
# 
# <img src="https://www.math.ubc.ca/~pwalls/math-python/img/jupyter/markdown.gif">
# *Tomado de: (https://www.math.ubc.ca/~pwalls/math-python/jupyter/markdown/)*

# ### Salidas de texto
# En la siguiente tabla resumimos algunas convenciones importantes para la escritura de documentos en Markdown:
# 
# | **Escrituta en Celda**| **Salida** |
# |:---:|:---:|
# |`Escritura normal` | Escritura normal|
# |`*énfasis*`| *énfasis*| 
# |`** texto fuerte **` | ** texto fuerte ** |
# |``código`` |`código` |
# 
# 
# 
#   

# ### Creación de listas
#  
#  Tambien podemos crear listas, tanto numeradas como no numeradas:
#  
#  
#   **Numeradas**:
#      
#          ``` 
#          1. Primer elemento
#              1. Primero del primero
#          2. Segundo elemento
#          3. Tercer elemento
#          ```
#  
#   1. Primer elemento
#         1. Primero del primero
#   2. Segundo elemento
#   3. Tercer elemento
#  
#  
#  
#  
#  
#   **NO Numeradas**:
# 
#           ``` 
#         * Primer elemento
#             *otro elemento
#         * Segundo elemento
#         * Tercer elemento
#          ```
#  
#   
#    * Primer elemento
#        * otro elemento
#    * Segundo elemento
#    * Tercer elemento
# 
# 
# 

# ### Links e imágenes
#   
# Finalmente, usando este lenguaje también podemos conectar links y visualizar imágenes:
#   
#   **Links**
#   
#   `[Universidad Externado] (https://www.uexternado.edu.co/)`
#   
#   [Universidad Externado](https://www.uexternado.edu.co/ "Universidad Externado")
#   
#   **Imágenes**
#   
#   `![Jupyter logo](http://jupyter.org/assets/nav_logo.svg)`
#   
#   
#   ![Jupyter logo](http://jupyter.org/assets/nav_logo.svg)

# ### Creación de encabezados en el documento
# 
# Es muy útil seccionar el documento por capítulos, subcapítulos, secciones, subsecciones, entre otros. A continuación, visualizamos las formas de crear encabezados en cuadernos de jupyter:
# 
# * **Encabezado 1** 
#  Escribimos: `# Encabezado 1` 
#  
#  
# * **Encabezado 2**
# Escribimos: `## Encabezado 2`
# 
# 
# * **Encabezado 3**
#  Escribimos: `### Encabezado 3`
#  
#  
# * **Encabezado 4**
# Escribimos: `#### Encabezado 4`
# 
#  
# * **Encabezado 5**
#  Escribimos: `##### Encabezado 5`
#  
#  
# * **Encabezado 6**
#  Escribimos: `###### Encabezado 6`

# :::{admonition} Ver también
# :class: seealso
# ![Jupyter logo](http://jupyter.org/assets/nav_logo.svg) [Proyecto Jupyter](https://jupyter.org/)
# :::

# ## Cierre
# 
# Estudiamos la forma de represntar algoritmos utilizando lenguaje natural o diagramas. También conocimos a Python y el aplicativo web que nos permitira correr el código en ese lenguaje: Jupyter. 
# 
# Como Jupyter tiene dos tipos de celda, las de código que usaremos de aquí en adelante para ejecutar nuestros códigos de programación y las de texto, que permiten documentar de manera especial nuestros algoritmos, empezamos con la sintáxis de las celdas de texto que se conoce como lenguaje Markdown o texto enriquecido. Usaremos estas herramientas para crear cuadernos elegantes, claros y explicativos. 
