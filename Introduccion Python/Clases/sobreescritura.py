class Animal:
    def comer(self):
        print('El animal come')

    def dormir(self):
        print('El animal duerme')


class Mascota:
    pass


class Felino:

    def caza(self):
        print('El felino caza')

class Gato(Mascota):
    
    def __init__(self, nombre):
        self.nombre = nombre

    def comer(self):
        super().comer()
        print(f'{self.nombre} come')
    
    def dormir(self):
        print(f'{self.nombre} duerme')

rober = Gato('Rober')

rober.comer()
rober.dormir()

rober.caza()