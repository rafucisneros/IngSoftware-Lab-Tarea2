'''
Created on 3 oct. 2017

@author: Rafael Cisneros
'''
from datetime import timedelta
from classTarifa import Tarifa

class Servicio():
    
    def __init__(self):
        pass
    
    def calcularPrecio(self, tarifa, tiempoDeServicio):
        precio = 0
        horasSemana, horasFinDeSemana = calcularTiempo(tiempoDeServicio[0], tiempoDeServicio[1])
        precio = tarifa.tarifaDiaSemana * horasSemana + tarifa.tarifaFinDeSemana * horasFinDeSemana
        
def calcularTiempo(fechaInicio, fechaFin):
    
    diasSemana = [0,1,2,3,4]     # 0 = lunes, 4 = viernes
    finDeSemana = [5,6]         # 5 = sabado, 6 = domingo
    horasDeSemana = 0
    horasFinDeSemana = 0    
    unaHora = timedelta(0,0,0,0,0,1,0)

    while fechaInicio < fechaFin:
        if fechaInicio.weekday() in diasSemana:
            horasDeSemana += 1
        elif fechaInicio.weekday() in finDeSemana:
            horasFinDeSemana += 1
        else:
            pass
        fechaInicio += unaHora

    return(horasDeSemana, horasFinDeSemana)