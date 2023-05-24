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
Enemy = []
blankSpace = '#'
HowMany = int(1)
Enemy.append(random.randint(1,grid_sizef-1))
Enemy.append(random.randint(1,grid_sizef-1))

def display_game(game, grid_size):
    for i in range(grid_size):
        for j in range(grid_size):
            if i == x and j == y:
                print(f"& ", end='')
            elif i == Enemy[0] and j == Enemy[1]:
                print(f"* ", end='')
            else:
                print(f"{game} ", end='')
        print("")
running = True
clear()
print("En este juego, eres un & y tienes que huir de *, puedes coger . para vencer a *")
Debug = input("Quieres entrar en modo DEBUG, veras cosas--> ")
blankSpace = input("Dime que quieres que sea el espacio en blanco, si lo dejas e blanco sera #--> ")
if blankSpace =="" or blankSpace== " ":
    blankSpace = '#'
while running:
    clear()
    if blankSpace =='&' or blankSpace =='.' or blankSpace =='*':
        print("HARDMODE, Mucha suerte bro")
    display_game(blankSpace, grid_sizef)
    if Debug =="y" or Debug == "Y":
        print("Posicion X jugador: " + str(x))
        print("Posicion Y jugador: " +str(y))
    opc = input("Arriba(w), abajo(s), izquierda(a), derecha(d), sal(q): ")
    if opc == "q" or opc == "Q":
        running = False
    if opc == "w" or opc == "W":
        x -= 1
    if opc == "s" or opc == "S":
        x += 1
    if opc == "a" or opc == "A":
        y -= 1
    if opc == "d" or opc == "D":
        y += 1
    for i in range(HowMany):
        x_EnemyN = x - int(Enemy[0])
        y_EnemyN = y - int(Enemy[1])
        if x_EnemyN > 0:
            x_EnemyN = 1
        elif x_EnemyN < 0:
            x_EnemyN = -1
        if y_EnemyN > 0:
            y_EnemyN = 1
        elif y_EnemyN < 0:
            y_EnemyN = -1
        Enemy[0] += x_EnemyN
        Enemy[1] += y_EnemyN
    if x == Enemy[0] and y == Enemy[1]:
        clear()
        running = False
        print("Has muerto")
