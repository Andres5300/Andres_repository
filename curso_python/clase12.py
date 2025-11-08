#Generador
def my_generator():
    yield 1
    yield 2
    yield 3

for value in my_generator():
    print(value)

#Fibonacci
def fibonacci(limit):
    a, b = 0, 1
    while a < limit:
        yield a 
        a, b = b, a+b

for num in fibonacci(10):
    print(num)


#generador_par
def generador_par(limite):
    a = 0
    while a <= limite:
        yield a
        a+=2

for num in generador_par(10):
    print(num)


#generador_inpar
def generador_inpar(limite):
    a = 1
    while a <= limite:
        yield a
        a+=2

for num in generador_inpar(10):
    print(num)    