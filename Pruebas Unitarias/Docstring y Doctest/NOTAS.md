# Docstring y Doctest

- [Comentarios]() : Existen tres formas de comentar nuestro codigo, con " # ", que nos permite comentar una sola linea, o con " """ || ''' " triples comillas dobles o simples, que nos permite comentar varias lineas de codigo.


- [Docstring](docstring.py) : Los comentarios del docstring deben cumplir con un par de puntos, el primero, es que en la primer linea del comentario vamos a colocar una descripcion del funcionamiento de nuestro codigo. Posteriormente hay que definir los objetos con los cuales se trabaja. El contenido de este comentario se encontrara en la funcion "__doc __" o "help()" que recibira como argumentos la funcion de la cual queremos conocer la documentacion.


- [Formato Doctring]() : NO hay un formato correcto o incorrecto al comentar nuestro codigo, pero el formato que se recomienda es el propuesto por google.


- [Modulo Doctest]() : Para probar si nuestra funcion se ejecuta correctamente vamos a usar el prefjo ">>>" seguido cocn la sentencia y en una nueva linea el objeto que en teoria se va a obtener despues de ejecutar la sentencia. Luego con ayuda de la terminal usaremos "python -m doctest (nombre del archivo py que deseemos testear)".


- [Objetos Documentables](documentar.py) : Los objetos documentables no son mas que objetos los cuales nosotros podemos documentar a traves del docstring. Los objetos documentables son funciones, clases, metodos y modulos, todos estos poseen __doc __.


- [Prueba en archivos externos]() : El modulo doctest no es un framework de testing. Se recomienda separar la documentacion del codigo necesario para poder llevar a cabo los casos de prueba.

