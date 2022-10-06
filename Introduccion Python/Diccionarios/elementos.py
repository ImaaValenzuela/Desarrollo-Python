diccionario = {'a':1 , 'b': 2, 'c': 3, 'd': 4}

print('z' in diccionario)

valor = diccionario['a']

print(valor)

valor2 = diccionario.get('g', "El elemento no se encuentra en el diccionario")

print(valor2)

valor3 = diccionario.setdefault('e', 5)

print(valor3)

print(diccionario)