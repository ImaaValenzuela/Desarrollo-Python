def usuaros(**kwargs):
    print(kwargs)

usuaros(eduardo=[10,9,5], fernando=[8,7,10])


def combinacion (*args, **kwargs):
    print(args)
    print(kwargs)

combinacion(1,2,3,4,5, nombre=True, curso='Python')