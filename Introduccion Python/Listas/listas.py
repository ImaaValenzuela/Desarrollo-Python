lista_cursos = ['Python', 'Django', 'Flask', 'Ruby', 'Java', 'Rust']

lista_cursos_2 = ['C', 'C++', 'Docker']

primer_curso = lista_cursos[0]

segundo_curso = lista_cursos[1]

ultimo_curso = lista_cursos [3]

lista_cursos[3] = 'Rails'

sub_lista = lista_cursos[0:2]

lista_cursos.append('MongoDB')

lista_cursos_2.append('C#')

lista_cursos.insert(0, 'Pygame')

lista_cursos.extend(lista_cursos_2)

print(len(lista_cursos))

print(lista_cursos)

lista_cursos.remove('MongoDB')

del lista_cursos [0]

print(lista_cursos)

lista_precios = [100, 69, 260, 80, 20, 430]

lista_precios.sort()

print(lista_precios)

lista_precios.sort(reverse=True)

print(lista_precios)

print(min(lista_precios))

print(max(lista_precios))

print(17 in lista_precios)

print(260 in lista_precios)

print(lista_precios.index(260))

print(100 not in lista_precios)

index = lista_precios.index(100)

print(index)