from random import randint


""" Ejercicio 1. Escriba una función que, dados una lista desordenada y un elemento:
a) devuelva la cantidad de apariciones del elemento recibido en la lista;
b) busque la primera coincidencia del elemento en la lista y devuelva su posición;
c) utilizando la función anterior, busque todos los elementos que coincidan con el que fue
recibido como parámetro y devuelva una lista con las respectivas posiciones. """

def contador_elem(l: list,n):
	x = 0
	cont = 0
	while x < (len(l)):
		if l[x] == n:
			cont += 1
		x+=1
	return cont

# print(contador_elem([9,9,9,9,5,9],9))

def indice(l:list,n):
	x = 0
	aux = 0
	while aux != 1 and x < (len(l)):
		x+=1
		if l[x] == n:
			aux += 1
	return x

# print(indice([2,3,9,9,5,9],5))

def search_and_list(l:list,n):
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

def b_binaria(l: list,e):
	
	l.sort()
	mitad_l = len(l) // 2
	aux_l = l
	largo = len(aux_l)
	pos_l = list(range(0,largo))
	print(l)
	print(pos_l)
	while largo != 1:
		
		if e >= aux_l[mitad_l] and (largo != 1):
			pos_l = pos_l[mitad_l:]
			aux_l = aux_l[mitad_l:]
			mitad_l = len(aux_l[mitad_l:]) //2

		elif e < aux_l[mitad_l]  and (largo != 1):
			
			pos_l = pos_l[:mitad_l]
			aux_l = aux_l[:mitad_l]
			mitad_l = len(aux_l[:mitad_l]) //2

		largo = len(aux_l)
	
	if aux_l[0] == e:
		return pos_l[0]
	else:
		l.append(e)
		l.sort()
		return b_binaria(l,e)
		
# print(b_binaria([4,1,6,8,5],-1))

def bBin(l: list[int], e: int):
	l.sort()
	i = 0
	f = len(l)
	m = (i +f)//2
	len_list = len(l)
	# print(l)
	while i !=f and l[m] != e:
		# print(m)
		if e > l[m] and (m+1<len_list):
			i = m+1
		else:
			f = m
		m = (i+f)//2
	# print(m)
	return l[m] == e

# print(bBin([1,6,4,2,7],999))

def iBin_Resolucion(l: list, e: int) -> int:
	l.sort() # Agrego esto para que se puedan utilizar listas de numeros desordenadas
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
		#l.insert(i,e)
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
	for x,y in lt:
		if x not in dicc:
			dicc[x] = []
		dicc[x].append(y)
	return dicc
 
print(tup_dic([('Hola','don Pepito'),('Hola','don Jose'),('Buenos','Dias')]))

# Ejercicio 5
# a)
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

# b)
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

# c)
""" 
Escriba una función que reciba una cantidad de iteraciones de una tirada de 2 dados a
realizar y devuelva un diccionario en el cual las claves sean los resultados de la suma de
los dados y los valores sean la cantidad de veces que se observa cada resultado. """

def dados(ct: int) -> dict:
    dicc = {}
    for n in range(ct):
        tirada = []
        for n in range(2):
            tirada.append(randint(1,6))
        print(tirada)
        if (tirada[0]+tirada[1]) in dicc:
            dicc[tirada[0]+tirada[1]] = dicc[tirada[0]+tirada[1]] + 1
        else:
            dicc[tirada[0]+tirada[1]] = 1
    return dicc
            
# print(dados(5))

# Evaluar si se podria realizar de otra forma que no sea utilizando el operador "in", como por ejemplo
# usando la busqueda binaria

