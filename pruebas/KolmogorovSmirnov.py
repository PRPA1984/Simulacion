def testKolmogorov(listaAleatorios:list, estadistico:float):
    #Ordenar
    longitud = len(listaAleatorios)
    listaAleatorios.sort()
    listaAbs = []
    for index in range(longitud):
        if listaAleatorios[index]<=0 or listaAleatorios[index]>=1:
            raise Exception("Todos los numeros aleatorios deben ser mayores a 0 y menores a 1")
        listaAbs.append(abs((index + 1)/longitud - listaAleatorios[index]))
    if max(listaAbs) < estadistico:
        return "Pasa la prueba con un valor de " + str(max(listaAbs))
    else:
        return "No pasa la prueba con un valor de " + str(max(listaAbs))

