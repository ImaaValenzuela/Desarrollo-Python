# Clases
Notas sobre clases


- [Clases](clases.py) : Para crear una clase usaremos la palabra "class", el nombre de la clase tiene que ir en PascalCase.


- [Atributos de clase](attrsclase.py) : Basta con definir variables dentro de una clase para crear atributos de clase. Para usar estos atributos haremos uso del nombre de la clase.


- [Atributos de instancia](attrsinstancia.py) : Se pueden añadir de forma dinamica atributos a nuestros objetos en tiempop de ejecucion. Para nosotros lograr esto python trabaja con un meta atributo llamado "__dict __" , dentro de este atributo vamos a encontrar todops aquellos atributos que posea nuestro objeto.


- [Atributos dinamicos](attrdinamicos.py) : Para añadir valores de forma dinamica vamos a colocar el objeto, luego el atributo y por ultimo el valor que nosotros queramos almacenar.


- [Metodos](metodos.py) : Lo recomendable es que cuando nosotros creemos objetos de un mismo tipo de clase, estos objetos comiencen con los mismos atributos. Para poder crear metodos haremos uso de funciones dentro de las clases. Por convencion pasaremos como parametros "self".


- [Metodo init](metodoinit.py) : El metodo init nos permite estandarizar objetos de forma mas sencilla, para usarlo, definiremos una funcion con "__init __" y pasaremos como parametro "self". Este metodo nos permite tambien inicializar los objetos.


- [Herencia](herencia.py) : Para heredar usaremos el nombre de una clase padrey la pasaremos como parametro a la clase hija.


- [Herencia multiple](herenciamult.py) : Una clase puede heredar de multiples clases.


- [Sobre escritura de metodos](sobreescritura.py) : Una clase hija puede modificar una clase padre. Para sobre escribir un metodo basta con volverlo a definir.


- [Sobre escritura de metodos pt 2](sobreescritura.py) : La funcion "super" nos permite acceder a la clase padre inmediata la cual facilmente podemos utilizar para usar sus metodos.


- [Metodos de clase](metodosclase.py) : Para definir un metodo de clase a la funcion le pasaremos como parametro "cls". Para convertir un metodo de instancia a uno de clase decoraremos la funcion con @classmethod.


