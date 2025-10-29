# Ejercicio 1 – Función simple
def saludar():
    print("¡Hola, mundo!")

saludar()
print()


# Ejercicio 2 – Parámetros y argumentos
def saludo_personal(nombre):
    print(f"¡Hola, {nombre}!")

saludo_personal("Ana")
saludo_personal("Carlos")
print()


# Ejercicio 3 – Valor de retorno
def area_rectangulo(base, altura):
    return base * altura

print("Área del rectángulo:", area_rectangulo(5, 3))
print()


# Ejercicio 4 – Valores por defecto
def potencia(base, exponente=2):
    return base ** exponente

print("5 al cuadrado:", potencia(5))
print("2 al cubo:", potencia(2, 3))
print()


# Ejercicio 5 – Funciones con múltiples retornos
def analisis_lista(numeros):
    maximo = max(numeros)
    minimo = min(numeros)
    promedio = sum(numeros) / len(numeros)
    return [maximo, minimo, promedio]

resultado = analisis_lista([5, 2, 8, 3, 9])
print("Análisis de la lista [5, 2, 8, 3, 9]:", resultado)
print()


# Ejercicio 6 - Funciones anidadas
def operaciones(a, b):
    def suma():
        return a + b

    def resta():
        return a - b

    def multiplicacion():
        return a * b

    return {
        "suma": suma(),
        "resta": resta(),
        "multiplicacion": multiplicacion()
    }

print("Operaciones con 5 y 2:", operaciones(5, 2))
print()


# Ejercicio 7 - Funciones recursivas
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print("Factorial de 5:", factorial(5))
print()


# Ejercicio 8 - Llamar una función desde otra
def cuadrado(n):
    return n ** 2

def doble_cuadrado(n):
    return 2 * cuadrado(n)

print("Cuadrado de 4:", cuadrado(4))
print("Doble del cuadrado de 4:", doble_cuadrado(4))
print()


# Ejercicio 9 - Contador de vocales
def contar_vocales(texto):
    contador = 0
    for letra in texto.lower():
        if letra in "aeiou":
            contador += 1
    return contador

print("Ejercicio 9 - Contador de vocales")
while True:
    frase = input("Escribe una frase (o 'fin' para salir): ")
    if frase.lower() == "fin":
        break
    print("Número de vocales:", contar_vocales(frase))
print()


# Ejercicio 10 - Adivina el número
import random

def comprobar_intento(secreto, intento):
    if intento < secreto:
        return "mayor"
    elif intento > secreto:
        return "menor"
    else:
        return "acertaste"

print("Ejercicio 10 - Adivina el número")
secreto = random.randint(1, 20)
intentos = 0

while intentos < 4:
    intento = int(input("Adivina el número (1-20): "))
    resultado = comprobar_intento(secreto, intento)
    if resultado == "acertaste":
        print("¡Correcto! Has adivinado el número.")
        break
    else:
        print("El número secreto es", resultado)
        intentos += 1

if intentos == 4 and resultado != "acertaste":
    print(f"Has perdido. El número era {secreto}.")
print()


# Ejercicio 11 - Ejemplo de POO
class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b != 0:
            return a / b
        else:
            return "Error: división entre cero"

calc = Calculadora()
print("Suma:", calc.sumar(5, 3))
print("Resta:", calc.restar(5, 3))
print("Multiplicación:", calc.multiplicar(5, 3))
print("División:", calc.dividir(5, 0))
print()


# Ejercicio 12 - Ejemplo de funcional

# Parte 1: aplicar_funcion()
def aplicar_funcion(lista, funcion):
    nueva_lista = []
    for elemento in lista:
        nueva_lista.append(funcion(elemento))
    return nueva_lista

# Funciones de ejemplo
def sumar_uno(x):
    return x + 1

def restar_uno(x):
    return x - 1

def duplicar(x):
    return x * 2

def dividir_por_dos(x):
    return x / 2

# Parte 2: reutilizar la función
valores = [1, 2, 3, 4]
print("Original:", valores)
print("Sumar uno:", aplicar_funcion(valores, sumar_uno))
print("Restar uno:", aplicar_funcion(valores, restar_uno))
print("Duplicar:", aplicar_funcion(valores, duplicar))
print("Dividir por dos:", aplicar_funcion(valores, dividir_por_dos))
print()

# Parte 3: composición de funciones
def componer(f, g):
    def nueva_funcion(x):
        return f(g(x))
    return nueva_funcion

# Ejemplo de composición: duplicar luego sumar uno
f = componer(sumar_uno, duplicar)
print("Composición (duplicar y luego sumar 1):")
print(aplicar_funcion(valores, f))
print()
