#Listas por comprension
squares = [x**2 for x in range(1,11)]
#print("Cuadrados:", squares)

celsius = [((9/5)* x)+32 for x in range(0,50,10)]
print(celsius)

#pares
evens = [x for x in range(1,20) if x%2 == 0]    
print(evens)

#impares
not_evens = [x for x in range(1,20) if x%2 != 0]    
print(not_evens)