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

# numeros_triangulares: Int -> None
def numeros_triangulares(n: int) -> None:
    n_anterior = 0
    for num in range(1,n+1):
        print(f"{num} - {n_anterior + num}")
        n_anterior = n_anterior + num
        
# numeros_triangulares(5)

# ------------------------------------------------------------------------
# EJ 7
# Escriba una función que le pida al usuario que ingrese un número positivo. Si el
# usuario ingresa cualquier cosa que no sea lo pedido se le debe informar de su error mediante
# un mensaje y volver a pedirle el número, repitiendo este proceso hasta que ingrese lo pedido

def input_positivo() -> None:
    n = 0
    while not(n>0):
        n = int(input("Ingrese un numero positivo: "))
        if not(n>0):
            print(f"{n} no es un numero positivo, por favor vuelva a intentarlo ...\n")
    print(":)")
    
# input_positivo()

# ------------------------------------------------------------------------
# EJ 8
# Escriba un programa que permita al usuario ingresar un conjunto de notas, pre-
# guntando a cada paso si desea ingresar más notas, e imprima el promedio correspondiente al
# finalizar la toma de datos

def notas():
    continuar = 's'
    l_notas = []
    prom = 0
    while (continuar == 's') or (continuar == 'S'):
        nota = int(input("Ingrese una nota numerica: "))
        l_notas += [nota]
        continuar = input("Desea ingresar mas notas? S/n: ")
    for nota in l_notas:
        prom += nota
    prom = prom/len(l_notas)
    print(f"El promedio es {prom}")
    
# notas()

# ------------------------------------------------------------------------
# EJ 9
# Escriba un programa que pida dos números enteros. El programa pedirá de nuevo
# el segundo número mientras no sea mayor que el primero. El programa terminará escribiendo
# los dos números.

def ej9():
    a = int(input("Ingrese el primer numero: "))
    b = 0
    while not(a<b):
        b = int(input("Ingrese el segundo numero: "))
    print(f"Los numeros son: {a} y {b}")
        
# ej9()

# ------------------------------------------------------------------------
# EJ 10
# Escriba una función que reciba dos números como parámetros y devuelva cuán-
# tos múltiplos del primero hay que sean menores que el segundo.

def ej10_A(a:int, b:int):
    multiplo = 0
    cont = 0
    cant_operaciones = 0
    while multiplo < b:
        cant_operaciones += 1
        cont += 1
        multiplo = a * cont
    # print(cont-1)
    print(f"+ Cantidad de multiplos: {cont-1}")
    print(f"  - Operaciones realizadas {cant_operaciones}\n")

def ej10_B(a:int, b:int):
    cont = 0
    cant_operaciones = 0
    for num in range(a,b+1):
        cant_operaciones += 1
        if (num%a == 0) and (num < b):
            cont +=1
    print(f"+ Cantidad de multiplos: {cont}")
    print(f"  - Operaciones realizadas {cant_operaciones}\n")

# print("\n-- Usando WHILE --")
# ej10_A(3, 9) # Hay 2 multiplos del primero que son menores estrictos del segundo
# ej10_A(2, 50) # Hay 24 multiplos del primero que son menores estrictos del segundo
# ej10_A(2, 100) # Hay 49 multiplos del primero que son menores estrictos del segundo
# print("\n-- Usando FOR --")
# ej10_B(3, 9) # Hay 2 multiplos del primero que son menores estrictos del segundo
# ej10_B(2, 50) # Hay 24 multiplos del primero que son menores estrictos del segundo
# ej10_B(2, 100) # Hay 49 multiplos del primero que son menores estrictos del segundo

# A pesar de dar el mismo resultado, el bucle For realiza mas operaciones de manera innecesaria,
# que se ahorran haciendolo con el bucle While

# ------------------------------------------------------------------------
# EJ 11

# A)
# Escriba un programa que contenga una contraseña inventada. El programa debe pre-
# guntarle al usuario la contraseña y no permitirle continuar hasta que la haya ingresado
# correctamente.

def passwd_A():
    passwd = '123456'
    entrada = ''
    while entrada != passwd:
        entrada = input("\nIntroduzca la contraseña: ")
    print("Sesion Iniciada!")

# passwd_A()

# B)
# Modifique el programa anterior para que solamente permita como máximo una cantidad
# fija de intentos

def passwd_B():
    passwd = '123456'
    entrada = ''
    intentos = 3
    while (entrada != passwd) and (intentos != 0):
        entrada = input(f"\n[Intentos restantes: {intentos}]\n - Introduzca la contraseña: ")
        intentos -=1
    if entrada != passwd:
        print("\n[!] Sin intentos restantes...")
    else:
        print("\nSesion Iniciada!")

# passwd_B()

# C)
# Modifique el programa anterior para que sea una función que devuelva si el usuario in-
# gresó la contraseña correctamente o no, mediante un valor booleano (True o False).

def passwd_C() -> bool:
    passwd = '123456'
    entrada = ''
    intentos = 3
    while (entrada != passwd) and (intentos != 0):
        entrada = input(f"\n[Intentos restantes: {intentos}]\n - Introduzca la contraseña: ")
        intentos -=1
    return entrada == passwd

# print(passwd_C())

# ------------------------------------------------------------------------
# EJ 12

# Escriba una función que reciba un número natural e imprima todos los números
# primos que hay menores o iguales que ese número.
      
# A) 
# Defina una función es_primo que toma un número natural y verifica si es un número primo.

def es_primo(n: int) -> bool:
    cant_divisiones = 1
    divisible = 0
    while cant_divisiones <= n:
        if (n % cant_divisiones) == 0:
           divisible += 1
        cant_divisiones += 1    
    return divisible == 2

def es_primo(n: int) -> bool:
    cant_divisiones = 1
    divisible = 0
    while cant_divisiones <= n:
        if (n % cant_divisiones) == 0:
           divisible += 1
        cant_divisiones += 1    
    return divisible == 2

# print(es_primo(7))

# B) 
# Resuelva el problema usando la función definida en el punto anterior.

def num_primos(num: int):
    while num != 0:
        if es_primo(num):
            print(num)
        num-=1

# num_primos(25)

# ------------------------------------------------------------------------
# EJ 13

# Escriba una función es_potencia_de_dos que reciba como parámetro un número natural
# y devuelva True si el número es una potencia de 2 y False en caso contrario

def es_potencia_de_dos(n: int) -> bool:
    if (n == 0):
        return False
    while (n%2 == 0):
        n = n/2
    return n == 1

# es_potencia_de_dos(8)

for num in range(10000):
    if es_potencia_de_dos(num):
        print(f"{num} - {es_potencia_de_dos(num)}")