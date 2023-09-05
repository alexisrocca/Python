# PRACTICA 2

# ------------------------------------------------------------------------
# EJ 1
# Escriba un ciclo definido para imprimir por pantalla todos los números entre 10 y 20


# n10to20: None -> None
# Imprime en pantalla todos los numeros entre 10 y 20

def n10to20():
    for number in range(11,21):
        print(number)
        
# n10to20()

# ------------------------------------------------------------------------
# EJ 2
# Escriba un programa que imprima por pantalla todas las fichas del dominó, una
# por línea y sin repetir.

# fichas_domino: None -> None
# Imprime en pantalla todas las fichas del domino

def fichas_domino() -> None:
    for x in range(0,7):
        for y in range(x,7):
            print(f"{x} - {y}")
            
# fichas_domino()

# ------------------------------------------------------------------------
# EJ 3
# Modifique el programa anterior para que pueda generar fichas de un juego que
# puede tener números de 0 a n

# fichas_domino_n: Int -> None
# Imprime en pantalla todas las fichas de un juego tipo domino de 0 hasta n
# n: representa la cantidad numerica maxima capaz de alcanzar la ficha

def fichas_domino_n(n: int) -> None:
    for x in range(0,n+1):
        for y in range(x,n+1):
            print(f"{x} - {y}")
            
# fichas_domino_n(20)

# ------------------------------------------------------------------------
# EJ 4
# Escriba una función que tome una cantidad m de valores que serán ingresados
# por el usuario y, a medida que se ingresa cada número, muestre el factorial del mismo. El valor
# de m es ingresado inicialmente por el usuario

# factorial: Int -> Int
# Devuelve el factorial de un numero
# n: es el numero del que se devolvera el factorial
def factorial(n:int) -> int:
    if n == 0:
        return 1
    return n * factorial(n-1)

# input_factorial: Int -> None
# cant_m: es la cantidad de veces que se pedira la entrada del usuario
def input_factorial(cant_m: int) -> None:
    for veces in range(cant_m):
        num = int(input(f"[{veces+1}] Ingrese un numero: "))
        print(f" - El factorial de {num} es {factorial(num)}")

# input_factorial(3)

# ------------------------------------------------------------------------
# EJ 5
# Usando la función dada como ejemplo en la presentación de La Receta en Python
# para convertir una temperatura de Fahrenheit a Celsius, genere una tabla de conversión de
# temperaturas, desde 0◦F hasta 120◦F , de 10 en 10.

# Representamos temperaturas mediante números enteros
# farCel : Int -> Int
# El parámetro representa una temperatura en Fahrenheit y ,
# se retorna su equivalente en Celsius .
# entrada : 32 , salida : 0
# entrada : 212 , salida : 100
# entrada : -40 , salida : -40
def farCel(f:int):
    return (f -32) *5/9

def tablaConversion() -> None:
    for temperatura in range(0,130,10):
        print(f"{temperatura}°F = {round(farCel(temperatura),3)}")

# tablaConversion()

# ------------------------------------------------------------------------
# EJ 6
# Escriba una función que reciba un número n como parámetro e imprima los pri-
# meros n números triangulares, junto con sus respectivos índices. El número triangular n se
# obtiene mediante la suma de los números naturales desde 1 hasta n

