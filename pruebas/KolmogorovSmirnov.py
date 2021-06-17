def testKolmogorov(listaAleatorios:list, estadistico:float):
    #Ordenar
    longitud = len(listaAleatorios)
    listaAleatorios.sort()
    listaAbs = []
    for index in range(longitud):
        listaAbs.append(abs((index + 1)/longitud - listaAleatorios[index]))
    if max(listaAbs) < estadistico:
        return "Pasa la prueba con un valor de " + str(max(listaAbs))
    else:
        return "No pasa la prueba con un valor de " + str(max(listaAbs))

