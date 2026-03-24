# Guía de Ejemplos: Conceptos de Programación en la Vida Real

A continuación, exploraremos tres de los conceptos más importantes de la programación introductoria utilizando analogías de la vida real. El objetivo es desmitificar herramientas como **Variables, Funciones, Condicionales y Ciclos (Loops)**, comprendiendo su utilidad práctica mediante la lectura de código documentado paso a paso.

---

## 1. La Máquina de Café (Funciones, Variables e If/Else)

Este ejemplo es ideal para entender la relación entre datos y acciones.
*   **Variables (Los insumos):** Piensa en las variables como los contendores donde guardamos los ingredientes a utilizar (azúcar, tipo de grano, cantidad de agua).
*   **Funciones (La máquina):** Una función es un proceso automatizado. Al igual que una máquina de café recibe los ingredientes, los procesa y nos entrega una bebida caliente, una función en Python recibe parámetros, ejecuta un bloque de código y devuelve un resultado (`return`).
*   **Condicionales (`if` / `else`):** Son las decisiones lógicas dentro de la máquina. Dependiendo de los ingredientes ingresados, el proceso final puede cambiar (ej., añadir leche o servir negro).

### Script en Python:

```python
def preparar_cafe(tipo_grano, cantidad_agua, con_leche):
    """
    Simula el funcionamiento de una máquina de café.
    
    Parámetros de entrada:
    - tipo_grano (str): El nombre del grano de café o variedad.
    - cantidad_agua (int): La cantidad de agua en mililitros.
    - con_leche (bool): Verdadero (True) si el usuario lo quiere con leche, Falso (False) si no.
    """
    print(f"--- Iniciando preparación de café {tipo_grano} ---")
    print(f"Calentando {cantidad_agua} ml de agua para el filtro...")
    
    # Estructura Condicional (If/Else)
    # Aquí la máquina "toma la decisión" basándose en el valor de la variable 'con_leche'
    if con_leche == True:
        print("Agregando espuma de leche caliente a la taza 🥛.")
        resultado = f"Café {tipo_grano} Cortado (con leche)"
    else:
        print("No se solicitó leche. Sirviendo el café negro ☕.")
        resultado = f"Café {tipo_grano} Negro"
        
    print("¡El proceso interno terminó, el café está listo para entregarse!")
    
    # El return es la máquina abriendo la puertecita y entregando el producto físico
    return resultado

# Definimos nuestras Variables (los valores de la vida real que inyectaremos en la máquina)
agua_necesaria = 250
grano_elegido = "Arábica Intenso"
quiere_leche = True

# Ejecutamos la función (Es decir, presionamos el botón de encendido de la máquina)
# Lo que retorne la función (la taza virtual) quedará guardado en la variable 'mi_taza'
mi_taza = preparar_cafe(grano_elegido, agua_necesaria, quiere_leche)

print("El cliente acaba de recibir su:", mi_taza)
```

---

## 2. El Cajero Automático (Operaciones Matemáticas y Control de Flujo)

Este es un excelente modelo para explicar cómo un programa reacciona a los eventos del mundo y "se protege" a sí mismo validando diferentes escenarios a través de vías lógicas.
*   **Variables y Operaciones:** El sistema debe recordar cuánto dinero tienes (`saldo`). Al sacar billetes, matemáticamente debe restar el monto retirado del total (`saldo = saldo - retiro`).
*   **Control de Flujo (`if` / `elif` / `else`):** El cajero evalúa distintas circunstancias:
    1. Si pides más plata de la que tienes -> Rechaza la operación.
    2. Si no es múltiplo de lo que el cajero dispone -> Te avisa la restricción.
    3. Si todo está en orden -> Entrega el dinero.

### Script en Python:

```python
# Variable flotante que almacena el dinero actual en la cuenta bancaria del usuario
saldo_actual = 50000.50

def intentar_retiro(saldo, monto_retiro):
    """
    Evalúa si es posible retirar dinero de un cajero automático en base al saldo.
    Retorna el nuevo saldo tras finalizar la operación.
    """
    print(f"\n--- Intento de retiro por: ${monto_retiro} ---")
    
    # Condicional Múltiple (If / Elif / Else)
    if monto_retiro > saldo:
        # Escenario 1: El usuario pide más dinero del que realmente tiene en su cuenta
        print("❌ Error: Fondos insuficientes. No puedes retirar esa cantidad.")
        
    elif monto_retiro % 100 != 0:
        # Escenario 2: El monto NO es múltiplo de 100 (El operador % obtiene el Resto de una división)
        # Es decir, si pides 150, sobra 50, por ende no es múltiplo estricto de 100.
        print("⚠️ Aviso: Este cajero automático solo dispone de billetes de $100.")
        
    else:
        # Escenario 3: Si NO se cumplió ninguno de los errores de arriba, entra en la vía del éxito
        saldo = saldo - monto_retiro  # Operación matemática de resta (Actualizamos el saldo)
        print(f"✅ Retiro aceptado. Por favor, agarre sus ${monto_retiro} de la ranura inferior.")
        
    # Retornamos a la base de datos central cómo quedó el saldo 
    # (Si hubo error será igual al inicio, si hubo éxito será un número menor)
    return saldo

print(f"Saldo inicial en la base de datos: ${saldo_actual}")

# Caso de prueba 1: Intentamos retirar más de lo que tenemos
saldo_actual = intentar_retiro(saldo_actual, 70000)

# Caso de prueba 2: Intentamos retirar un monto que no es un billete válido (150 pesos)
saldo_actual = intentar_retiro(saldo_actual, 150)

# Caso de prueba 3: Retiro limpio y exitoso sin romper ninguna validación
saldo_actual = intentar_retiro(saldo_actual, 5000)

print(f"\nSaldo final guardado en su perfil tras todas las operaciones: ${saldo_actual}")
```

---

## 3. La Caja Registradora del Supermercado (Listas y Ciclos/Loops)

Este es el ejemplo perfecto para comprender las colecciones de datos masivos y los bucles automáticos. 
*   **Listas (La cinta transportadora):** En vez de tener cientos de variables (ej. `producto1 = "Pan"`, `producto2 = "Agua"`), los artículos se agrupan en una secuencia ordenada llamada Lista.
*   **Loops (El cajero escaneando incansablemente):** Un ciclo, como el bucle `for`, le sirve al programador para repetir un código muchísimas veces sin tener que escribirlo a mano una y otra vez. Se traduce como: *"Por cada elemento de este grupo, haz X acción"*.

### Script en Python:

```python
# El carrito_compras es una Lista (un tipo de dato que agrupa múltiples ítems ordenados)
carrito_compras = ["Lata de Tomate", "Pan", "Sachet de Leche", "Docena de Huevos"]

# Este Diccionario simula ser el sistema interno de precios del hipermercado
sistema_de_precios = {
    "Lata de Tomate": 80.50,
    "Pan": 120.00,
    "Sachet de Leche": 95.00,
    "Docena de Huevos": 150.00
}

def cobrar_cliente(lista_productos):
    """
    Toma una lista de productos de un carrito, cicla por cada uno de ellos,
    identifica su precio e imprime el ticket de cobro final.
    """
    # Esta es una variable "acumuladora" (Una cajita vacía donde iremos metiendo dinero de a poco)
    total_a_pagar = 0.0 
    
    print("🛒 --- Iniciando paso por caja (Escaneando la cinta) ---")
    
    # Bucle For (Ciclo/Loop principal):
    # Esto se lee así: Por cada 'producto' dentro de la 'lista_productos', repite el bloque de código indentado
    for producto in lista_productos:
        
        # Le preguntamos "cuánto vale" al sistema de precios utilizando el nombre del producto de esta interacción
        precio_actual = sistema_de_precios[producto] 
        
        # Le sumamos a la boleta el valor individual de este escaneo
        total_a_pagar = total_a_pagar + precio_actual 
        
        # Imprimimos la acción repetitiva de escuchar un ticket generándose
        print(f"  * Beep! Escaneado: {producto} -> sumó ${precio_actual}")
        
    # Una vez acabados los elementos del carrito, el loop For CORTA su repetición 
    # y seguimos normalmente en la línea de abajo.
    print("-----------------------------------------------------")
    print(f"✅ Lectura finalizada. El monto total a abonar es de: ${total_a_pagar}")
    
    return total_a_pagar

# El software llama de forma fácil a la función dándole como parámetro toda la cajita del carrito
ticket_final = cobrar_cliente(carrito_compras)
```
