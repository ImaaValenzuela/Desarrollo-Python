nombre = 'Imanol'

segundo_nombre = 'Itzan'

nombres = nombre + segundo_nombre

apellido = 'Valenzuela'

segundo_apellido = 'Eguez'

apellidos = '%s %s' %(apellido, segundo_apellido)

pais = 'Argentina'

provincia = 'Buenos Aires'

residencia = '{}, {}, {localidad}'.format(
    pais, 
    provincia, 
    localidad = 'Capital Federal'
)


nombre_completo = f'{nombre} {apellido}'