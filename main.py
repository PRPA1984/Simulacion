import traceback

from flask import Flask
from flask import request
from flask_cors import CORS, cross_origin

from generadores.CuadradoMedio import cuadradoMedio
from generadores.Lineal import lineal
from pruebas.ChiCuadrado import testChiCuadrado
from pruebas.KolmogorovSmirnov import testKolmogorov
from pruebas.Rachas import testRachas
from variableAleatoria.AceptacionRechazo import aceptacionRechazo
from variableAleatoria.TIDiscreta import TIDiscreta

app = Flask(__name__)
CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'


@app.route('/generadores/mixto')
@cross_origin()
def generadorMixto():
    try:
        request_data = request.args
        df = lineal(a=int(request_data['a']),
                    b=int(request_data['b']),
                    m=int(request_data['m']),
                    semilla=int(request_data['semilla']))
        return df.to_dict()
    except Exception as e:
        return {'error': e.args[0]},400


@app.route('/generadores/cuadradoMedio')
@cross_origin()
def generadorCM():
    try:
        request_data = request.args
        df = cuadradoMedio(cantidad_digitos_deseada=int(request_data['cantidad_digitos_deseada']),
                           semilla=int(request_data['semilla']))
        return df.to_dict()
    except Exception as e:
        return {'error': e.args[0]},400
@app.route('/pruebas/rachas')
@cross_origin()
def pruebaRachas():
    try:
        request_data = request.args
        string_list=request_data['numeros'].split(',')

        a = testRachas(listaAleatorios=[float(i) for i in string_list],
                          estadistico=float(request_data['estadistico']))
        return {'value': a},200
    except Exception as e:
        traceback.print_exc()
        return {'error': e.args[0]},400
@app.route('/pruebas/Kolmogorov')
@cross_origin()
def pruebaKolmogorov():
    try:
        request_data = request.args
        string_list = request_data['numeros'].split(',')
        a = testKolmogorov(listaAleatorios=[float(i) for i in string_list],
                          estadistico=float(request_data['estadistico']))
        return {'value': a}, 200
    except Exception as e:
        return {'error': e.args[0]}, 400
@app.route('/pruebas/chiCuadrado')
@cross_origin()
def pruebaChiCuadrado():
    try:
        request_data = request.args
        string_list = request_data['numeros'].split(',')
        a = testChiCuadrado(listaAleatorios=[float(i) for i in string_list],
                               k=int(request_data['k']),
                                estadistico=float(request_data['estadistico']))
        return {'value': a}, 200
    except Exception as e:
        return {'error': e.args[0]},400

@app.route('/variableAleatoria/transformadaDiscreta', methods = ['POST'])
@cross_origin()
def transformadaDiscreta():
    try:
        request_data = request.json
        aux_dict = {}
        for x in request_data['dictFrecuencia']:
            aux_dict[x['variableAleatoria']] = int(x['frecuenciaObservada'])
        df = TIDiscreta(dict_va_frecuencia=aux_dict,
                        cant_va=int(request_data['cantVa']))
        return df.to_dict()
    except Exception as e:
        return {'error': e.args[0]},400
@app.route('/variableAleatoria/aceptacionRechazo')
@cross_origin()
def aRechazo():
    try:
        request_data = request.args
        df = aceptacionRechazo(funcion=request_data['funcion'],
                               a=float(request_data['a']),
                               b=float(request_data['b']),
                               M=float(request_data['M']),
                               cant_va=int(request_data['cant_va']))
        return df.to_dict()
    except Exception as e:
        traceback.print_exc()
        return {'error': e.args[0]},400

if __name__ == "__main__":

    app.run(port=9001)