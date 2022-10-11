def saludar(username):
    mensaje = f'Hola {username}'

    def mostrar_mensaje():
        print(mensaje)
    
    return mostrar_mensaje

username = 'Kotaro'

respuesta = saludar(username)