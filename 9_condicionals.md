# Ejemplos de Condicionales en Python

En este documento se muestran diferentes ejemplos prácticos del uso de condicionales en Python.

## Condicional if Simple

```python
# Ejemplo básico con números
number = 10
if number > 5:
    print("El número es mayor que 5")

# Comparación de igualdad
number = 3
if number == 3:
    print("El número es igual a 3")
```

## Estructura if-elif-else con Edad

```python
age = 18
if age < 18:
    print("Eres menor de edad")
elif age == 18:
    print("Tienes 18 años, justo en la mayoría de edad")
else:
    print("Eres mayor de edad")
```

## Verificación de Listas

```python
my_list = []
# Verificar lista vacía
if not my_list:
    print("La lista está vacía")

# Añadir elemento y verificar su presencia
my_list.append(42)
if 42 in my_list:
    print("El número 42 está en la lista")
```

## Verificación de Nombres

```python
name = "Carlos"
if name == "Carlos":
    print("Hola, Carlos")
elif name == "María":
    print("Hola, María")
else:
    print("Hola, desconocido")
```

### Características importantes:

1. **Evaluación Secuencial:**
   - Las condiciones se evalúan de arriba a abajo
   - Solo se ejecuta el primer bloque que cumpla la condición
   - El `else` se ejecuta si ninguna condición anterior es verdadera

2. **Operadores de Comparación:**
   ```python
   # Ejemplos de operadores comunes
   x > 5    # Mayor que
   x < 5    # Menor que
   x == 5   # Igual a
   x != 5   # Diferente de
   x >= 5   # Mayor o igual que
   x <= 5   # Menor o igual que
   ```

3. **Operadores de Pertenencia:**
   ```python
   x in lista    # Verifica si x está en la lista
   x not in lista    # Verifica si x no está en la lista
   ```

### Buenas Prácticas:

1. **Legibilidad:**
   ```python
   # Bueno
   if edad >= 18:
       print("Mayor de edad")
   
   # Evitar
   if not edad < 18:
       print("Mayor de edad")
   ```

2. **Indentación:**
   ```python
   # Correcto
   if condicion:
       print("Dentro del if")
       print("También dentro")
   print("Fuera del if")
   ```

3. **Nombres Descriptivos:**
   ```python
   # Bueno
   edad_usuario = 25
   if edad_usuario >= 18:
       print("Acceso permitido")
   
   # Evitar
   x = 25
   if x >= 18:
       print("Acceso permitido")
   ```

### Casos de Uso Comunes:

1. **Validación de Datos:**
   ```python
   edad = input("Introduce tu edad: ")
   if edad.isdigit():
       edad = int(edad)
       if edad >= 18:
           print("Acceso permitido")
   else:
       print("Por favor, introduce un número válido")
   ```

2. **Control de Flujo:**
   ```python
   saldo = 1000
   retiro = 500
   if saldo >= retiro:
       saldo -= retiro
       print(f"Retiro exitoso. Saldo: {saldo}")
   else:
       print("Saldo insuficiente")
   ```

3. **Verificación de Estados:**
   ```python
   estado_conexion = "conectado"
   if estado_conexion == "conectado":
       print("Procesando datos")
   elif estado_conexion == "reconectando":
       print("Esperando conexión")
   else:
       print("Error de conexión")
   ```

### Consejos Adicionales:

1. **Evitar Anidamiento Excesivo:**
   ```python
   # Mejor
   if not condicion_inicial:
       return
   
   # Continuar con el código principal
   ```

2. **Usar Valores Booleanos Directamente:**
   ```python
   # Mejor
   if es_valido:
       procesar()
   
   # Evitar
   if es_valido == True:
       procesar()
   ```

3. **Mantener las Condiciones Simples:**
   ```python
   # Si necesitas muchas condiciones, considera usar un diccionario
   opciones = {
       "A": "Opción A seleccionada",
       "B": "Opción B seleccionada",
       "C": "Opción C seleccionada"
   }
   resultado = opciones.get(seleccion, "Opción no válida")
   ```