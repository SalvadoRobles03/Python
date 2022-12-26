import math


a =["pera", "manzana", "uva", "Kiwi"]
b =["manzana", "Kiwi", "pera", "uva"]
c =[1, 2.39, True, "Tagamandapio"]
d =[int, float, math, len]
e = [1,2,3,4,5,6,7,8,9]
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']

print(len(a))
print(min(a))
print(max(a))

e[0] = 6
print (e, "Modificar el valor de la lista (no se puede hacer con Strings)")

e[0:2] = [78,91,75]
print (e, "Modificar varios valores de la lista")

del e[1]
print(e,"Borrar datos de lista")
e.remove(9)
print(e,"Borrar datos de lista")

e = e + [78,91,75]
print (e, "agregar varios valores a la lista")
e.append(8)
print (e, "agregar varios valores a la lista")
e.extend([78,91,75])
print (e, "agregar varios valores a la lista")
e.insert(4, 789654123)
print (e, "agregar valores a la lista")

print("\n", x[1][1][1], "Llamar valores que estan dentro de una listadentro de otra lista")

print("\n", a==b)

print(a[2],b[0],c[-1], "El negativo es como si contarás la lista al revés")

print(a[0:3], "Pone los valores que estan desde el primer espacio hasta el segundo")

print(d[3](c), "Número de datos dentro de la lista")

print(a[2:0:-2],"agarrar un numero en un rango ")

print(a[::-1],"Los pone al revés")

print("pera" in a, "Checa si está dentro de la lista")

print(a + ["guayaba", "Melón"], "Agrega valores a la lista")

print(a * 2, "Duplica la lista")

