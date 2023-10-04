from random import randint


""" Ejercicio 1. Escriba una función que, dados una lista desordenada y un elemento:
a) devuelva la cantidad de apariciones del elemento recibido en la lista;
b) busque la primera coincidencia del elemento en la lista y devuelva su posición;
c) utilizando la función anterior, busque todos los elementos que coincidan con el que fue
recibido como parámetro y devuelva una lista con las respectivas posiciones. """


def contador_elem(l: list, n):
    x = 0
    cont = 0
    while x < (len(l)):
        if l[x] == n:
            cont += 1
        x += 1
    return cont

# print(contador_elem([9,9,9,9,5,9],9))


def indice(l: list, n):
    x = 0
    aux = 0
    while aux != 1 and x < (len(l)):
        x += 1
        if l[x] == n:
            aux += 1
    return x

# print(indice([2,3,9,9,5,9],5))


def search_and_list(l: list, n):
    x = 0
    r_list = []
    while x < (len(l)):
        if l[x] == n:
            r_list.append(x)
        x += 1
    return r_list

# print(search_and_list([2,3,9,9,5,9],9))


""" Ejercicio 2. Escriba una función que tome una lista de números desordenada y:
a) devuelva el valor máximo;
b) devuelva una tupla que incluya el valor máximo y su posición. """


def search_index(l: list):

    aux = 0
    mayor = 0
    pos = 0

    for x in range(0, len(l)):
        for y in range(0, len(l)):
            if l[x] > l[y]:
                aux += 1
            if aux == len(l):
                mayor = l[x]
                pos = x
    return (mayor, pos)


# print(search_index([2,3,10,4,5,7]))


""" Ejercicio 3. Escriba una función que tome una lista ordenada y un elemento. Si el elemento
se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posició """


def b_binaria(l: list, e):

    l.sort()
    mitad_l = len(l) // 2
    aux_l = l
    largo = len(aux_l)
    pos_l = list(range(0, largo))
    print(l)
    print(pos_l)
    while largo != 1:

        if e >= aux_l[mitad_l] and (largo != 1):
            pos_l = pos_l[mitad_l:]
            aux_l = aux_l[mitad_l:]
            mitad_l = len(aux_l[mitad_l:]) // 2

        elif e < aux_l[mitad_l] and (largo != 1):

            pos_l = pos_l[:mitad_l]
            aux_l = aux_l[:mitad_l]
            mitad_l = len(aux_l[:mitad_l]) // 2

        largo = len(aux_l)

    if aux_l[0] == e:
        return pos_l[0]
    else:
        l.append(e)
        l.sort()
        return b_binaria(l, e)

# print(b_binaria([4,1,6,8,5],-1))


def bBin(l: list[int], e: int):
    l.sort()
    i = 0
    f = len(l)
    m = (i + f)//2
    len_list = len(l)
    # print(l)
    while i != f and l[m] != e:
        # print(m)
        if e > l[m] and (m+1 < len_list):
            i = m+1
        else:
            f = m
        m = (i+f)//2
    # print(m)
    return l[m] == e

# print(bBin([1,6,4,2,7],999))


def iBin_Resolucion(l: list, e: int) -> int:
    l.sort()  # Agrego esto para que se puedan utilizar listas de numeros desordenadas
    i = 0
    f = len(l)
    m = (i + f) // 2
    print(l)

    while i != f and l[m] != e:
        if (e > l[m]):
            i = m+1
        else:
            f = m
        m = (i + f) // 2
    if i == f:
        # l.insert(i,e)
        l[i:f] = [e]
        print(l)
    return m

# print(iBin_Resolucion([1,7,4,3,2,6],7))
# print(iBin_Resolucion([],7))


""" 
Ejercicio 4. Escriba una función que reciba una lista de tuplas y devuelva un diccionario en
donde las claves sean los primeros elementos de las tuplas y los valores una lista con los
segundos """


def tup_dic(lt: list) -> dict:
    dicc = {}
    for x, y in lt:
        if x not in dicc:
            dicc[x] = []
        dicc[x].append(y)
    return dicc

# print(tup_dic([('Hola','don Pepito'),('Hola','don Jose'),('Buenos','Dias')]))

""" 
Ejercicio 5

a) """


def str_dict(s: str) -> dict:
    dicc = {}
    for palabra in s.lower().split():
        if palabra in dicc.keys():
            n = dicc[palabra] + 1
            dicc[palabra] = n
        else:
            dicc[palabra] = 1
    return dicc

# print(str_dict("Hola que tal hola funciona esto? hola jaja"))
""" 
b)
 """

def char_dict(s: str) -> dict:
    dicc = {}
    for palabra in s.lower():
        if palabra in dicc.keys():
            n = dicc[palabra] + 1
            dicc[palabra] = n
        else:
            dicc[palabra] = 1
    return dicc

# print(char_dict("Hola que tal hola funciona esto? hola jaja"))


""" 
c)
Escriba una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
realizar y devuelva un diccionario en el cual las claves sean los resultados de la suma de
los dados y los valores sean la cantidad de veces que se observa cada resultado. """

def dados(ct: int) -> dict:
    dicc = {}
    for n in range(ct):
        tirada = []
        for n in range(2):
            tirada.append(randint(1, 6))
        print(tirada)
        if (tirada[0]+tirada[1]) in dicc:
            dicc[tirada[0]+tirada[1]] = dicc[tirada[0]+tirada[1]] + 1
        else:
            dicc[tirada[0]+tirada[1]] = 1
    return dicc

# print(dados(5))

""" 
Ejercicio 6. Escriba una función que reciba un texto y devuelva un diccionario que, para
cada caracter presente en el texto, almacene la cadena más larga en la que se encuentra ese
caracter.
"""

def pml_dicc(s: str) -> dict:
    dicc = {}
    for palabra in s.split():
        for letra in palabra.lower():
            if letra not in dicc or len(palabra) > len(dicc[letra]):
                dicc[letra] = palabra
    return dicc                    

texto = "Hoy es un hermoso dia de primavera"

print(pml_dicc(texto))

# CONJUNTOS
""" 
Ejercicio 10. Escriba una función que tome una lista y utilice un conjunto para eliminar sus
elementos duplicados. """


def list_set(l: list) -> set:
    return set(l)


# print(list_set([1,1,1,5,4,3,6,3,3,5]))
""" 
Ejercicio 11. Escriba una función que tome dos cadenas de texto y devuelva un conjunto con
las palabras que aparecen en ambas cadenas (sin tener en cuenta mayúsculas y minúsculas). """


def str_set(s1: str, s2: str) -> set:
    return set(s1.lower().split()) & set(s2.lower().split())

# print(str_set("hola","hola jesus"))


""" 
Ejercicio 12. Escriba una función que, dados dos conjuntos, devuelva un nuevo conjunto que
contenga los elementos que están en uno de los conjuntos pero no en ambos. """


def conj_conj(c1: set, c2: set) -> set:
    return (c1 | c2) - (c1 & c2)

# print(conj_conj({1,2,3,4,5},{2,4,6,1,3}))


""" 
Ejercicio 13. Escriba una función que tome una lista desordenada de números naturales
como entrada, calcule cuál es el número N máximo de la lista y devuelva un conjunto con los
números naturales menores a N que no están en la lista. """


def n_max(l: list) -> set:
    return set(range(max(l))) - set(l)

# print(n_max([1,5,7,10]))


""" 
Ejercicio 14. Organizar una reunión
Escriba una función que tome como entrada un diccionario cuyas claves sean los nombres
de las personas asistentes a la reunión y cuyos valores sean las listas de los días disponibles
que tiene cada persona. La función debe devolver un conjunto con los días en los que todas
las personas pueden asistir. """


def reunion(d: dict) -> set:
    print(d)
    a = set()
    for persona in d:
        if a == set():
            a = d[persona]
        a = set(a) & set(d[persona])
    return a

personas = {
        "Pepe":["lunes","martes"],
        "Mono": ["martes","miercoles","jueves"],
        "MonoMayor": ["lunes","jueves","martes"]
    }

# print(reunion(personas))
