import pandas as pd

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)

def cuadradoMedio(cantidad_digitos_deseada:int, semilla:int):
    if (cantidad_digitos_deseada <= 0):
        raise Exception("El valor de la cantidad de digitos debe ser mayor a 0")
    elif (semilla <= 0):
        raise Exception("El valor de la semilla debe ser mayor a 0")
    dataframe = pd.DataFrame(columns = ["Xn", "X^2", "Cant Digitos", "Numero ajustado segun 0s", "Parte Central", "Nro Aleatorio"])
    i = 0
    cant_digitos_maxima = len(str((10**cantidad_digitos_deseada - 1) ** 2))

    if(cant_digitos_maxima % 2 != 0):
            cant_digitos_maxima = cant_digitos_maxima + 1
    while True:
        if(i == 0):
            anterior = semilla
            i = 1
        else:
            anterior = dataframe.astype(int).iloc[-1:]["Parte Central"].item()
        numero_cuadrado = anterior**2
        cant_digitos_cuadrado = len(str(numero_cuadrado))
        
        if(cant_digitos_cuadrado <= cant_digitos_maxima):
            diferencia = cant_digitos_maxima - cant_digitos_cuadrado
        
            if (diferencia % 2 == 0):
                cantidad_ceros_adelante = int(diferencia/2)
                cantidad_ceros_atras =  int(diferencia/2)
            else:
                cantidad_ceros_adelante = int(diferencia/2 - 0.5)
                cantidad_ceros_atras =  int(diferencia/2 + 0.5)
                
            ceros_adelante = ""
            for x in range(cantidad_ceros_adelante):
                ceros_adelante = ceros_adelante + str(0)
                
            numero_ajustado = numero_cuadrado * (10 ** cantidad_ceros_atras)
            numero_ajustado = ceros_adelante + str(numero_ajustado)

       
        primer_slice = int((cant_digitos_maxima - cantidad_digitos_deseada)/2)
        segundo_slice = int(cant_digitos_maxima - (cant_digitos_maxima - cantidad_digitos_deseada)/2)
        parte_central = numero_ajustado[ primer_slice: segundo_slice]
        nroAleatorio = int(parte_central)/(10**cantidad_digitos_deseada)
        if nroAleatorio in dataframe["Nro Aleatorio"].values:
            break
        else:
            dataframe = dataframe.append({
                "Xn": anterior,
                "X^2" : numero_cuadrado,
                "Cant Digitos": cant_digitos_cuadrado,
                "Numero ajustado segun 0s": numero_ajustado,
                "Parte Central": int(parte_central),
                "Nro Aleatorio": nroAleatorio
            }, ignore_index = True)
    return dataframe

