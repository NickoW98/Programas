import math

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Error: División por cero"

def potencia(a, b):
    return a ** b

def raiz_cuadrada(a):
    if a >= 0:
        return math.sqrt(a)
    else:
        return "Error: Raíz cuadrada de un número negativo"

def logaritmo(a, base=math.e):
    if a > 0:
        return math.log(a, base)
    else:
        return "Error: Logaritmo de un número no positivo"

def seno(a):
    return math.sin(math.radians(a))

def coseno(a):
    return math.cos(math.radians(a))

def tangente(a):
    return math.tan(math.radians(a))

def menu():
    print("\n" + "="*30)
    print("     CALCULADORA AVANZADA     ")
    print("="*30)
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Raíz Cuadrada")
    print("7. Logaritmo")
    print("8. Seno")
    print("9. Coseno")
    print("10. Tangente")
    print("0. Salir")
    print("="*30)

def calculadora():
    while True:
        menu()
        opcion = input("Selecciona una operación (0-10): ")

        if opcion == "0":
            print("¡Gracias por usar la calculadora! ¡Hasta luego!")
            break

        elif opcion in ["1", "2", "3", "4", "5"]:
            a = float(input("Ingresa el primer número: "))
            b = float(input("Ingresa el segundo número: "))

            if opcion == "1":
                resultado = sumar(a, b)
                operacion = "Suma"
            elif opcion == "2":
                resultado = restar(a, b)
                operacion = "Resta"
            elif opcion == "3":
                resultado = multiplicar(a, b)
                operacion = "Multiplicación"
            elif opcion == "4":
                resultado = dividir(a, b)
                operacion = "División"
            elif opcion == "5":
                resultado = potencia(a, b)
                operacion = "Potencia"
            print(f"\n{operacion} de {a} y {b} = {resultado}")

        elif opcion == "6":
            a = float(input("Ingresa un número: "))
            resultado = raiz_cuadrada(a)
            print(f"\nRaíz Cuadrada de {a} = {resultado}")

        elif opcion == "7":
            a = float(input("Ingresa el número: "))
            base = input("Ingresa la base (presiona Enter para usar la base natural): ")
            base = float(base) if base else math.e
            resultado = logaritmo(a, base)
            print(f"\nLogaritmo de {a} con base {base} = {resultado}")

        elif opcion in ["8", "9", "10"]:
            a = float(input("Ingresa el ángulo en grados: "))

            if opcion == "8":
                resultado = seno(a)
                operacion = "Seno"
            elif opcion == "9":
                resultado = coseno(a)
                operacion = "Coseno"
            elif opcion == "10":
                resultado = tangente(a)
                operacion = "Tangente"
            print(f"\n{operacion} de {a} grados = {resultado}")

        else:
            print("Opción no válida. Por favor, selecciona una opción del 0 al 10.")

        # Preguntar si el usuario quiere realizar otra operación
        continuar = input("\n¿Deseas realizar otra operación? (s/n): ").strip().lower()
        if continuar != 's':
            print("¡Gracias por usar la calculadora! ¡Hasta luego!")
            break

# Ejecutar la calculadora
calculadora()

