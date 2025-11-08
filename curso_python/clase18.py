try:
    divisor = int(input("Ingresa un numero divisor "))
    result = 100/divisor
    print(result)
except ZeroDivisionError as e:
    print("Error: El divisor no puede ser cero")
    print("Ha occurido un error", e)
except ValueError as e:
    print("Error: Debes introducir un número valido")        
    print("Ha occurido un error", e)

