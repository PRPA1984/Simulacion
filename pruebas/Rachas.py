import math
def testRachas(listaAleatorios:list, estadistico:float):
    listaRachas = list(map(lambda x: "-" if x<= 0.5 else "+",listaAleatorios))
    for index in range(len(listaRachas)):
        if (index == 0):
            b = 1
        elif (listaRachas[index] != listaRachas[index - 1]):
            b = b + 1
    n1 = listaRachas.count("+")
    n2 = listaRachas.count("-")
    n = n1 + n2
    media = 2*n1*n2/n + 0.5
    desvEstandar = math.sqrt((2*n1*n2*(2*n1*n2 - n))/(n**2 *(n - 1)))
    zo = (b - media)/desvEstandar
    if (zo >= abs(estadistico)*(-1) and zo <= abs(estadistico)):
        return "Pasa la prueba con un valor de " + str(zo)
    else: 
        return "No pasa la prueba con un valor de " + str(zo)
        




