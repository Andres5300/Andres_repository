#ITERACION Y BUCLES

numbers = [1,2,3,4,5]
for i in numbers:
    print(i)

for i in range(10):
    print(i)    

for i in range(3,10):
    print(i)        

frutas = ["manzana","fresa","uva","durazno"]

for fruta in frutas:
    print(fruta)

x = 0

while x < 5:
    if x == 3:
        break
    print(x)
    x+=1

print("xxxxxx")
numbers = [1,2,3,4,5]
for i in numbers:
    if i == 3:
        continue
    print(i)

