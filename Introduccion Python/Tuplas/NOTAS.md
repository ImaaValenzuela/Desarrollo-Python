# Tuplas
Notas sobre tuplas

- [¿QueSonLasTuplas](/Introduccion%20Python/Tuplas/tuplas.py) : Las tuplas nos permiten almacenar diferentes tipos de datos. Los elementos almacenados dentro de estas no se pueden modificar. Estas se declaran con "()".

- [IndiceDeTuplas](/Introduccion%20Python/Tuplas/tuplas.py) :  A cada elemento de las tuplas les corresponde un indice, este empieza desde 0. Tambien podremos crear una subtupla. indicando indice inicial y final, el indice final no es tomado en cuenta.

- [ListasyTuplas](/Introduccion%20Python/Tuplas/listas.py) : Cuando nosotros no sepamos la cantidad de elementos que debemos almacenar y/o sepamos que su valor puede variar, usaremos listas. En caso contrario, si sabemos que nuestros elementos no van a cambiar y queremos que se conserven asi el resto del programa, haremos uso de las tuplas. Para pasar de tupla a lista o lista  tupla hay dos funciones. Si queremos generar una nueva lista desde una tupla, usaremos "list()" y pasaremos como argumento la tupla. En caso viceversa, usaremos "tuple()" y como argumento pasaremos la lista.


- [Desempaquetado](/Introduccion%20Python/Tuplas/descomprimir.py) : Las tuplas se pueden desenpaquetar, descomprimir y asignar sus valores a variables. El "*" se usa como prefijo, al momento de descomprimir, si colocamos este prefijo, se asignara esta variable en formato de lista, ya que estos valores no fueron desenpaquetados. Si no queremos incluir el resto de valores en una variable, indicaremos " *_". Para omitir un solo valor, " _"


- [Zip](/Introduccion%20Python/Tuplas/comprimir.py) : Para almacenar variables se puede usar "zip()", nos retornara un elemento tipo zip. Cuando lo convirtamos en tupla, se formaran subtuplas. La combinacion para comprimir debe ser exacta, si una variable posee mas elementos, estos no seran tomados en cuenta. 