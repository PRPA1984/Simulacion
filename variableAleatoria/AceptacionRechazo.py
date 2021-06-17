import pandas as pd
from random import random

def aceptacionRechazo(funcion: str, a:int, b:int, M:int, cant_va:int):
    #La funcion es la f(x) como String
    if (a > b):
        raise Exception("El valor de a debe ser menor al valor de b")
    df = pd.DataFrame(columns=['r1', 'r2', 'v.a.x', 'f(x)', 'f(x)/M'])
    for x in range(cant_va):
        while(True):
            r1 = random()
            r2 = random()
            x = a + (b-a) * r1  #Variable Aleatoria
            f_vax = eval(funcion)
            if (r2 <= f_vax/M):
                df = df.append({
                    'r1': r1,
                    'r2': r2,
                    'v.a.x': x,
                    'f(x)': f_vax,
                    'f(x)/M': f_vax/M
                },ignore_index = True)
                break
    return df