# Importando Libreria
import readchar
# Pedir el nombre del jugador por teclado
nombre_jugador = input("Por favor, introduce tu nombre: ")

# Imprimir un mensaje de bienvenida con el nombre
print("¡Bienvenido,", nombre_jugador + "! Espero que disfrutes jugando.")

# Bucle infinito para precionar teclas
def main():
    while True:
        tecla = readchar.readkey()
        if tecla == readchar.key.UP:  
            break
        print("Tecla presionada:", tecla)

if __name__ == "__main__":
    print("Presiona cualquier tecla. Presiona la tecla ↑ (UP) para terminar.")
    main()
