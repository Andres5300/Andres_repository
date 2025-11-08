def greet(name, last_name):
    print("Hola", name, last_name)

greet("Andres","Herrera")

#para poner un valor por defecto

def greet(name, last_name = "Sin apellido"):
    print("Hola", name, last_name)

greet("Andres")

