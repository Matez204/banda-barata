from musicos import *
import random
class Banda:
    def __init__(self):
        self.musicos=[]
        self.instrumentos =[Guitarra(),Piano(),Tiple()]
        self.amigos=["Juan","Miguel","Maria","Ana","Juana","Pedro"]

    def crear_banda(self,cantidad_musicos):
        for i in range (cantidad_musicos):
            self.musicos.append(Musico(random.choice(self.amigos)))
            self.musicos[-1].asignar_instrumento(random.choice(self.instrumentos))
        
    
    def mostrar_banda(self):
        print("Los integrantes de la banda son ")
        for m in self.musicos:
            print(m.nombre,end=" ")
            m.instrumento.mostrar()
           

cosa=Banda()
cosa.crear_banda(5)
cosa.mostrar_banda()