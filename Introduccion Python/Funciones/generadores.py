def pares():
    for numero in range(0, 100, 2):
        yield numero

        print('Se reanuda la ejecucion')

for par in pares():
    print(par)