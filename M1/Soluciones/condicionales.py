# Ejercicio 1 – Número positivo o negativo
numero = float(input("Ejercicio 1 - Introduce un número: "))
if numero > 0:
    print("El número es positivo")
elif numero < 0:
    print("El número es negativo")
else:
    print("El número es cero")
print()

# Ejercicio 2 – Mayor de edad
edad = int(input("Ejercicio 2 - Introduce tu edad: "))
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")
print()

# Ejercicio 3 – Par o impar
n = int(input("Ejercicio 3 - Introduce un número entero: "))
if n % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")
print()

# Ejercicio 4 – Comparar dos números
a = float(input("Ejercicio 4 - Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
if a > b:
    print("a es mayor que b")
elif a == b:
    print("a es igual a b")
else:
    print("a es menor que b")
print()

# Ejercicio 5 – Nota aprobada o suspensa
nota = float(input("Ejercicio 5 - Introduce tu nota (0 a 10): "))
if nota >= 5:
    print("Has aprobado")
else:
    print("Has suspendido")
print()

# Ejercicio 6 – Clasificación de notas
nota = float(input("Ejercicio 6 - Introduce tu nota (0 a 10): "))
if nota < 0 or nota > 10:
    print("Nota inválida")
elif nota < 5:
    print("Insuficiente")
elif nota < 7:
    print("Suficiente")
elif nota < 9:
    print("Notable")
else:
    print("Sobresaliente")
print()

# Ejercicio 7 – Número mayor de tres
x = float(input("Ejercicio 7 - Introduce el valor de x: "))
y = float(input("Introduce el valor de y: "))
z = float(input("Introduce el valor de z: "))
if x >= y and x >= z:
    mayor = x
elif y >= x and y >= z:
    mayor = y
else:
    mayor = z
print("El número mayor es:", mayor)
print()

# Ejercicio 8 – Descuento en compras
precio = float(input("Ejercicio 8 - Introduce el precio del producto: "))
if precio > 100:
    precio_final = precio * 0.9  # 10% de descuento
    print("Se ha aplicado un 10% de descuento.")
else:
    precio_final = precio
print("Precio final:", precio_final)
print()

# Ejercicio 9 – Año bisiesto (simplificado)
anio = int(input("Ejercicio 9 - Introduce un año: "))
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("El año es bisiesto")
else:
    print("El año no es bisiesto")
print()

# Ejercicio 10 – Calculadora básica
print("Ejercicio 10 - Calculadora básica")
operacion = input("Elige una operación (sumar, restar, multiplicar, dividir): ").lower()
num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

if operacion == "sumar":
    resultado = num1 + num2
elif operacion == "restar":
    resultado = num1 - num2
elif operacion == "multiplicar":
    resultado = num1 * num2
elif operacion == "dividir":
    if num2 != 0:
        resultado = num1 / num2
    else:
        resultado = "Error: división entre cero"
else:
    resultado = "Operación no válida"

print("Resultado:", resultado)
print()
