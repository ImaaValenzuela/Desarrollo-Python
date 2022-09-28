# Listas
Notas sobre listas

- [¿QueSonLasListas?](/Introduccion%20Python/Listas/introduccionListas.py) : Las listas on estrucuturas de datos. Hay dos formas de trabajar con listas, con la funcion "list()" o con al declarar la variable, darle el valor = "[]". A cada valor de la lista le corresponde un indice, estos indices comienzan desde el 0.

- [Listas](/Introduccion%20Python/Listas/listas.py) : Mediante un indice seremos capaces de de obtener y/o actualizar elementos dentros de una lista.


- [ActualizarElementos](/Introduccion%20Python/Listas/) : Para actualizar un elemento de una lista nos apoyaremos en el index que posee. 


- [Sublistas](/Introduccion%20Python/Listas/listas.py) : Si queremos crear una sublista con elementos que tenemos en una lista pasaremos los indices correspondientes; Es importante saber que el indice final no sera tomado en cuenta para esta sublista, ejemplo, [0 : 3], incluira los elementos, 0, 1 y 2. Si omitimos el indice final, obtenemos los ultimos elementos de la lista , ejemplo, [0 :], incluira los elementos, 0, 1, 2 ,3. Si omitimos el indice inicial, obtendremos los primeros elemntos de la lista sin el indice final, ejemplo, [: 3], obtendremos, 0, 1, 2. Tambien podemos crear una lista que omita elementos, por ejemplo, [1: 5: 2], obtendremos 1 y 3.


- [ModificarListas](/Introduccion%20Python/Listas/listas.py) : Para añadir un elemento al final de una lista usaremos la funcion "append()", en esta pasaremos como parametro el nuevo elemento. Para conocer la longitud de una lista usaremos la funcion "len()". Para agregar un elemento en la posicion que deseemos, usaremos "insert()", pasaremos dos parametros, el indice que ocupara este nuevo elemento , y el nuevo elemento. Tambien podemos extender aun mas la lista conla funcion "extend()", para esto crearemos una nueva lista y la pasaremos como parametro. Para eliminar un elemento usaremos "remove()", pasando como argumento el elemneto que deseamos eliminar. Para eliminarlos mediante el indice, usaremos "del". Por ultimo esta "clear", esta funcion elimina a todos los elementos de la lista.


- [MetodosDeListas](/Introduccion%20Python/Listas/listas.py) : Podemos ordenar una lista de forma ascendente usando la funcion "sort()" ,y descendente "sort(reverse)". Para conocer los maximos y minimos, usaremos "min" y "max". Tambien podemos corroborar si un elemento esta en la lista usando la palabra reservada "in", elemento in lista?, devuelve un booleano True o False. Tambien podemos hacerlo usando un operador logico, "not", elemento not in lista?, devolviendo booleano.


- [Index](/Introduccion%20Python/Listas/listas.py) : Para conocer el indice de un elemento, usaremos "index", esto nos retorna su primer indice con dicho valor. Es importante que antes de buscar el index de un elemento, usemos in para confirmar que dicho elemento se encuentra en el listado.


- [Matrices](/Introduccion%20Python/Listas/matrices.py) : Una matriz es un conjunto de numeros ordenados en filas y/o columnas Utilizando listas seremos capaces de trabajar con matrices de una forma sencilla.




