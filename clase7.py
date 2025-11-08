#copiar listas en python sin compartir memoria
a = [1,2,3,4,5]
b = a
print(a)
print(b)
del a[0]
print(a)
print(b)
c = a[:]
print(c)
print("Ubicacion de a", id(a))
print("Ubicacion de b", id(b))
print("Ubicacion de c", id(c))
