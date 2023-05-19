import sys
import os
import random

def clear():
    #print(os.name)
    if os.name == "posix":#linux
        os.system ("clear") 
    elif os.name != "mac":
        os.system ("cls") 
x = 2
y = 2
grid_sizef = 5
def display_game(game, grid_size):

    for i in range(grid_size):
        for j in range(grid_size):
            if i == x and j == y:
                print(f"& ", end='')
            else:
                print(f"{game} ", end='')
        print("")

running = True
while running:
    clear()
    display_game("#", grid_sizef)
    opc = input("Arriba(w), abajo(s), izquierda(a), derecha(d), sal(q): ")
    if opc == "w":
        x -= 1
    if opc == "s":
        x += 1
    if opc == "a":
        y -= 1
    if opc == "d":
        y += 1
    if x > grid_sizef:
        x = grid_sizef
    if y > grid_sizef:
        y = grid_sizef
    if opc == "q":
        running = False
        #sys.exit()