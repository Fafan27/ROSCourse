# [Tarea 1 - Programación en Python y control de versiones en GIT/GitHub)] 


| Código | Description |
| ------:| ----------- |
| ***Asignatura*** | Curso ROS | 
| **Curso ROS** | Tarea *01* |



## Contenido

- [Objetivo](#objetivo)
- [Introducción](#introduccion)
- [Desarrollo](#desarrollo)
- [Conclusiones](#conclusiones)
- [Autor](#autor)
- [Referencias](#referencias)

## Objetivo

Desarrollar las capacidades necesarias para la programación de robots en ROS Noetic.

## Introducción

Se crearau progrma de python con las caracteristicas propias de un Robot con 5 grados de libertad,
además, se guiará en el uso y práctica de los repositorios de GitHub. 


## Desarrollo

**Actividades**

Generar un repositorio en su cuenta personal de GitHub

Subir un programa de Python con las siguientes caracter´sitcas:

- Un clase llamada **Robot**
- Un **arreglo** de **cadenas** representando el **nombre de cada artiuculación.**
- Un **arreglo** de **flotantes** representando el **valor de cada articulación.**
- Una **cadena** con el **nombre** del robot.
- Una variable a un objeto llamado **Pose** que represente la pose del robot con los valores 
**x** (posición en x), **y** (posición en y), **z** (posición en z), **rxr** (rotación en x en radianes), 
**ryr** (rotacion en y en radianes), **rzr** (rotación en z radianes).
- Todas las variables deben ser **inicializadas** con valores en el **constructor** para un 
manipulador de **5 grados** de libertad más uno más llamado **base** (eslabón 0).
- Un método llamado **set_name(robot_name)** para cambiar el nombre del robor.
- Un método llamado **get_articulacion(articulacion_nombre)** que devuelva el valor de la articulación **articulación_nombre**

## Conclusiones

Conclusiones o cierre al trabajo realizado.

Lorem ipsum dolor sit amet, consetetur sadipscing elitr, sed diam nonumy eirmod
tempor invidunt ut labore et dolore magna aliquyam erat, sed diam voluptua. At
vero eos et accusam et justo duo dolores et ea rebum. Stet clita kasd gubergren,
no sea takimata sanctus est Lorem ipsum dolor sit amet [[3]](#3). **<- referencia insertada en el párrafo** . 

## Autor

***[Nombre del autor o listado de los integrantes del equipo]***

**Autor** Felipe Rivas Campos [GitHub profile](https://github.com/rivascf)

o en caso de tratarse de un equipo

| Iniciales  | Description |
| ----------:| ----------- |
| **RICF** | Felipe Rivas Campos [GitHub profile](https://github.com/rivascf) |
| **EPM**  | Erik Peña Medina [GitHub profile](https://github.com/ErikFiUNAM) |
| **MGR-MX** | Mechatronics Research Group, México [GitHub profile](https://github.com/mrg-mx) |

## Referencias

_Referencia simple_

<a id="1">[1]</a>  I.A. Glover and P.M. Grant, Digital Communications, 3rd ed.  Harlow: Prentice Hall, 2009. 

_Referencia con vínculo insertado en el título del libro_

<a id='2'>[2]</a>	J. B. Kuipers, [Quaternions and rotation sequences](https://amzn.to/2RY2lwI). Princeton, NJ: Princeton University Press, 2002. (Chapter 5,  Section 5.14 “Quaternions to Matrices”, pg. 125)

_Referencia con url externo visible_

<a id="3">[3]</a>  H.-L. Pham, V. Perdereau, B. Adorno, en P. Fraisse, “Position and Orientation Control of Robot Manipulators Using Dual Quaternion Feedback”, 11 2010, bll 658–663. <https://www.researchgate.net/publication/224200087_Position_and_Orientation_Control_of_Robot_Manipulators_Using_Dual_Quaternion_Feedback>

**Nota**:

> Listado de referencias documentales consultadas para realizar el trabajo:
> consultar el siguiente [vínculo](https://www.bath.ac.uk/publications/library-guides-to-citing-referencing/attachments/ieee-style-guide.pdf)
> para el formato de referencia estilo **IEEE**.
> 
> ```text
> [Num ref] Iniciales del autor. Apellido del autor, Título del libro, edicion (si no es la primera). 
> Lugar de publicación: Publicador, Año.
> ```