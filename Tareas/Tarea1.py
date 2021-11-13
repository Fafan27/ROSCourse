class Robot:
    robot_name = "robot_name"
    def datos(self):
         articulaciones = []
         art = int(input("Cantidad de articulaciones: "))
         for i in range(art):
            print("Ingre el nombre de la articulación", i+1)
            articulacion = input()
            articulaciones.append(articulacion)
         print(articulaciones)
         valor_articulaciones: float = []
         for i in range(art):
             print("Ingresa el valor de la articulación", i+1)
             va_art = input()
             valor_articulaciones.append(va_art)
         print(valor_articulaciones)
         pose = []
         vp = ["posición en x","posición en y","posición en z","rotacion en x (en radianes)","rotacion en y (en radianes)","rotacion en z (en radianes)"]
         for i in range(len(vp)):
             print("Ingresa el valor de la", vp[i])
             valorp = input()
             pose.append(valorp)
         print(pose)
    def set_name(self):
        nombre = str(input("Nombre del robot"))
        self.robot_name.replace(nombre)
        print(self.robot_name)

Robot_generico = Robot()
Robot_generico.set_name()