# Calculadora en Python - Explicación 🧮

Vamos a crear una calculadora paso a paso. Es como construir una máquina que nos ayuda a hacer matemáticas.

## Funciones Básicas de Matemáticas

```python
def suma(numero1, numero2):
    return numero1 + numero2

def resta(numero1, numero2):
    return numero1 - numero2

def division(numero1, numero2):
    return numero1 / numero2

def multiplicacion(numero1, numero2):
    return numero1 * numero2
```
**Explicación:** Estas son las operaciones básicas que nuestra calculadora puede hacer. Cada función toma dos números y devuelve el resultado.

## Menú de la Calculadora
```python
def mostrar_menu():
    print("--------------------------")
    print("=== CALCULADORA BASICA ===")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Salir")
```
**Explicación:** Es como el menú de un restaurante: muestra todas las opciones disponibles para el usuario.

## Obtener la Elección del Usuario
```python
def seleccionar_opcion():
    opcion = input("\nElige una opción (1-5):")
    return opcion
```
**Explicación:** Es como cuando un mesero pregunta qué quieres ordenar. El usuario elige qué operación quiere hacer.

## Pedir los Números
```python
def pedir_numeros():
    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))
    return num1, num2
```
**Explicación:** Pide los números con los que vamos a trabajar. Como reunir los ingredientes antes de cocinar.

## La Función Principal
```python
def calculadora():
    while True:
        mostrar_menu()
        opcion = seleccionar_opcion()

        if opcion == "5":
            print("\n Bye Bye")
            break

        if opcion in ["1", "2", "3", "4"]:
            num1, num2 = pedir_numeros()

            # Realizar operaciones según la opción
            if opcion == "1":
                print(f"\nLa suma es: {suma(num1, num2)}")
            elif opcion == "2":
                print(f"\nLa resta es: {resta(num1, num2)}")
            # ... resto de operaciones
```
**Explicación:** Esta es la función principal que:
1. Muestra el menú
2. Espera a que elijas una opción
3. Pide los números
4. Hace el cálculo
5. Muestra el resultado
6. Repite todo hasta que elijas salir

## Características Especiales

### Protección contra División por Cero
```python
if opcion == "4":  # División
    if num2 == 0:
        print("\nError: No se puede dividir por cero")
    else:
        resultado = division(num1, num2)
```
**Explicación:** Es como un guardián que evita que hagamos algo imposible (dividir por cero).

### Pausa entre Operaciones
```python
input("Presiona Enter para continuar...")
```
**Explicación:** Da tiempo para ver el resultado antes de continuar, como hacer una pausa entre episodios de una serie.

## Cómo Usar la Calculadora
1. Se muestra el menú con opciones
2. Eliges una operación (1-5)
3. Si eliges 5, el programa termina
4. Si eliges 1-4, pides dos números
5. La calculadora muestra el resultado
6. Presionas Enter para hacer otra operación

¡Es como tener una mini calculadora que puedes usar cuando quieras! 🎮✨