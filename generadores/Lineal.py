import pandas as pd

def lineal(a:int, b:int, m:int, semilla:int):
    if(a <= 0 or a>=m):
        raise Exception("El valor de a debe estar comprendido entre 0 y m")
    elif(b < 0 or b>=m):
        raise Exception("El valor de b debe estar comprendido entre 0 y m")
    elif (m <= 0):
        raise Exception("El valor de m debe ser mayor a 0")
    elif (semilla <= 0):
        raise Exception("El valor de la semilla debe ser mayor a 0")
    dataframe = pd.DataFrame(columns = ["Xn+1", "Nro Aleatorio"])
    i = 0
    while True:
        if(i == 0):
            anterior = float(semilla)
            calc_a_b_mod = anterior
            i = 1
        else:
            anterior = dataframe.iloc[-1:]["Xn+1"].item()
            calc_a_b_mod = (a*anterior + b ) % m
        nroAleatorio = calc_a_b_mod/m
        if nroAleatorio in dataframe["Nro Aleatorio"].values:
            break
        else:
            dataframe = dataframe.append({
                "Xn+1" : calc_a_b_mod,
                "Nro Aleatorio": nroAleatorio
            }, ignore_index = True)
    return dataframe