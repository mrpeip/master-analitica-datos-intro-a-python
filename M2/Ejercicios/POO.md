## Ejercicio 1: Clase básica y método simple

Crea una clase Libro con atributos titulo y autor.

    Agrega un método presentar() que imprima "'{titulo}' escrito por {autor}'".
    
    Crea una instancia y llama al método presentar().

## Ejercicio 2: Métodos de instancia con cálculo

Agrega un atributo paginas_leidas inicializado en 0.

    Crea métodos leer(paginas) y reiniciar() que aumenten o reinicien las páginas leídas, e impriman el estado.

    Crea una instancia y simula la lectura de varias páginas.

## Ejercicio 3: Atributos de clase y métodos de clase

Crea una clase Biblioteca con atributo de clase total_libros que cuente cuántos libros se han agregado.

    Agrega un método de clase mostrar_total() que imprima el total de libros.
    Crea varias instancias de Libro y llama al método de clase desde Biblioteca.

## Ejercicio 4: Métodos estáticos

    Crea un método estático es_bestseller(paginas) que devuelva True si el libro tiene más de 300 páginas, y False en caso contrario.

    Llama al método desde la clase y desde una instancia.

## Ejercicio 5: Encapsulamiento de atributos

    Haz que el atributo isbn de la clase Libro sea privado (__isbn).

    Agrega un método ver_isbn() que devuelva su valor.

    Prueba acceder directamente al atributo (debe fallar) y a través del método (debe funcionar).

## Ejercicio 6: Herencia básica

Crea una clase Animal con atributo nombre y método hablar() que imprima "El animal hace un sonido".

    Crea una subclase Perro que sobrescriba hablar() para imprimir "El perro ladra".

    Crea una instancia de Perro y llama al método hablar().

## Ejercicio 7: Herencia con constructor y super()

Crea una subclase Gato que herede de Animal, agregue un atributo raza, y use super().__init__() para inicializar el nombre.

    Agrega un método detalle() que imprima nombre y raza.

    Crea una instancia de Gato y llama a detalle().

## Ejercicio 8: Polimorfismo
    Crea una lista con objetos de tipo Animal, Perro y Gato.

    Recorre la lista y llama al método hablar() de cada objeto, demostrando que el mismo método se comporta diferente según la instancia.

## Ejercicio 9: Interacción entre objetos

Crea una clase Alumno con atributos nombre y nota.

    Crea una clase Curso que tenga una lista alumnos y un método aprobados() que devuelva los nombres de los alumnos con nota mayor o igual a 5.

    Crea varias instancias de Alumno, agrégalas a un Curso y muestra los aprobados.

## Ejercicio 10: El banco

    Crea una clase CuentaBancaria con atributos titular y saldo y métodos depositar(cantidad) y retirar(cantidad).

    Crea una subclase CuentaAhorro que agregue un atributo interes y un método aplicar_interes() que aumente el saldo según el interés.

    Crea varias instancias, realiza depósitos y retiros, aplica interés y muestra el saldo final de cada cuenta.