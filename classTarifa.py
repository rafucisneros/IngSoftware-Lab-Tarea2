'''
Created on 4 oct. 2017

@author: donato
'''


class Tarifa():
    
    def __init__(self, tarifaDiaSemana, tarifaFinDeSemana):
        self.tarifaDiaSemana = tarifaDiaSemana
        self.tarifaFinDeSemana = tarifaFinDeSemana
    
    #Cambio los valores de la tarifa de los dias de semana
    def setTarifaDiaSemana(self, tarifaDiaSemana):
        self.tarifaDiaSemana = tarifaDiaSemana
    
    #cambio los valores de la tarifa del fin de semana
    def setTarifaFinDeSemana(self, tarifaFinDeSemana):
        self.tarifaFinDeSemana = tarifaFinDeSemana
    
    #Verifico qeu la funcion no trabaje con tarifa con montos iguales 
    def verificarDiferencia(self):
        if self.tarifaDiaSemana == self.tarifaFinDeSemana:
            return False
        else:
            return True
    
    #Verifico que la funcion no acepte tarifas negativas
    def verificarNoNegativo(self):
        if self.tarifaDiaSemana >= 0 and self.tarifaFinDeSemana >= 0:
            return True
        else:
            return False
    
    #Verifico que los dos casos anteriores se cumplan
    def verificar(self):
        if self.verificarNoNegativo() and self.verificarDiferencia():
            return True
        else:
            return False