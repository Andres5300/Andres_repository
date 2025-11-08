#ITERADOR

#Lista
lista = [1,2,3,4]
texto = "Hola Mundo"
iterador = iter(lista)
iterador_texto = iter(texto)

print(next(iterador))
print(next(iterador))
print(next(iterador))
print(next(iterador_texto))
print(next(iterador_texto))

#ejemplo con For

for char in texto:
    print(char)

#crear un iterador para numeros impares
# limite
limit = 10

#crear iterador
odd_iter = iter(range(1,limit+1,2))

#usar iterador
for num in odd_iter:
    print(num)

    