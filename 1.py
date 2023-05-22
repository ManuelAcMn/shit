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
if x_Enemy == x and y_Enemy == y:
    x_Enemy = random.randint(1,grid_sizef-1)
    y_Enemy = random.randint(1,grid_sizef-1)

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
        print("Posicion X enemigo: " +str(x_Enemy))
        print("Posicion Y enemigo: " +str(y_Enemy))
    opc = input("Arriba(w), abajo(s), izquierda(a), derecha(d), sal(q): ")
    x_EnemyN = x - int(x_Enemy)
    y_EnemyN = y - int(y_Enemy)
    if x_EnemyN > 0:
        x_EnemyN = 1
    elif x_EnemyN < 0:
        x_EnemyN = -1
    if y_EnemyN > 0:
        y_EnemyN = 1
    elif y_EnemyN < 0:
        y_EnemyN = -1
    x_Enemy += x_EnemyN
    y_Enemy += y_EnemyN
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
    if x == x_Enemy and y == y_Enemy:
        clear()
        running = False
        print("Has muerto")
