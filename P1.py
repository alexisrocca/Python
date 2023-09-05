# ------------------------------------------------------------------------
# EJ 1
# Escriba un programa que imprima los primeros 25 números naturales pares.

def par(n: int):
    return n%2==0

def npares(n: int) -> int:
    if n == 0:
        return 
    if n%2 == 0:
        print(n)
    return npares(n-1)

# npares(25)

# ------------------------------------------------------------------------
# EJ 2
# Escriba un programa que imprima los primeros 100 números naturales pares

# npares(100)

# ------------------------------------------------------------------------
# EJ 3
# Escriba un programa que imprima los primeros n números pares mayores que m.

def npares_m(n: int,m: int) -> int:
    if n == 0:
        return 
    if (n%2 == 0) and (n>m):
        print(n)
    return npares_m(n-1,m)

def npares_m(m: int, n:int) -> int:
    if n == 0:
        return
    if (m%2 == 0):
        print(m)
        return npares_m(m+2,n-1)
    return npares_m(m+1,n)
    
npares_m(25,5)

# ------------------------------------------------------------------------
# EJ 4
# Escriba un programa que calcule e imprima el resultado de la suma de los prime-
# ros 50 números naturales usando una función recursiva

def sumnat(n:int = 50) -> int:
    if n == 0:
        return n
    return n + sumnat(n-1)

# print(sumnat(50))

# ------------------------------------------------------------------------
# EJ 5
# Escriba un programa que calcule e imprima el resultado de la suma de los prime-
# ros n números naturales usando una función recursiva.

# print(sumnat(25))

# ------------------------------------------------------------------------
# EJ 6
# Escriba un programa que calcule e imprima el resultado de la suma de los núme-
# ros naturales mayores que n y menores que m usando una función recursiva

def sumnat_m(x:int, n: int, m: int) -> int:
    if x == 0:
        return x
    if (x > n) and (x < m):
        return x + sumnat_m(x-1,n,m)
    return sumnat_m(x-1,n,m)

# print(sumnat_m(10,5,9))
# 6 + 7 + 8 = 21 

# ------------------------------------------------------------------------
# EJ 7
# Escriba un programa que reciba un nombre y retorne el nombre pasado concate-
# nado 2 veces. Es decir, supongamos que la función se llama duplica, si hacemos duplica(”Federico”)
# el resultado que deberíamos obtener sería: ”FedericoFederico”

def duplicar(nombre: str) -> str:
    return print(nombre*2)

# duplicar("Alexis")

# ------------------------------------------------------------------------
# EJ 8
# Escriba un programa que reciba un nombre y un número n, y retorne el nombre pa-
# sado concatenado n veces. Es decir, supongamos que la función se llama duplica, si hacemos
# duplica(”F ederico”, 3) el resultado que deberíamos obtener sería: ”F edericoF edericoF ederico”

def multiplicar_str(nombre:str, veces: int) -> str:
    return print(nombre*veces)

# multiplicar_str("Alexis",3)

# ------------------------------------------------------------------------
# EJ 9

def suma(a:float,b:float) -> float:
    return a+b

def resta(a:float,b:float) -> float:
    return a-b

def multiplicacion(a:float,b:float) -> float:
    return a*b

def division(a:float,b:float) -> float:
    return a/b

def Calculadora():
    print("---------------------\n| 1 - Sumar\n| 2 - Restar\n| 3 - Multiplicar\n| 4 - Dividir\n| 5 - Salir\n---------------------")
    op = int(input(": "))
    if op == 1:
        print("---------------------\nSuma")
        a = float(input("Num: "))
        b = float(input("Num: "))
        print(f"El resultado es {suma(a,b)}")
    elif op == 2:
        print("---------------------\nResta")
        a = float(input("Num: "))
        b = float(input("Num: "))
        print(f"El resultado es {resta(a,b)}")
    elif op == 3:
        print("---------------------\nMultiplicacion")
        a = float(input("Num: "))
        b = float(input("Num: "))
        print(f"El resultado es {multiplicacion(a,b)}")
    elif op == 4:
        print("---------------------\nDivision")
        a = float(input("Num: "))
        b = float(input("Num: "))
        print(f"El resultado es {division(a,b)}")
    elif op == 5:
        return
    Calculadora()
        
# Calculadora()