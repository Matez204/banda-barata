
class instrumento:
    def afinar(self):
        pass
    def tocar(self):
        pass
    def mostrar(self):
        print(str(type(self)).split(".")[-1][:-2])
class Guitarra(instrumento):
    def afinar(self):
        print("Afinanfo guitarra")
    def tocar(self):
        print("Tocando guitarra")
class Piano(instrumento):
    def afinar(self):
        print("Afinanfo piano")
    def tocar(self):
        print("Tocando piano")
class Tiple(instrumento):
    def afinar(self):
        print("Afinanfo Tiple")
    def tocar(self):
        print("Tocando Tiple")

if __name__=="__main__":
    guitarra=Guitarra()
    print(str(type(guitarra)).split(".")[-1][:-2])