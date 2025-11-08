#CLASE_LISTAS
to_do = ["Dirigirnos al hotel",
         "Ir a almorzar",
         "Visitar un museo",
         "Volver al hotel"]

print(to_do)

numbers = [1,2,3,4,5,"seis"]

print(type(numbers)) #tipo
print(len(numbers)) #longitud
print("Primer elemento:" ,numbers[0]) #por posición
print(numbers[0:2]) #slicing
print(numbers[:2]) #slicing #si es cero la posicion de salida se puede omitir
print(numbers[2:]) #slicing #desde el 2 hasta el final
print(numbers[2:-1]) #slicing

numbers.append("nuevo elemento")
print(numbers) 
numbers.insert(1,"segundo elemento")
print(numbers)
print(numbers.index(2))

enteros = [1,2,3,4,65,7]
print("Mayor", max(enteros))
print("Menor", min(enteros))
del numbers[-1]
print(numbers)
del numbers[:2]
print(numbers)
del numbers #se elimina la lista
print(numbers)

