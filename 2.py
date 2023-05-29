import sys
import os
import random
import time

objs = ["Ak-47", "Cuchillo mariposon", "Arco del poder", "Muñequito de ti mismo"]

class Tiradas(object):
    LosQueEntran = []
    Nombres = ""
    def __init__(self, Objs = [32548], NombreBanner= ""):
        if Objs[0] == 32548:
            self.LosQueEntran = []
            for i in range(len(objs)):
                self.LosQueEntran.append(i)
        else:
            self.LosQueEntran = Objs
        self.Nombres = NombreBanner
    def GetName(self):
        return self.Nombres
    def GetObjs(self):
        return self.LosQueEntran

def clear():
    #print(os.name)
    if os.name == "posix":#linux
        os.system ("clear") 
    elif os.name != "mac":
        os.system ("cls")
clear()
tiradasRestantes= int(10)
dinero=int(100)
tiene = []
for i in range(len(objs)):
    tiene.append(False)

#Banners
BannersDisponibles = []
BannersDisponibles.append(Tiradas([32548],"Tirada Estelar"))
BannersDisponibles.append(Tiradas([0, 3],"Tirada Meteorica"))

if os.path.exists("./SavadoGacha.txt"):
    f = open("./SavadoGacha.txt")
    f2 = f.readlines()
    for i in range(len(tiene)):
        tiene[i] = bool(f2[i])
    f.close()
    clear()

def InprimirBanner(tira = int(1)):
    banner = BannersDisponibles[tira-1]
    if tira == 1:
        print("     " + banner.GetName() + "               >")
    elif tira == len(BannersDisponibles):
        print("<    " + banner.GetName() + "                ")
    else:
        print("<    " + banner.GetName() + "               >")
    print("     Puedes conseguir: ", end="")
    on = banner.GetObjs()
    for i in range(len(on)):
        if i == len(on):
            print(objs[on[i]])
        else:
            print(objs[on[i]] + ", ", end="")
    print()
    print("      1.  1 tirada 1 pase")
    print("      2.  10 tirada 8 pase")
    print("      3.  Salir")

def Mostrar(mostrarObjs = True):
    print(str(dinero)+"€                      " + str(tiradasRestantes)+" tiradas restantes")
    if mostrarObjs == True:
        for i in range(len(objs)):
            if tiene[i] == False:
                print(str(i+1) + ". "+objs[i]+ ": no tiene")
            else:
                print(str(i+1) + ". "+objs[i]+ ": tiene")

def TiraYa(BannerTirado = int(0), NumeroTiradas = 1):
    Mostrar(False)
    banner = BannersDisponibles[BannerTirado]
    opciones = banner.GetObjs()
    Salio = random.choice(opciones)
    opciones =objs[Salio]
    print("Obteniste " + opciones)
    tiene[Salio] = True
    print("Quieres guardar datos? ")
    opc = input("Yes/No: ")
    if opc == "yes" or opc == "y" or opc == "Y" or opc == "Yes" or opc == "YES":
        f = open("./SavadoGacha.txt", "w")
        for i in tiene:
            f.write(str(i))
        f.close()
        clear()
    if opc == "no" or opc == "n" or opc == "N" or opc == "No" or opc == "NO":
        1+1
    inicio()

def inicio():
    Mostrar()
    opc = input("Que quieres hacer [1. Comprar tirada, 2. Hacer tirada, 3. salir]: ")
    if opc == "1" or opc == "comprar tirada":
        clear()
        Mostrar(False)
        print("Comprame ezta")
        time.sleep(.5)
        clear()
        inicio()
    
    elif opc == "2" or opc == "hacer tirada":
        clear()
        Tirada = 1
        NoTiro = True
        while NoTiro:
            Mostrar(False)
            #print()
            InprimirBanner(Tirada)
            print("---------------------------------")
            print("a/d - Cambiar banner | s - salir")
            opc = input("Dime que quieres hacer: ")
            if opc == "a" or opc == "A":
                Tirada = Tirada -1
                if Tirada <= 0:
                    Tirada=1
                clear()
            elif opc == "d" or opc == "D":
                Tirada = Tirada +1
                if Tirada > len(BannersDisponibles):
                    Tirada = len(BannersDisponibles)
                clear()
            elif opc == "1":
                NoTiro = False
                clear()
                TiraYa(Tirada-1, 1)
            elif opc == "3" or opc == "salir" or opc == "s" or opc == "S":
                NoTiro = False
                clear()
                inicio()
            else:
                clear()

    elif opc == "3" or opc == "salir" or opc == "s":
        clear()
        Mostrar(False)
        print()
        print("      Seguro/a de que quieres salir?")
        opc = input("      Yes/No: ")
        if opc == "yes" or opc == "y" or opc == "Y" or opc == "Yes" or opc == "YES":
            sys.exit()
        if opc == "no" or opc == "n" or opc == "N" or opc == "No" or opc == "NO":
            inicio()
    else:
        clear()
        Mostrar(False)
        print("Opcion invalida")
        time.sleep(.5)
        clear()
        inicio()

inicio()
