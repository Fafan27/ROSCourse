#!/usr/bin/env python

class Robot:
    def datos(articulaciones, valor_articulaciones): 
        art = int(input("Cantidad de articulaciones: "))
        for i in range(art):
            print("Ingre el nombre de la articulación", i+1)
            articulacion = input()
            articulaciones.append(articulacion)
        for i in range(art):
            print("Ingresa el valor de la articulación", i+1)
            va_art = input()
            valor_articulaciones.append(va_art)
    def get_pose(pose):
        vp = ["posición en x","posición en y","posición en z","rotacion en x (en radianes)","rotacion en y (en radianes)","rotacion en z (en radianes)"]
        for i in range(len(vp)):
            print("Ingresa el valor de la", vp[i])
            valorp = input()
            pose.append(valorp)
        for i in range(len(vp)):
            print(f"{vp[i]} {valorp}")
    def set_name(robot_name):
        robot_name= input("Nombre del robot:")
        print(f"Nuevo nombre del robot: {robot_name}")
    def get_articulacion(articulaciones, valor_articulaciones):
        busqueda=input("¿De qué articulación quieres conocer el valor? ")
        indice_busqueda = -1
        for i in range(len(articulaciones)):
            if articulaciones[i] == busqueda:
                indice_busqueda = i
                break
        if indice_busqueda == -1:
            print("Nombre de articulación no encontrada")
        else:
            print(f"EL valor de la articulación {busqueda} es: {valor_articulaciones[indice_busqueda]}")
    def main (articulaciones, valor_articulaciones, robot_name, pose):
        art = int(input("Cantidad de articulaciones: "))
        for i in range(art):
            print("Ingre el nombre de la articulación", i+1)
            articulacion = input()
            articulaciones.append(articulacion)
        for i in range(art):
            print("Ingresa el valor de la articulación", i+1)
            va_art = input()
            valor_articulaciones.append(va_art)
        robot_name= input("Nombre del robot:")
        print(f"Nuevo nombre del robot: {robot_name}")
        vp = ["posición en x","posición en y","posición en z","rotacion en x (en radianes)","rotacion en y (en radianes)","rotacion en z (en radianes)"]
        for i in range(len(vp)):
            print("Ingresa el valor de la", vp[i])
            valorp = input()
            pose.append(valorp)
        for i in range(len(vp)):
            print(f"{vp[i]} {valorp}")
bandera = True
datos_listos = False
robot_name = []
articulaciones = []
valor_articulaciones : float = []
pose = []
while bandera == True:
    print("Bienvenido al programa")
    print("1. Ingresar datos del robot")
    print("2. Asginar nombre al robot")
    print("3. Obtener el valor de una articulación")
    print("4. Obtener los valores de la pose")
    print("5. Salir")
    print("__main__")
    __name__ = input("Introduzca la opción deseada: ")
    if __name__ == "1":
        print("****Ingreso de datos****")
        Robot.datos(articulaciones, valor_articulaciones)
        datos_listos = True
        print(articulaciones)
        print(valor_articulaciones)
        input("Oprima la tecla enter para continuar")
    elif datos_listos == False and __name__ != "__main__":
        print("Por favor, primero ingrese los datos del robot")
        input("Oprima la tecla enter para continuar")
    elif __name__ == "2":
        Robot.set_name(robot_name)
        input("Oprima la tecla enter para continuar")
    elif __name__ == "3":
        Robot.get_articulacion(articulaciones, valor_articulaciones)
        input("Oprima la tecla enter para continuar")
    elif __name__ == "4":
        Robot.get_pose(pose)
        input("Oprima la tecla enter para continuar")
    elif __name__ == "5":
        print("Hasta luego")
        bandera = False
    elif __name__ == "__main__":
        Robot.main(articulaciones,valor_articulaciones,robot_name,pose)
        input("Oprima la tecla enter para continuar")
    else:
        print("Seleccione una opción válida")
        input("Oprima la tecla enter para continuar")
