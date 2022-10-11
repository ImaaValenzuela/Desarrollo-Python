animal = 'Leon'
tipo = 'mamifero'

def imprimir_animal():
    animal = 'Ballena'

    global tipo

    tipo = 'Mamifero'

    print(animal)
    print(id(animal))
    print(tipo)
    print(id(tipo))

imprimir_animal()

print(animal)
print(id(animal))
print(tipo)
print(id(tipo))