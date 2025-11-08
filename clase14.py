matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]]

transposed = [[row[i] for row in matriz] for i in range(len(matriz[0]))]


print(matriz)
print(transposed)