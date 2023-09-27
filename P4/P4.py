""" Ejercicio 1. Escriba una función que, dados una lista desordenada y un elemento:
a) devuelva la cantidad de apariciones del elemento recibido en la lista;
b) busque la primera coincidencia del elemento en la lista y devuelva su posición;
c) utilizando la función anterior, busque todos los elementos que coincidan con el que fue
recibido como parámetro y devuelva una lista con las respectivas posiciones. """

def contadorelem(l: list,n: any):
  x = 0
  cont = 0
  while x < (len(l)):
    if l[x] == n:
      cont += 1
    x+=1
  return cont

#print(contadorelem([9,9,9,9,5,9],9))

def indice(l:list,n:any):
  x = 0
  aguantemenem = 0
  while aguantemenem != 1 and x < (len(l)):
    x+=1
    if l[x] == n:
      aguantemenem += 1  
  return x

#print(indice([2,3,9,9,5,9],5))

def peron(l:list,n:any):
  x = 0
  juan = []
  while x < (len(l)):
    if l[x] == n:
      juan.append(x)  
    x+=1
  return juan

#print(peron([2,3,9,9,5,9],9))

""" Ejercicio 2. Escriba una función que tome una lista de números desordenada y:
a) devuelva el valor máximo;
b) devuelva una tupla que incluya el valor máximo y su posición. """

def lisandro(l:list):
  
  aux = 0
  mayor = 0
  pos = 0

  for x in range(0,len(l)):
    for y in range(0,len(l)):
      if l[x] > l[y]:
        aux+=1
      if aux == len(l):
        mayor = l[x]
        pos = x
  return (mayor, pos)


print(lisandro([2,3,10,4,5,7]))


""" Ejercicio 3. Escriba una función que tome una lista ordenada y un elemento. Si el elemento
se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posició """