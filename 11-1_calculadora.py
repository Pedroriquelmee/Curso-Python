# Definición de funciones para las operaciones básicas

def suma(numero1, numero2):
    # Devuelve la suma de dos números
    return numero1 + numero2

def resta(numero1, numero2):
    # Devuelve la resta de dos números
    return numero1 - numero2

def division(numero1, numero2):
    # Devuelve la división de dos números
    return numero1 / numero2

def multiplicacion(numero1, numero2):
    # Devuelve la multiplicación de dos números
    return numero1 * numero2

# Función para mostrar el menú principal
def mostrar_menu():
    print("--------------------------")
    print("=== CALCULADORA BASICA ===")
    print("1. Suma")  # Opción para sumar
    print("2. Resta")  # Opción para restar
    print("3. Multiplicación")  # Opción para multiplicar
    print("4. División")  # Opción para dividir
    print("5. Salir")  # Opción para salir del programa

# Función para que el usuario seleccione una opción
def seleccionar_opcion():
    opcion = input("\nElige una opción (1-5):")  # Solicita una opción entre 1 y 5
    return opcion

# Función para pedir dos números al usuario
def pedir_numeros():
    num1 = float(input("Introduce el primer número: "))  # Pide el primer número
    num2 = float(input("Introduce el segundo número: "))  # Pide el segundo número
    return num1, num2  # Devuelve los dos números como una tupla

# Función principal de la calculadora
def calculadora():
    while True:  # Bucle infinito para mantener el programa en ejecución
        mostrar_menu()  # Muestra el menú principal
        opcion = seleccionar_opcion()  # Captura la opción seleccionada

        if opcion == "5":  # Si la opción es "5", se termina el programa
            print("\n Bye Bye")  # Mensaje de despedida
            break  # Salimos del bucle

        # Si la opción es válida (1-4), pedimos números
        if opcion in ["1", "2", "3", "4"]:
            num1, num2 = pedir_numeros()  # Solicitamos los dos números

            # Ejecuta la operación seleccionada
            if opcion == "1":  # Suma
                resultado = suma(num1, num2)  # Llama a la función suma
                print(f"\nLa suma es: {resultado}")  # Muestra el resultado

            elif opcion == "2":  # Resta
                resultado = resta(num1, num2)  # Llama a la función resta
                print(f"\nLa resta es: {resultado}")  # Muestra el resultado

            elif opcion == "3":  # Multiplicación
                resultado = multiplicacion(num1, num2)  # Llama a la función multiplicación
                print(f"\nLa multiplicación es: {resultado}")  # Muestra el resultado

            elif opcion == "4":  # División
                # Verifica que el segundo número no sea cero
                if num2 == 0:
                    print("\nError: No se puede dividir por cero")  # Muestra un error
                else:
                    resultado = division(num1, num2)  # Llama a la función división
                    print(f"\nLa división es: {resultado}")  # Muestra el resultado
        else:
            # Si la opción no es válida, muestra un mensaje de error
            print("\nError: Opción no válida")

        # Pausa para que el usuario pueda leer los resultados antes de continuar
        input("Presiona Enter para continuar...")

# Inicia la calculadora
calculadora()
