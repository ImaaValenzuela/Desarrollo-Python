def funcion_principal ():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c'

        nonlocal b
        b = 'cambio de valor'

        print(a)
        print(b)
        print(id(b))
    
    funcion_anidada()
    print(b)
    print(id(b))

funcion_principal()