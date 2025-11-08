#DICCIONARIOS
numbers = {1:"uno",2:"dos",3:"tres"}
print(numbers)
print(numbers[2])
informacion = {"nombre":"Carla",
               "apellido":"Paz",
               "altura":1.70}
print(informacion)
del informacion["altura"]
print(informacion)
claves = informacion.keys()
print(claves)
print(type(claves))
values = informacion.values()
print(values)
print(type(values))
pairs = informacion.items()
print(pairs)

contactos = {"Carla":{
               "apellido":"Paz",
               "altura":1.70},
               "Andres":{
               "apellido":"Herrera",
               "altura":1.80}}

print("Los contactos son" ,contactos)
print("Los datos de carla son" ,contactos["Carla"])