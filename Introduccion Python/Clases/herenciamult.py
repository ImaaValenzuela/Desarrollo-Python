class Mascota:

    def comer(self):
        print('La mascota duerme')

    def dormir(self):
        print('La mascota duerme')

class Felino:

    def caza(self):
        print('El felino caza')

class Gato(Mascota):
    pass

rober = Gato()

rober.comer()
rober.dormir()

rober.caza()