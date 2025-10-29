# Ejercicio 1
class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo      # Guardamos el título del libro
        self.autor = autor        # Guardamos el autor del libro

    def presentar(self):
        print(f"'{self.titulo}' escrito por {self.autor}")

# Creamos una instancia
libro1 = Libro("Cien años de soledad", "Gabriel García Márquez")

# Llamamos al método
libro1.presentar()

# Ejercicio 2

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.paginas_leidas = 0   # Comienza en 0

    def presentar(self):
        print(f"'{self.titulo}' escrito por {self.autor}")

    def leer(self, paginas):
        self.paginas_leidas += paginas
        print(f"Llevas leídas {self.paginas_leidas} páginas.")

    def reiniciar(self):
        self.paginas_leidas = 0
        print("Progreso reiniciado.")

# Probamos
libro2 = Libro("El Hobbit", "J.R.R. Tolkien")
libro2.leer(20)
libro2.leer(15)
libro2.reiniciar()


# Ejercicio 3

class Biblioteca:
    total_libros = 0  # Atributo de clase

    @classmethod
    def mostrar_total(cls):
        print(f"Total de libros: {cls.total_libros}")

class Libro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        Biblioteca.total_libros += 1  # Cada vez que se crea un libro, aumentamos el contador

# Creamos libros
l1 = Libro("1984", "George Orwell")
l2 = Libro("Hamlet", "William Shakespeare")
l3 = Libro("Don Quijote", "Miguel de Cervantes")

# Mostramos total
Biblioteca.mostrar_total()

# Ejercicio 4

class Libro:
    @staticmethod
    def es_bestseller(paginas):
        return paginas > 300

# Llamado desde la clase
print(Libro.es_bestseller(350))  # True

# Llamado desde una instancia
lib = Libro()
print(lib.es_bestseller(200))     # False

# Ejercicio 5

class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.__isbn = isbn       # Atributo privado

    def ver_isbn(self):
        return self.__isbn

libro = Libro("Dune", "Frank Herbert", "123-456-789")

# Acceso directo (no funciona porque es privado)
# print(libro.__isbn)  # Descomenta y verás un error

# Acceso correcto
print(libro.ver_isbn())

# Ejercicio 6

class Animal:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("El animal hace un sonido")

class Perro(Animal):
    def hablar(self):
        print("El perro ladra")

toby = Perro("Toby")
toby.hablar()


# Ejercicio 7

class Gato(Animal):
    def __init__(self, nombre, raza):
        super().__init__(nombre)  # Llamamos al constructor de Animal
        self.raza = raza

    def detalle(self):
        print(f"Nombre: {self.nombre}, Raza: {self.raza}")

misu = Gato("Misu", "Persa")
misu.detalle()


# Ejercicio 8

animales = [Animal("Bicho"), Perro("Firulais"), Gato("Luna", "Siames")]

for animal in animales:
    animal.hablar()   # Cada uno responde diferente


# Ejercicio 9

class Alumno:
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

class Curso:
    def __init__(self):
        self.alumnos = []

    def agregar(self, alumno):
        self.alumnos.append(alumno)

    def aprobados(self):
        return [alumno.nombre for alumno in self.alumnos if alumno.nota >= 5]

curso = Curso()
curso.agregar(Alumno("Lucía", 7))
curso.agregar(Alumno("Mario", 4))
curso.agregar(Alumno("Ana", 9))

print("Aprobados:", curso.aprobados())

# Ejercicio 10

class CuentaBancaria:
    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo

    def depositar(self, cantidad):
        self.saldo += cantidad

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
        else:
            print("Saldo insuficiente")

class CuentaAhorro(CuentaBancaria):
    def __init__(self, titular, saldo=0, interes=0.02):
        super().__init__(titular, saldo)
        self.interes = interes

    def aplicar_interes(self):
        self.saldo += self.saldo * self.interes

# Probamos
c1 = CuentaBancaria("Juan", 1000)
c2 = CuentaAhorro("Sara", 2000, 0.05)

c1.depositar(500)
c1.retirar(300)

c2.depositar(1000)
c2.aplicar_interes()

print(f"{c1.titular} saldo final: {c1.saldo}")
print(f"{c2.titular} saldo final: {c2.saldo}")
