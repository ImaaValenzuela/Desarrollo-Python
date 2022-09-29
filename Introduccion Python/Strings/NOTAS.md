# Strings
Notas sobre strings.

- [StringsConListado](/Introduccion%20Python/Strings/strings.py) : Para hacer una lista con string, usaremos la funcion "split", esta generara una lista con elementos determinados por cada espacio que haya en el string. Si queremos separarlos con algun caracter especifico, pasaremos como argumento ese caracter, ejemplo, split('-'). Tambien podemos utilizar como segundo argumento, las veces que queremos dividir el string; split('-', 2), esto nos daria una lista de dos elementos individuales y uno colectivo. Por otro lado, podemos generar un string a partir de una lista. Para esto usaremos la funcion "join()", pasaremos como argumento la lista.


- [Concatenar1](/Introduccion%20Python/Strings/concatenar.py) : Formas de concatenar, con el "+" o con "%s".


- [Concatenar2](/Introduccion%20Python/Strings/concatenar.py) : Mas formas de concatenar, placeholder "{}" y "format()", pasando como argumento los strings. Tambien podemos pasar parametros en los placeholder


- [FString](/Introduccion%20Python/Strings/concatenar.py) :  Un FString te permite interpolar elementos


- [FuncionPrint](/Introduccion%20Python/Strings/imprimir.py) : Con funcion print() podemos concatenar elementos, con el "sep=" podemos seleccionar el valor que separe los strings-


- [ValidarSubStrings](/Introduccion%20Python/Strings/busqueda.py) : Para conocer si un string se encuentra dentro de otro string, existen varias formas. Esta el metodo ".count", que nos dice cuantas veces aparece el substring o caracter. Despues el "in" o "not in", lo cual nos devuelve un boolean. Y por ultimo, los metodos "startwith" y "endwith", los cuales nos retornan un booleano. Nos sirve para corroborar con que palabra empieza o termina el string-

- [JustificarTexto](/Introduccion%20Python/Strings/alineacion.py) : Existen tres metodos que nos permitiran justificar texto, "ljust" el cual nos justifica el texto a la izquierda, "rjust" que nos justifica el texto a la derecha y "center" que lo centra. Estos metodos no modifican al string original, genera uno nuevo.