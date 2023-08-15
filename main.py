# Importando Libreria
import readchar

# Pedir el nombre del jugador por teclado
nombre_jugador = input("Por favor, introduce tu nombre: ")

# Imprimir un mensaje de bienvenida con el nombre
print("¡Bienvenido,", nombre_jugador + "! Espero que disfrutes jugando.")

#Precionar Teclas para Moverse por el laberinto
WALL_CHAR = "#"
PATH_CHAR = "."
PLAYER_CHAR = "P"

def convert_to_matrix(maze_string):
    return [list(row) for row in maze_string.split("\n")]

def print_maze(matrix):
    for row in matrix:
        print("".join(row))

def main_loop(matrix, start, end):
    px, py = start
    matrix[py][px] = PLAYER_CHAR
    print_maze(matrix)
    while (px, py) != end:
        key = readchar.readkey()
        if key == readchar.key.UP and py > 0 and matrix[py - 1][px] != WALL_CHAR:
            matrix[py][px] = PATH_CHAR
            py -= 1
        elif key == readchar.key.DOWN and py < len(matrix) - 1 and matrix[py + 1][px] != WALL_CHAR:
            matrix[py][px] = PATH_CHAR
            py += 1
        elif key == readchar.key.RIGHT and px < len(matrix[py]) - 1 and matrix[py][px + 1] != WALL_CHAR:
            matrix[py][px] = PATH_CHAR
            px += 1
        elif key == readchar.key.LEFT and px > 0 and matrix[py][px - 1] != WALL_CHAR:
            matrix[py][px] = PATH_CHAR
            px -= 1
        matrix[py][px] = PLAYER_CHAR
        print("\033[H\033[J")  # Clear the terminal
        print_maze(matrix)

def main():
    maze_string = "...#############\n...............#\n####..####..####\n#..#.....#..#..#\n#..####..#..#..#\n#........#.....#\n####..#######..#\n#..#........#..#\n#..#..#######..#\n#........#.....\n#############.."
    start = (0, 0)
    end = (4, 4)
    
    maze_matrix = convert_to_matrix(maze_string)
    main_loop(maze_matrix, start, end)

if __name__ == "__main__":
    main()

