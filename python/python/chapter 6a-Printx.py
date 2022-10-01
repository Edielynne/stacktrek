def multiplex(n):
    return printx(n)


def printx(n):
    x = "" 
    for i in range(int(n)):
        x = x + "x"
    return x
print(multiplex(5))