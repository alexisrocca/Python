""" Ejercicio 1. Escriba un programa que imprima los primeros 25 números naturales pares. """

def NP_aux(n:int):
    return n*2

def NumerosPares(n: int):
    # for num in range(2,((n*2)+2),2):
    #     print(num)
    if n!=0:
        if n%2 ==0:
            print(n)
            return NumerosPares((n*2)-2)
        return NumerosPares(n-1)
    return
    
NumerosPares(25)