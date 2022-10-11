# Funciones
Notas sobre funciones

- [Funciones](funciones.py) : Para definir una funcion usaremos def. Las funciones deben declararse en snakecase. Las funciones se pueden llamar las n de veces que nosotros querramos.


- [Argumentos](argumentos.py) : Los parametros nos permite usar variables. 


- [Retornar Valores](return.py) : return nos permite almacenar datos. Cuando se llega al return en una función, la función ya se da por terminada. Las funciones nos permiten retornar multiples valores, convirtiendo estos en una tupla.


- [Parametros Opcionales](parametros.py) : A diferencia de otros lenguajes los parametros pueden ser opcionales. Para definir un parametro no usaremos espacio. 


- [Args](args.py) : Para recibir la n cantidad de argumentos usaremos un "*" pegado a nuestro argumento, esto nos generaria una tupla. Todos estos parametros que tengan como prefijo asterisco, seran llamados args.


- [Args pt 2](args.py) : El uso de asteriscos no nos limita a usar parametros, nuestra funcion puede tener la n cantidad de parametros que querramos. Entre funcion y funcion tiene que haber dos espacios que los separe.  


- [Kwargs](kwargs.py) : Kwargs nos permite crear diccionarios, para etso usaremos "**" y definiremos el parametro como kwargs. 


- [Scopes](scope.py) : Hay dos tipos de variables, las variables globales, estas pueden ser utilizadas dentro de cualquier bloque. Por otro lado estan las variables locales, estas pueden ser utilizadas unicamente dentro del bloque en el que fueron creadas. Cada elemento posee un id unico, con la funcion "id", podemos verlo. Para modificar una variable global dentro de un bloque usaremos la funcion "global.


- [Funciones Anidadas](anidadas.py) : Las funciones pueden poseer otras funciones dentro.


- [Ciudadanos de primera clase](ciudadanos.py) : Las funciones pueden ser asignadas a variables, pueden ser utilizadas como argumentos de otras funciones, e inclusive funciones pueden retornar otras funciones.


- [Funciones Lambda](lambdas.py) : Las funciones lambdas o anonimas son funciones que son expresadas en una linea de codigo- No poseen un nombre. La funcion lambda no necesita la palabra reservada return, ya que siempre va a retornar la linea de codigo que sea ejecutada.


- [Callbacks](callbacks.py) : Son funciones las cuales son utilizadas como argumentos para otras funciones.


- [Variables no locales](nonlocals.py) : Las variables locales pueden ser utilizadas en bloques de codigo inferiores donde fueron creadas. Para modificar el valor de estas usaremos la funcion "nonlocal".


- [Retornar Funciones](returnfunc.py) : Funciones pueden ser asignadas a variables, funciones pueden ser utilizadas como argumentos y funciones pueden retornar otras funciones.


- [Closures](closures.py) : Los closures son funciones las cuales pueden generar de manera dinamica otra funcion y esta funcion puede acceder a variables locales aun cuando la primera alla finalizado.


- [Decoradores](decoradores.py) : Los decoradores tienen como objetivo poder extender funcionalidades a una funcion. Recibe como argumento una funcion y retorna otra funcion. Para decorar una funcion usaremos "@" seguido del nombre del decorador a utilizar. 


- [Decoradores pt 2](decoradores2.py)  


- [Generadores](generadores.py) : Es un tipo de funcion la cual retorna objetos que facilmente podremos iterar sin que la funcion finalice. Esto se hace con la palabra "yield".


- [Distribucion perezosa](lazyiterator.py) 


- [Documentar Funciones](documentar.py) : Lo recomendable es que siempre que creemos una funcion, la documentemos. Para documentar una funcion, usaremos "docstring", que no es mas que un comentario que se coloca en la primer linea de codigo dentro de una funcion. En python existen objetos documentables, estos son los modulos, las clases, los metodos y las funciones("__ doc __").


- [Testear Funciones](documentar.py) : Para testear funciones primero usaremos ">>>" y simularemos pasando parametros. Luego con ayuda de la terminal usaremos "python -m doctest (nopmbre del archivo py que deseemos testear)".


