import pandas as pd

def testChiCuadrado(listaAleatorios:list, k:int, estadistico:float):
    intervalos=pd.DataFrame(columns=['Rango', 'Frecuencia Observada', 'Frecuencia Esperada'])
    for x in range(0, k+1):
        if x==0:
            intervalos = intervalos.append({'Rango': 0,
                                            'Frecuencia Observada': 0,
                                            'Frecuencia Esperada': len(listaAleatorios)/k}, ignore_index=True)
        else:
            intervalos = intervalos.append({'Rango': x/k,
                                            'Frecuencia Observada': 0,
                                            'Frecuencia Esperada': len(listaAleatorios)/k}, ignore_index=True)
    for num in listaAleatorios:
        for index,row in intervalos[1:].iterrows():
            if(num>=intervalos.iloc[index - 1]['Rango'] and num < row['Rango']):
                intervalos.iloc[index]['Frecuencia Observada'] += 1
            else:
                continue
    aux_array = []
    for index,row in intervalos[1:].iterrows():
        aux_array.append((row['Frecuencia Observada'].item() - row['Frecuencia Esperada'].item())**2/row['Frecuencia Esperada'].item())
    if sum(aux_array) < estadistico:
        return "Pasa la prueba con un valor de " + str(sum(aux_array))
    else:
        return "No pasa la prueba con un valor de " + str(sum(aux_array))