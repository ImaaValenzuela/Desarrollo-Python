promedio = lambda *args : sum(args) / len(args)

aprobatorio = lambda calificacion : calificacion >= 7

def mostrar_mensaje(func_promedio, func_aprobatorio, *args):
    promedio = func_promedio(*args)

    if func_aprobatorio(promedio):
        print(f'Felicidades, aprobaste la materia con {promedio}')
    else:
        print(f' Tu promedio es de {promedio}, No aprobaste la materia')

mostrar_mensaje(promedio, aprobatorio, 10,8,5,7,4)