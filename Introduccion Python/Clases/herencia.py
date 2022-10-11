class Mascota:

    def comer(self):
        print('La mascota duerme')

    def dormir(self):
        print('La mascota duerme')

class Perro(Mascota):
    pass

duke = Perro()

duke.comer()
duke.dormir()