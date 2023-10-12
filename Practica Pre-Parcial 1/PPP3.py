from random import randint

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

# print(cantidadElemDist([1,2,3,4,5,5,6,7,6,5,4,7,1]))

""" Ejercicio 8. Para comprobar si una palabra está en una lista se puede utilizar el operador in,
pero sería una búsqueda lenta ya que busca a través de las palabras según el orden en el cual
aparecen en la lista. Si la lista almacena las palabras en orden alfabético, podemos acelerar
las cosas con una búsqueda dicotómica (también conocida como búsqueda binaria). Esta es
similar a lo que hacemos cuando buscamos una palabra en el diccionario. Comenzamos por
el centro y comprobamos si la palabra que buscamos está antes o después del centro. Si está
antes, buscamos sólo en la primera mitad, si está después, buscamos en la segunda mitad de
la lista. Con esto podemos reducir el tiempo de búsqueda.
Implemente la función busquedaDicotomica que toma una lista de palabras ordenadas alfabé-
ticamente y una palabra a buscar y retorna si la palabra está en la lista o no. """

def bBinaria(l: list, e: int) -> bool:
    i = 0
    f = len(l)
    m = (i+f)//2
    while (i!=f) and (e != l[m]):
        if (e > l[m]) and (m + 1 < len(l)):
            i = m + 1
        else:
            f = m
        m = (i+f)//2
    return l[m] == e

# lista = sorted(["hola","que","tal","como","estas"])
# print(bBinaria(lista,"hola"))

""" Ejercicio 9. Escriba un programa que tenga una función que tome una cadena y muestre
cada caracter que la forma del último al inicial """

def cadenaUaI(s: str) -> str:
    s_return = ""
    for c in range(len(s)-1,-1,-1):
        s_return += s[c]
    return s_return

# print(cadenaUaI("Marina"))

""" Ejercicio 10. Escriba un programa que contenga a la función contar(l, x) que cuente cuán-
tas veces aparece un carácter l dado en una cadena """

def contar(l: list, x: str) -> int:
    cant_x = 0
    for c in l:
        if c == x:
            cant_x += 1
    return cant_x

# print(contar("holaaa cuantas veces aparece a","a"))

""" Ejercicio 11. Escriba un programa que cuente cúantas veces aparecen cada una de las vo-
cales en una cadena. No importa si la vocal aparece en mayúscula o en minúscula """

def contarVocales(s: str) -> str:
    vocales = ["a","e","i","o","u"]
    vocales_contadas = 0
    for c in s.lower():
        if (
            (c == vocales[0]) or
            (c == vocales[1]) or
            (c == vocales[2]) or
            (c == vocales[3]) or
            (c == vocales[4])
            ):
            vocales_contadas += 1
    return vocales_contadas

# print(contarVocales("vocales"))
        
""" Ejercicio 12. Escriba un programa que contenga una función que reciba como parámetro una
cadena de palabras separadas por espacios y devuelva como resultado cuántas palabras de
más de cinco letras tiene la cadena dada. """

def palabrasCincoLetras(s: str) -> int:
    c_palabras = 0
    for palabra in s.split():
        if len(palabra) >= 5:
            c_palabras += 1
    return c_palabras

# print(palabrasCincoLetras("Hola hola hola hola palabra"))

""" Ejercicio 13. Cartas como tuplas
a) Proponga una representación con tuplas para las cartas de la baraja francesa.
b) Escriba una función llamada poker que reciba cinco cartas de la baraja francesa e informe
(devuelva el valor lógico correspondiente) si esas cartas forman o no un póker (es decir
que hay 4 cartas con el mismo número). """

def nTiradasBarajaFrancesa(n: int) -> list: #(Numero, Palo)
    tirada = []
    for n in range(n):
        num = randint(1,13)
        palo = randint(1,4)
        
        if num == 1:
            num = 'As'
        elif num == 11:
            num = 'J'
        elif num == 12:
            num = 'Q'
        elif num == 13:
            num = 'K'
        
        if palo == 1:
            palo = 'Trebol'
        if palo == 2:
            palo = 'Diamante'
        if palo == 3:
            palo = 'Corazones'
        if palo == 4:
            palo = 'Picas'
        
        tirada.append((num,palo))
        
    # print(tirada)
    return tirada

# print(nTiradasBarajaFrancesa(10))

def poker(t: list) -> bool:
    return (
        t[0][0] == t[1][0] and \
        t[1][0] == t[2][0] and \
        t[2][0] == t[3][0]
        )

def aLotOfPoker():
    p=0
    for n in range(500000):
        isPoker = poker(nTiradasBarajaFrancesa(4))
        if isPoker:
            p +=1
    print(f'Hiciste Poker {p} veces!')

aLotOfPoker()

# print(poker([(6,'Corazones'),(6,'Picas'),(6,'Trebol'),(6,'Diamante')]))