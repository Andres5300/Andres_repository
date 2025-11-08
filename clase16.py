#FUNCIONES LAMBDA

add = lambda a, b: a + b
print(add(10,4))

multiply = lambda a, b: a*b
print(multiply(80,5))

# cuadrado de un numero

numbers = range(11)

squared_numbers = list(map(lambda x: x**2, numbers))
print("Cuadrados:", squared_numbers)

#Pares
even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)