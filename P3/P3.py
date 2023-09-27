# PRACTICA 3

# ------------------------------------------------------------------------
# EJ 1
# Escriba una función posicionesMultiplo que tome una lista y un número y retorne la lista formada por los elementos que están en las posiciones múltiplos de ese número.
# Por ejemplo: posicionesMultiplo([1,2,3,4,5,6,7],2) retorna [1,3,5,7] y posicionesMultiplo([1,2,3,4,5,6,7],3) da como resultado [1,4,7]

def posicionesMultiplo(l: list, n: int) -> list:
    l_return = []
    for elem in range(len(l)):
        # print(n*(elem))
        if n*(elem) < len(l):
            l_return.append(l[n*(elem)])
    return print(l_return)

# posicionesMultiplo([1,2,3,4,5,6,7],2)
# posicionesMultiplo([1,2,3,4,5,6,7],3)
# posicionesMultiplo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],4)
# posicionesMultiplo([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25],5)

# ------------------------------------------------------------------------
# EJ 2
# Escriba una función que tome una lista de números y devuelva la suma acumulada, es decir, una nueva lista donde el primer elemento es el mismo, el segundo elemento es
# la suma del primero con el segundo, el tercer elemento es la suma del resultado anterior con el
# siguiente elemento y así sucesivamente. Por ejemplo, la suma acumulada de [1,2,3] es [1,
# 3, 6].

def elemSum(l: list) -> list:
        l_return = []
        for i in range(len(l)):
            if i == 0:
                l_return.append(l[0])
            else:
                l_return.append(l_return[i-1]+l[i])
        return print(l_return)

# elemSum([1,2,3])
# elemSum([1,2,3,4])

# ------------------------------------------------------------------------
# EJ 3
# Escriba una función llamada elimina que tome una lista y elimine el primer y
# último elemento de la lista. La función debe devolver una nueva lista con los elementos que no
# fueron eliminados.