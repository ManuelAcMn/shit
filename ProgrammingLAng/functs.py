import sys
import time
varValue = []
varNames = []
varType = []
functions = ["print", "input", "wait", "give", "if", "else"]
operatorsd = ["EQUAL", "NOT EQUAL", "GREATER", "LOWER", "GREATER THAN", "L0WER THAN"]
operatorsimbol = ["==", "!=", ">", "<", ">=", "<="]
on = input("dime el nombre del archivo: ")
print ("-----EXECUTION START-----")
if not on.endswith('.fk'):
    on = on+".fk"
def RaiseError(ErrorMSG):
    print("ERROR: " + ErrorMSG)
    sys.exit()


def LoadVar(var):
    if var.startswith('$'):
        var = var[1:]
        #print(var)
        for d in range(len(varNames)):
            if varNames[d] == var:
                return varValue[d]
        return ""
        #raise RaiseError(var + " is not a variable")
    else:
        raise RaiseError("The variable to load is not a variable/not initialized")

def SaveVar(var, content):
    if var.startswith('$'):
        var = var[1:]
        exis = True
        for i in range(len(varNames)):
            if varNames[i] == var:
                varValue[i] = content
                exis = False
        if exis:
            #Create a new one
            varNames.append(var)
            varValue.append(content)
            if content.isnumeric():
                varType.append("Number")
            elif content == "true" or content=="false":
                varType.append("Boolean")
            else:
                varType.append("Text")

def VarDetecter(text):
    oda = text.split(" ")
    finalPhrase = ""
    for i in oda:
        if i.startswith('$'):
            finalPhrase += LoadVar(i)+" "
        else:
            finalPhrase += i + " "
    return finalPhrase

def ifChanger(text):
    oda = text.split(" ")
    for i in range(len(oda)):
        if oda[i].startswith('$'):
            oda[i] = LoadVar(oda[i])
        else:
            for a in range(len(operatorsd)):
                if oda[i] == operatorsd[a] or oda[i] == operatorsimbol[a]:
                    oda[i] = operatorsd[a]
    print(oda)
    if oda[1] == operatorsd[0]:
        return oda[0] == oda[2]
    
    elif oda[1] == operatorsd[1]:
        return oda[0] != oda[2]
    
    elif oda[1] == operatorsd[2]:
        return oda[0] > oda[2]
        
    elif oda[1] == operatorsd[3]:
        return oda[0] < oda[2]
        
    elif oda[1] == operatorsd[4]:
        return oda[0] >= oda[2]
        
    elif oda[1] == operatorsd[5]:
        return oda[0] <= oda[2]
    
def fun(funct, text):
    if funct == "print":
        print(VarDetecter(text))
    elif funct == "input":
        output = input(VarDetecter(text))
    elif funct == "wait":
        tes = int(0)
        try:
            tes = int(text)
        except:
            raise RaiseError(text + " is not an valid number")
        time.sleep(int(tes))
    elif funct == "give":
        #print(text)
        ds = text.split(" ")
        SaveVar(ds[0], ds[1])
    elif funct == "if":
        booled = ifChanger(text)
        print(booled)
    elif funct == "else":
        print("ElSe")

def lexer(texts):
    s = open(texts)
    lines = s.readlines()
    for j in range(len(lines)):
        i = lines[j]
        lines[j] = i.replace("\n", "")
    for i in lines:
        x = i.split(" ")
        if x[0] in functions:
            fun(x[0], i.replace(x[0]+" ", ""))
        if x[0].startswith('$'):
            LoadVar(x[0])
    print("-----END OF EXECUTION, VARIABLES WERE-----")
    print(varNames)
    print(varValue)
    print(varType)
    s.close()

lexer(on)

