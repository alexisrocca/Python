""" Ejercicio 3. Escriba una función llamada elimina que tome una lista y elimine el primer y
último elemento de la lista. La función debe devolver una nueva lista con los elementos que no
fueron eliminados."""

def elimina(l: list) -> list:
    return l[1:-1]

# print(elimina([1,2,3,4,5,6,7]))

""" Ejercicio 4. Escriba una función ordenada que tome una lista como parámetro y devuelva
T rue si la lista está ordenada en orden ascendente y F alse en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna T rue y ordenada([’b’, ’a’]) retorna F alse. """

def ordenada(l: list) -> bool:
    ordenada = True
    i=0
    while i+1 < len(l) and l[i] < l[i+1]:
        i+=1
        if i+1 < len(l) and l[i] >= l[i+1]:
            ordenada = False
    return ordenada
    
# print(ordenada([1, 2, 3]))
# print(ordenada(['a','b','c']))
# print(ordenada([1,2,3,4,5,7,6]))
        
""" Ejercicio 5. Escriba una función llamada duplicado que tome una lista y devuelva T rue si
tiene algún elemento duplicado. La función no debe modificar la lista. """

def duplicado(l: list) -> bool:
    return len(list(set(l))) != len(l)

# print(duplicado([1,2,3,4,5,5]))
# print(duplicado([1,2,3,4,5,6]))

""" Ejercicio 6. Escriba una función llamada eliminaDuplicados que tome una lista y devuelva
una nueva lista con los elementos únicos de la lista original. No tienen porque estar en el mismo
orden. Ayuda: puede utilizar la función sort """

def eliminaDuplicados(l: list) -> list:
    return list(set(l))

# print(eliminaDuplicados([1,2,3,4,6,7,8,3,5,4,3,5,7]))

""" Ejercicio 7. Escriba una función que tome una lista y retorne la cantidad de elementos dist
intos que tiene. Se recomienda usar la función del ejercicio anterior. """

def cantidadElemDist(l:list) -> int:
    return len(eliminaDuplicados(l))