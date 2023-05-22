import sys
import os
import random
import math

def clear():
    #print(os.name)
    if os.name == "posix":#linux
        os.system ("clear") 
    elif os.name != "mac":
        os.system ("cls") 
x = 2
y = 2
grid_sizef = 5
x_Enemy = random.randint(1,grid_sizef-1)
y_Enemy = random.randint(1,grid_sizef-1)
blankSpace = '#'
def display_game(game, grid_size):
    for i in range(grid_size):
        for j in range(grid_size):
            if i == x and j == y:
                print(f"& ", end='')
            elif i == x_Enemy and j == y_Enemy:
                print(f"* ", end='')
            else:
                print(f"{game} ", end='')
        print("")
def NextMove():
    newpos = []
    newpos.append(x- x_Enemy)
    newpos.append(y - y_Enemy)
    if newpos[0] > 1:
        newpos[0] = 1
    elif newpos[0] < -1:
        newpos[0] = -1
    if newpos[1] > 1:
        newpos[0] = 1
    elif newpos[1] < -1:
        newpos[1] = -1
    x_Enemy += newpos[0]
    y_Enemy += newpos[1]
    return newpos

running = True
clear()
print("En este juego, eres un & y tienes que huir de *")
Debug = input("Quieres entrar en modo DEBUG, veras cosas--> ")
blankSpace = input("Dime que quieres que sea el espacio en blanco, si lo dejas e blanco sera #--> ")
if blankSpace =="" or blankSpace== " ":
    blankSpace = '#'
arraysa = []
while running:
    clear()
    display_game(blankSpace, grid_sizef)
    if Debug =="y" or Debug == "Y":
        print("Posicion X jugador: " + str(x))
        print("Posicion Y jugador: " +str(y))
        print("Posicion X enemigo: " +str(x_Enemy))
        print("Posicion Y enemigo: " +str(y_Enemy))
        print(arraysa)
    opc = input("Arriba(w), abajo(s), izquierda(a), derecha(d), sal(q): ")
    arraysa = NextMove() #-1 IZQ 1 Der, 
    if opc == "q":
        running = False
    if opc == "w":
        x -= 1
    if opc == "s":
        x += 1
    if opc == "a":
        y -= 1
    if opc == "d":
        y += 1
    if x == x_Enemy and y == y_Enemy:
        clear()
        running = False
        print("Has muerto")
        #sys.exit()
