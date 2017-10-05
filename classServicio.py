'''
Created on 4 oct. 2017

@author: donato
'''

from datetime import timedelta, date, datetime
from classTarifa import Tarifa

class Servicio():
    
    def __init__(self):
        pass
    
    # tiempoDeServicio es una tupla donde tiempoDeServicio[0] es la fecha de inicio del servicio
    # y tiempoDeServicio[1] es la fecha de finalizacion del servicio.
    # Las fechas se introducen con el siguiente formato_:
    # Fecha = datetime(anio, mes, dia, hora, minutos)
    # Ejemplo
    #fechaInicio = datetime(2017, 10, 1, 0, 0)
    #fechaFin = datetime(2017, 10, 10, 0, 0)
    def calcularPrecio(self, tarifa, tiempoDeServicio):
        if tarifa.verificar():
            if self.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]):
                horasSemana, horasFinDeSemana = self.calcularTiempo(tiempoDeServicio[0], tiempoDeServicio[1])
                precio = tarifa.tarifaDiaSemana * horasSemana + tarifa.tarifaFinDeSemana * horasFinDeSemana
                return precio
            else:
                #print('Restricciones de timpo violadas')
                return False
        else:
            #print('Restricciones de Tarifa violadas')
            return False
        
    def calcularTiempo(self, fechaInicio, fechaFin):
        
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
    #ime.struct_time((d.year, d.month, d.day, 0, 0, 0, d.weekday(), yday, -1)
    
    #verifico el si es tiempo trabajado esta entra 15minuto y 7 dias
    def verificarTiempo(self, fechaInicio, fechaFin):
        if fechaInicio < fechaFin:
            if fechaInicio.year == fechaFin.year:
                if fechaInicio.month == fechaFin.month:
                    if fechaInicio.day == fechaFin.day:
                        #comprobamos si el tiempo minimo es alcanzado
                        if fechaInicio.hour == fechaFin.hour:
                            if fechaFin.minute - fechaInicio.minute >= 15:
                                return True
                            else:
                                return False
                        else:
                            return True
                    else:
                        #comprobamos si el tiempo maximo no es exedido
                        if fechaFin.day - fechaInicio.day < 7:
                            return True
                        elif fechaFin.day - fechaInicio.day == 7:
                            if fechaFin.hour < fechaInicio.hour:
                                return True
                            elif fechaFin.hour == fechaInicio.hour:
                                if fechaFin.minute <= fechaInicio.minute:
                                    return True
                                else:
                                    return False
                            else:
                                return False
                        else:
                            return False
                else:
                    return False
            else:
                return False
        else:
            return False