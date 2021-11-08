#!/usr/bin/env python
# coding: utf-8

# <div style="padding: -5px;
#   text-align: center;
#   color: white;
#   font-size: 20px;">
#    <img src="images/banner.jpg" alt="MINE-Seminario de programación" style="width:100%;">
#   <h1 style="
#   position: absolute;
#   top: 5%;
#   left: 50%;">Programación en consola - Introducción</h1>
# </div>

# Actualmente, la manera más sencilla de interacción entre una computadora y su usuario, es mediante una **interfaz gráfica de usuario** o **GUI** (**Graphical User Inteface**). Por ejemplo, para abrir un programa, por lo general das clic en el ícono de éste para así ejecutarlo, o  cuando estás en internet, usas el ratón para interactuar con los diferentes elementos dispuestos en las diferentes páginas web. Pero antes de la creación de las GUI, la manera usual para interactuar con la computadora, era mediante una interfaz de línea de comandos o **CLI** (**Command-Line Interface**).
# 
# Algunas de las ventajas que las interfaces de línea de comandos ofrecen son:
# 1. Ejecución de tareas asignando parámetros específicos.
# 2. Automatización de tareas por medio de scripts.
# 3. Es ideal para la administración de sistemas para toda una empresa.
# 
# En vista de tal importancia, lo primero que haremos es abrir la *terminal*, esto depende del sistema operativo, en *OS X* o *Linux*, abriremos la **terminal** mientras que, en *Windows* podremos abrir *PowerShell* o en su defecto [GitBash](https://git-scm.com/downloads).
# 
# 
# De modo que, nuestro primer acercamiento con nuestra CLI, será para aprender a navegar por el sistema de archivos de nuestra computadora:
# 
# Para ello escribe el comando `pwd` (*print work directory*) y luego pulsa *Enter*, esto nos permitirá ver el directorio actual en el que estamos trabajando. En *OS X* o en *Linux* el resultado debería ser como el siguiente: `/usuarios/nombre-de-usuario`; mientras que, en *Windows* sería `C:\usuarios\nombre-de-usuario`.
# 
# Como puedes observar hay diferencias, pero son pocas y no afectarán el desarrollo del resto del cuaderno.
# 
# Para conocer los archivos y carpetas que hay en el directorio en el cual estamos ubicados, podemos utilizar el comando `ls`, el cuál listará todos y cada uno de los elementos antes mencionados.
# 
# ____
# En *OS X* y en *Linux* el comando `ls` arroja la lista únicamente, mientras que, en *Windows* arroja la lista acompañado de la última vez que se modificó el archivo/directorio, su peso y el tipo  (`l` (link), `d` (directory), `a` (archive), `r` (read-only), `h` (hidden), 
# `s` (system)).
# ____
# Para tener el mismo manejo en los diferentes sistemas operativos, a la hora de trabajar en la consola, en *Windows* usaremos el GitBash o instalaremos la consola de Ubuntu en  nuestro sistema, de la siguiente manera:
# 1. `Configuración -> Actialización y Seguridad -> Para programadores`
# Allí debemos habilitar el *Modo de programador*. Debemos aceptar, los cambios.
# <img src="https://github.com/CiDExt/Programacion1/blob/main/images/i1.PNG?raw=true"  width="600">
# 2. Luego, en el menú de inicio buscaremos "activar o desactivar las características de Windows", y allí habilitaremos el *Subsistema de Windows para Linux*. Nos pedirá reiniciar el computador.
# <img src="https://github.com/CiDExt/Programacion1/blob/main/images/i2.png?raw=true" width="400">
# 3. En la Tienda de Microsoft, buscaremos "Ubuntu", para descargar la opción que deseemos.
# <img src="https://github.com/CiDExt/Programacion1/blob/main/images/i3.png?raw=true" width="400">
# 4. Abrimos el PowerShell y ejecutamos el comando `bash`.
# 
# De estamanera tendremos la consola de Ubuntu en Windows.
# ____
# Si estabas en el *PowerShell* y ahora ejecutas `ls` verás que la presentación de la lista es diferente, es como lo ven tus compañeros de *OS X* y  *Ubuntu*.
# 
# Para ver todas las opciones de los comandos y la mejor forma de usarlos, empleamos `man 'comando'`, por ejemplo,`man ls` nos da todas las opciones que tenemos para ver la lista de archivos y carpetas. Ejecuta `ls -l`  para ver una lista larga de los archivos el la carpeta, verás entradas de éste tipo:
# 
# `drwxrwxrwx 1 root root     512 Apr 14 21:22 '3D Objects'`
# 
# La primera entrada, indica el tipo de fichero
# (`d`: directorio, `-`: archivo, `l`: enlace simbólico, `s`: socket, `p`: tubería, `b`: archivo de bloque, `c`: archivo de caracteres). Las tres entradas que siguen indican los permisos del propietario, las tres siguientes, los del grupo y los últimos 3 los permisos de los demás (`r`: *read* 4,  `w`: *write* 2, `x`: *execute* 1), el ejemplo indica que `3D Objects` es una carpeta, y todos los usuarios tienen todos los permisos.
# 
# La siguiente entrada, el número, indica la cantidad de enlaces que tiene el fichero. En el ejemplo el `2`.
# 
# Las dos entradas que siguen, indican el usuario propietario y el grupo propietario. En el ejemplo el `root root`.
# 
# El valor que sigue, es el tamaño del archivo, en nuestro ejemplo `512`. 
# 
# Por último el nombre del archivo o directorio.
# 
# La marca de tiempo que tiene el archivo, nos indica la fecha en que el archivo o directorio fueron modificados por última vez `Apr 14 21:22`.
# 
# **Para crear una nueva carpeta** empleamos el comando `mkdir` (*make directory*), por ejemplo `mkdir prueba`. Para comprobar la creación de la carpeta, puedes ejecutar el comando `ls` y debería aparecer la carpeta que acabamos de crear.
# 
# **Para cambiar de carpeta**, empleamos el comando `cd` (*change directory*), por ejemplo, `cd prueba`. Si deseamos ir a una carpeta diferente empleamos `cd ruta-de-la-carpeta`. El comando `cd` tiene opciones adicionales para moverse con facilidad dentro de las carpetas `cd ..`
# nos lleva a la carpeta de "arriba", mientras que `cd --` nos lleva a la carpeta principal.
# 
# 
# Una vez dentro de nuestra carpeta de prueba, vamos a crear un archivo y lo modificaremos desde la consola, esto lo haremos con el comando `nano testfile.txt`. Lo anterior abre un editor de texto plano, en el cual podemos ingresar la siguiente información:
# 
# día ganancia                                               
# 01 $\$ $5000                                                   
# 02 $\$ $8000                                                   
# 03 $\$ $9000   
# 
# Luego de registrar la información, para guardar el archivo `CTR+X` y luego `Enter`. Para verificar la creación del archivo, recuerda usar el comando `ls`, o si quieres ver la carpeta con tu GUI.
# 
# Podemos verificar la creación del archivo, y los permisos del mismo (ejecuta `ls -l`):
# 
# `-rwxrwxrwx 1 root root 4 Jul 21 11:58 testfile.txt`
# 
# Es decir, el archivo que creamos tiene todos los permisos, para todos los usuarios. Si queremos modificar esto, empleamos el comando `chmod`, ten presente su sintáxis: `chmod 'a_quien_da_o_quita_permiso''signo''permiso' 'nombre_del_archivo' `
# 
# A quien da o quita el permiso: `u`: usuario;`g`: grupo; `o`: otros; `a`: todos.
# 
# Signo: `+` para dar el permiso y `-` para quitarlo.
# 
# Permisos: `r`, `w` y `x` como antes.
# 
# `chmod o-w testfile.txt`
# 
# Le quita el permiso de escribir a los demás.
# 
# 
# **Para cambiar el nombre de un archivo**, el comando `mv` (*move*) nos permite realizar esta acción, `mv testfile.txt arprueba.txt`.
# 
# 
# **Para hacer una copia del archivo**, empleamos el comando `cp` (*copy*), por ejemplo, `cp arprueba.txt f1.txt`
# 
# **Para ver el contenido de un archivo**, empleamos el comando `cat`, `cat f1.txt` debe mostrar el contenido que ingresamos en el primer archivo.
# 
# En *bash* (*OS X*, *Linux* y *Git*) podemos concatenar archivos, con el comando anterior y guardar esa información en un tercer archivo, por ejemplo `cat arprueba.txt f1.txt > 2.txt.
# `
# 
# **Para copiar múltiples archivos**, el comando `cp` sirve nuevamente, si queremos copiar todos los archivos del tipo `.txt` podemos ejecutar la siguiente línea, `cp ruta-origen\*.txt ruta-destino`
# 
# **Para bortar un archivo**, usamos el comando `rm` (*remove*) así: `rm 2.txt`. Si quieremos **borrar la carpeta de prueba** completamente, haremos lo siguiente:
# 
# `cd..`
# 
# `rm prueba`
# 
# **Para limpiar el espacio de trabajo**, empleamos el comando `clear`.
# 
# Ahora debes ir al directorio en el cual está alojado este cuaderno:
# 
# `cd ubicación`
# 
# Allí, utilizaremos el comando `grep`, **para buscar contenido en un archivo**, para este ejemplo, buscaremos en este cuaderno, así:
# 
# `grep 'para' Consola.ipynb`
# 
# Esto nos arrojará las líneas en las cuales tenemos escrito la palabra 'para' en el archivo.
# 
# El comando `grep 'Para' Consola.ipynb` buscará las ocurrencias de la palabra 'Para' en el documento.
# 
# Mientras que, el comando `grep -i 'para' Consola.ipynb` buscará las ocurrencias de la palabra 'para', sin importar la coincidencia de las mayúsculas en el documento.
# 
# Las otras opciones del comando son:
# * **-c**: Muestra el número de líneas que coinciden con la palabra buscada.
# * **-n**: Muestra las ocurrencias de la palabra buscada en el documento y las antecede del número de la línea en la que está el documento.
# * **-v**: Muestra las líneas que no coinciden con la palabra buscada. 
# 
# **Para buscar un archivo**, lo podemos hacer por muchas opciones, dentro de las más comunes encontramos el tipo, el nombre y el tiempo, y el comando que emplearemos con ello es:  `find`. Para buscar por el tipo de fichero tenemos las opciones:
# * `b` block.
# * `c` character.
# * `d` directory.
# * `p` llamados pipe (FIFO).
# * `f` archivos regulares.
# * `s` socket.
# 
# `find -type f` Buscará todos los archivos que tengamos en nuestra carpeta.
# 
# Para buscar por contenido en el nombre, por ejemplo, buscar todos los cuadernos de python que tengamos en nuestra carpeta, empleamos el comando:
# 
# `find -name '*.ipynb'`
# 
# 
# Para buscar los archivos que han sido accedidos durante las últimas $n\times 24$ horas, empleamos el comando `find -atime n`, donde $n$ representa:
# 
# * +7 = hace más de 7 días.
# * 2 = entre 2 y 3 días.
# * -2 = dentro de los últimos 2 días.
# * +1 = hace más de un día.
# * 1 = entre 1 y 2 días.
# * -1 = dentro del último día.
# * 0 = dentro del último día.
# 
# `find -atime 0`
# 
# Para buscar los archivos que han cambiado durante las últimas $n\times 24$ horas, empleamos el comando `find -ctime n`, donde $n$ representa los mismos tiempos de **-atime**
# 
# `find -ctime 0`
# 
# Si queremos ver el historial de nuestra consola de comandos, podemos emplear el comando `history`.

# In[ ]:




