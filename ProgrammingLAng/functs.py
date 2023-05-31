import sys
varValue = []
varNames = []
on = input("dime el nombre del archivo: ")
def RaiseError(ErrorMSG):
    print("ERROR: " + ErrorMSG)
    sys.exit()
def fun(funct, text):
    if funct == "print":
        if text.startswith('$'):
            for d in range(len(varNames)):
                print(d)
        else:
            print(text)
    elif funct == "input":
        output = input(text)
    elif funct == "give":
        print(text)
        ds = text.split(" ")
        if ds[0].startswith('$'):
            varNames.append(ds[0].replace("$", ""))
        else:
            return RaiseError("The variable introduced is not a variable(no $)")
        varValue.append(ds[1])
def lexer(texts):
    s = open(texts)
    functions = ["print", "input", "wait", "give"]
    lines = s.readlines()
    for i in lines:
        x = i.split(" ")
        if x[0] in functions:
            fun(x[0], i.replace(x[0]+" ", ""))

lexer(on)
