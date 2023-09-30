""" Ejercicio 1. Escriba una función que, dados una lista desordenada y un elemento:
a) devuelva la cantidad de apariciones del elemento recibido en la lista;
b) busque la primera coincidencia del elemento en la lista y devuelva su posición;
c) utilizando la función anterior, busque todos los elementos que coincidan con el que fue
recibido como parámetro y devuelva una lista con las respectivas posiciones. """

def contador_elem(l: list,n: any):
  x = 0
  cont = 0
  while x < (len(l)):
    if l[x] == n:
      cont += 1
    x+=1
  return cont

# print(contador_elem([9,9,9,9,5,9],9))

def indice(l:list,n:any):
  x = 0
  aux = 0
  while aux != 1 and x < (len(l)):
    x+=1
    if l[x] == n:
      aux += 1
  return x

# print(indice([2,3,9,9,5,9],5))

def search_and_list(l:list,n:any):
  x = 0
  r_list = []
  while x < (len(l)):
    if l[x] == n:
      r_list.append(x)  
    x+=1
  return r_list

# print(search_and_list([2,3,9,9,5,9],9))

""" Ejercicio 2. Escriba una función que tome una lista de números desordenada y:
a) devuelva el valor máximo;
b) devuelva una tupla que incluya el valor máximo y su posición. """

def search_index(l:list):
  
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


# print(search_index([2,3,10,4,5,7]))


""" Ejercicio 3. Escriba una función que tome una lista ordenada y un elemento. Si el elemento
se encuentra en la lista, debe encontrar su posición mediante búsqueda binaria y devolverlo. Si
no se encuentra, debe agregarlo a la lista en la posición correcta y devolver esa nueva posició """

def b_binaria(l: list,e) -> list:
  
  l.sort()
  mitad_l = len(l) // 2
  aux_l = l
  largo = len(aux_l)
  pos_l = list(range(0,largo))
  print(l)
  print(pos_l)
  while largo != 1:
    
    if e >= l[mitad_l] and (largo != 1):
      pos_l = pos_l[mitad_l:]
      aux_l = aux_l[mitad_l:]
      mitad_l = len(aux_l[mitad_l:]) //2

    elif e < aux_l[mitad_l]  and (largo != 1):
      
      pos_l = pos_l[:mitad_l]
      aux_l = aux_l[:mitad_l]
      mitad_l = len(aux_l[:mitad_l]) //2

    largo = len(aux_l)
  # return aux_l[0] == e
  
  if aux_l[0] == e:
    return pos_l[0]
  
  else:
    l.append(e)
    l.sort()
    return b_binaria(l,e)
    
# print(b_binaria([4,1,6,8,5],-1))
""" 
Ejercicio 4. Escriba una función que reciba una lista de tuplas y devuelva un diccionario en
donde las claves sean los primeros elementos de las tuplas y los valores una lista con los
segundos """

def tup_dic(lt: list) -> dict:
  dicc = {}
  for x,y in lt:
    keys = []
    if x in dicc.keys():
      keys = dicc[x]  
    keys.append(y)
    dicc[x] = keys
  return dicc

# print(tup_dic([('Hola','don Pepito'),('Hola','don Jose'),('Buenos','Dias')]))