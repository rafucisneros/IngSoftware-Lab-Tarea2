'''
Created on 3 oct. 2017

@author: Rafael Cisneros
'''
from datetime import timedelta
from classTarifa import Tarifa

class Servicio():
    
    def __init__(self):
        pass
    
    # tiempoDeServicio es una tupla donde tiempoDeServicio[0] es la fecha de inicio del servicio
    # y tiempoDeServicio[1] es la fecha de finalizacion del servicio.
    # Las fechas se introducen con el siguiente formato_:
    # Fecha = datetime(año, mes, dia, hora, minutos)
    # Ejemplo
    #fechaInicio = datetime(2017, 10, 1, 0, 0)
    #fechaFin = datetime(2017, 10, 10, 0, 0)
    def calcularPrecio(self, tarifa, tiempoDeServicio):
        horasSemana, horasFinDeSemana = calcularTiempo(tiempoDeServicio[0], tiempoDeServicio[1])
        precio = tarifa.tarifaDiaSemana * horasSemana + tarifa.tarifaFinDeSemana * horasFinDeSemana
        return precio
        
def calcularTiempo(fechaInicio, fechaFin):
    
    diasSemana = [0,1,2,3,4]         # 0 = lunes, 4 = viernes
    finDeSemana = [5,6]              # 5 = sabado, 6 = domingo
    horasDeSemana = 0
    horasFinDeSemana = 0    
    unaHora = timedelta(0,0,0,0,0,1,0)  # timedelta equivalente a una hora

    while fechaInicio < fechaFin:
        if fechaInicio.weekday() in diasSemana:
            horasDeSemana += 1
        elif fechaInicio.weekday() in finDeSemana:
            horasFinDeSemana += 1
        else:
            pass
        fechaInicio += unaHora

    return(horasDeSemana, horasFinDeSemana)