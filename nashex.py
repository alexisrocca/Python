



# recibe una lista
# recibe una palabra o numero
# dice si la palabra esta en la lista tomando la busqueda a partir de la mitad de la misma.

def busquedaDicotomica(l:list,e:str) -> bool:
    i = 0
    f = len(l)
    m = (i + f) // 2
    while (i != f and l[m] != e):
        if (e > l[m]):
            i = m+1
        else:
            f = m
        m = (i + f) // 2
    return l[m] == e


#print(busquedaDicotomica(["juan","domingo","peron","juana","zurdui"], "juan"))

# recibe lista desordenada y elemento
# cant de apariciones

def cantapariciones(l:list,n:any):
    a = 0
    for x in l:
        if x == n:
            a += 1
    return a


def posicionprimerlemento(l:list,n:any):
    x = 0

    while l[x] != n:
        x += 1
    return x

#print(cantaparaciones2([1,2,3,4,5,6,7,8,9,7],7))
        

def cantapariciones3(l:list,n:any):
    posiciones = []
    cant = cantapariciones(l,n)
    while cant != 0:
        PosObj = posicionprimerlemento(l,n)
        l[PosObj] = 0
        posiciones.append(PosObj) 
        cant -= 1

    return posiciones

#print(cantapariciones3(["e","d","a","a","b","a","c",],"a"))



def maximo(l:list):
    max = l[0]
    for x in l:
        if x > max:
            max = x
    return max

def maxYpos(l:list):
    max = maximo(l)
    x = 0
    while max != l[x]:
        x+=1
    
    return (max,x)

#print(maxYpos([2,5,7,9,2,4,67,97,1,4,6,7,8]))


def tuplas_a_diccionario(l:list):
    Directorio = {}

    for clave,valor in l:
        if clave not in Directorio:
            Directorio[clave] = []
        Directorio[clave].append(valor)

    return Directorio

print(tuplas_a_diccionario( [ ( " Hola " , " don␣ Pepito " ) , ( " Hola " , " don␣ Jose " ) ,( " Buenos  ", ' d i a s')]))

def contar_dic(string:str):
    lista = string.split()

    for i in range(len(lista)):
        lista[i] = lista[i].lower()

    diccionario = {}

    for palabra in lista:
        if palabra not in diccionario:
            diccionario[palabra] = 0
        diccionario[palabra] += 1 
    
    return diccionario
    
#print(contar_dic("Que lindo dia que hace hoy"))


def conteo_caracter(string:str):

    string_sin_espacios = string.replace(" ", "")
    string.lower()
    diccionario = {}
    

    for letra in string_sin_espacios:
        if letra not in diccionario:
            diccionario[letra] = 0
        diccionario[letra] += 1
    
    return diccionario

#print(conteo_caracter("aaaaa aaaaa"))
from random import *

def tirarDados(n:int):

    valores_sum = []
    dir = {}

    while n > 0:
        dados = randint(1,12)
        valores_sum.append(dados)
        n -= 1
    
    for valor in valores_sum:
        if valor not in dir:
            dir[valor] = 0
        dir[valor] += 1

    return dir

#print(tirarDados(10))

def palabra_mas_larga(string:str):
    dic= {}
    for palabra in string.split():
        largo_palabra = len(palabra)
        palabra = palabra.lower()
        for caracter in palabra:
            if (caracter not in dic) or (len(dic[caracter]) < largo_palabra):
                dic[caracter] = palabra
    return dic

#print(palabra_mas_larga("Hoy es un hermoso dia de primavera"))


def promedio(dic: dict, alumno: str):
    prom = 0

    if alumno in dic:
        for nota in dic[alumno]:
            prom += nota

    
    return prom/len(dic[alumno])


#print(promedio({"juan": [5,5,7,7]},"juan"))

def prom_max(lista:list):
    mejor_promedio = lista[0]
    for estudiante in lista:
        if estudiante[1] > mejor_promedio[1]:
            mejor_promedio = estudiante
    return mejor_promedio



def mayor_prom(dir:dict):
    lista_alumnos_con_promedios = []
    for estudiante in dir:
            prom = promedio(dir , estudiante)
            lista_alumnos_con_promedios.append((estudiante, prom))

    mejor_alumno = prom_max(lista_alumnos_con_promedios)

    print("el mejor promedio es",mejor_alumno[0],"con un promedio de:",mejor_alumno[1])
    
#mayor_prom({"Juan": [5,5,7,7],"Pedro": [10,10,10,10],"Juan Cruz": [8,5,7,7],"Santiago": [5,3,2,9]})


def eliminarduplicados_conjuntos(l:list):
    h = set(l)
    richard = [] 
    for elemento in h:
        richard.append(elemento)
    return richard

#print(eliminarduplicados_conjuntos([1,2,3,4,5,6,7,1,1,1,1,2,2,2,2,3]))

def palabras_comunes(cadena1, cadena2):
    # Convertir las cadenas a minúsculas y dividirlas en palabras
    palabras1 = set(cadena1.lower().split())
    palabras2 = set(cadena2.lower().split())
    
    # Devolver la intersección de los dos conjuntos
    return palabras1 & palabras2

#print(palabras_comunes("Juan Domingo Peron el mejor","Juan Domingo Peron el peor"))


def no_en_ambos(conjunto1,conjunto2):
    conjunto_interseccion = conjunto1 & conjunto2
    conjunto_total = conjunto1 | conjunto2

    return conjunto_total - conjunto_interseccion


#print(no_en_ambos({1,2,3,4,5,6,7,8},{1,2,3,4,9,10}))

def mayor_list_desordenada(lista:list) -> set:
    lista.sort()
    mayor = lista[-1]
    a  = set()
    for x in range(0,mayor):
        if x not in lista:
            a.add(x)
    return a

#print(mayor_list_desordenada([2,4,8,9,50,1,2,3,4,5,6]))


# Versión recomendable
def numerosFaltantes (l: list[int]) -> set[int]:
    maximo = max(l)
    universo = set(range(maximo))
    s = set(l)
    return universo - s 


""" Ejercicio 14. Organizar una reunión
Escriba una función que tome como entrada un diccionario cuyas claves sean los nombres
de las personas asistentes a la reunión y cuyos valores sean las listas de los días disponibles
que tiene cada persona. La función debe devolver un conjunto con los días en los que todas
las personas pueden asistir. """


# recibe un diccionario
# devuelve el conjunto de dias
# las claves son nombres


def reunion(itinerario:dict)-> set:
    dias_posibles = set()
    for persona in itinerario:
        if dias_posibles == set():
            dias_posibles.update(itinerario[persona])
        else:
            dias_posibles = dias_posibles & set(itinerario[persona])

    return dias_posibles

#print(reunion({"Susana": ["domingo","viernes","martes"], "Juan": ["lunes","viernes","domingo"],"Santi": ["martes","viernes","domingo"]}))


#print(reunion({"Ana": ["Lunes", "Martes", "Miércoles"],"Juan": ["Martes", "Miércoles", "Jueves"],"Pedro": ["Miércoles", "Jueves", "Viernes"]}))
precios = {
    "manzanas": 0.5,
    "bananas": 0.25,
    "naranjas": 0.75
}

carrito = {
    "manzanas": 10,
    "bananas": 5,
    "naranjas": 2
}

def precios(productos:dict,cantidades:dict):
    suma_total = 0
    lista_de_productos = []

    for producto,precio in cantidades.items():
        lista_de_productos.append((producto,precio))
    
    for nombre,valor in lista_de_productos:
        suma_total += productos[nombre]
    return suma_total

# print((precios(precios,carrito)))

#print(carrito["manzanas"])