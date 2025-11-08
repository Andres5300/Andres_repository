jugador1 = input("JUGADOR 1 Introduzca piedra, papel o tijera:").lower()
jugador2 = input("JUGADOR 2 Introduzca piedra, papel o tijera:").lower()

if jugador1 == jugador2:
    print("Ambos jugadores sacaron igual")
elif jugador1 == "piedra" and jugador2 == "papel":
    print("Jugador 2 gana")
elif jugador1 == "piedra" and jugador2 == "tijera":
    print("Jugador 1 gana")    
elif jugador1 == "papel" and jugador2 == "piedra":
    print("Jugador 1 gana")    
elif jugador1 == "papel" and jugador2 == "tijera":
    print("Jugador 2 gana")    
elif jugador1 == "tijera" and jugador2 == "piedra":
    print("Jugador 2 gana")        
elif jugador1 == "tijera" and jugador2 == "papel":
    print("Jugador 1gana")      