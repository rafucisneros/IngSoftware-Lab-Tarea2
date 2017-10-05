'''
Created on 4 oct. 2017

@author: donato
'''
import unittest

from classServicio import Servicio
from classTarifa import Tarifa
from datetime import timedelta, date, datetime
import unittest


class ServicioTest(unittest.TestCase):
    def setUp(self):
        self.s = Servicio()
        self.tarifa = Tarifa(1,2)
    
    def testServicioMinHorasMaxPrecio(self):
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 1, 0, 17)]
        self.assertEquals(2, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'el precio del servicio deberia ser 2')
    
    def testServicioMaxHorasMinPrecio(self):
        tiempoDeServicio = [datetime(2017, 1, 2, 0, 0), datetime(2017, 1, 9, 0, 0)]
        self.assertEquals(216, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'el precio del servicio deberia ser 216')
    
    def testServicioMinHorasMinPrecio(self):
        tiempoDeServicio = [datetime(2017, 1, 2, 0, 0), datetime(2017, 1, 2, 0, 17)]
        self.assertEquals(1, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'el precio del servicio deberia ser 1')
    
    def testServicioMaxHorasMaxPrecio(self):
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 8, 0, 0)]
        self.assertEquals(216, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'el precio del servicio deberia ser 216')
    
    #Las fronteras se dividieron por la entrada de datos en 3 froteras:
    
    #---->Los que cumplen con el limite de tiempo (minimo 15 minutos y maximo 7 dias)
    def testMinTiempo1(self): #solo 15 minutos (deberia ser aprobado)
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 1, 0, 15)]
        self.assertTrue(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema tiempo minimo. El tiempo ingresado deberia ser valido')
    
    def testMinTiempo2(self): #15 minutos + 1minuto (deberia ser aprobado)
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 1, 0, 16)]
        self.assertTrue(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema tiempo minimo. El tiempo ingresado deberia ser valido')
    
    def testMinTiempo3(self): #15 minutos - 1minuto (deberia fallar)
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 1, 0, 14)]
        self.assertFalse(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema tiempo minimo. El tiempo ingresado no deberia ser valido')
    
    def testMaxTiempo1(self): #Servicio la semana completa (deberia aprobar)
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 8, 0, 0)]
        self.assertTrue(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema tiempo maximo. Los dias ingresados deberia ser valido')
    
    def testMaxTiempo2(self): #Servicio de un anio (deberia fallar)
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2018, 1, 1, 0, 0)]
        self.assertFalse(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema tiempo maximo. Revisar periodo entre anio de inicio y fin')
        
    def testMaxTiempo3(self): #Servicio de un mes (deberia fallar)
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 2, 1, 0, 0)]
        self.assertFalse(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema tiempo maximo. Revisar periodo entre mes de inicio y fin')
    
    def testMaxTiempo4(self): #Servicio de una semana menos un dia (deberia aprobar)
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 7, 0, 0)]
        self.assertTrue(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema tiempo maximo. Los dias ingresados deberia ser valido')
    
    def testMaxTiempo5(self): #Servicio de una semana mas un dia (deberia fallar)
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 9, 0, 0)]
        self.assertFalse(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema tiempo maximo. Los dias ingresados no deberian superar los 7 dias')
    
    def testMaxTiempo6(self): #Servicio de una semana y una hora (deberia fallar)
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 8, 1, 0)]
        self.assertFalse(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema tiempo maximo. Las horas ingresadas no deberian superar los 7 dias')
    
    def testMaxTiempo7(self): #Servicio de una semana y un minuto (deberia fallar)
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 8, 0, 1)]
        self.assertFalse(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema tiempo maximo. Los minutos ingresados no deberian superar los 7 dias')
    
    #---->Los que complen con las restricciones de la case tarifa
    def testTarifaNegativa1(self): #Tarifa de dia de semana negativa (deberia fallar)
        self.tarifa.setTarifaDiaSemana(-1)
        self.tarifa.setTarifaFinDeSemana(1)
        self.assertFalse(self.tarifa.verificar(), "Problema con tarifas negativas, 'tarifaDiaSemana' no deberia aceptarse")
    
    def testTarifaNegativa2(self): #Tarifa de fin de semana negativa (deberia fallar)
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(-1)
        self.assertFalse(self.tarifa.verificar(), "Problema con tarifas negativas, 'tarifaFinDeSemana' no deberia aceptarse")
    
    def testTarifaConDecimal1(self): #Verificamos si la tarifa de dia de semana acepta decimales
        self.tarifa.setTarifaDiaSemana(1.11)
        self.tarifa.setTarifaFinDeSemana(1)
        self.assertTrue(self.tarifa.verificar(), "Problema con tarifas decimales, 'tarifaDiaSemana' deberia aceptar decimales")
  
    def testTarifaConDecimal2(self): #Verificamos si la tarifa de fin de semana acepta decimales
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(1.11)
        self.assertTrue(self.tarifa.verificar(), "Problema con tarifas decimales, 'tarifaFinDeSemana' deberia aceptar decimales")
    
    def testTarifaDiferentes1(self): #Caso en el que las tarifa tienen el mismo valor (deberia fallar)
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(1)
        self.assertFalse(self.tarifa.verificar(), 'Problema con funcion verificarDiferente() no deberia aceptar tarifas iguales')
    
    def testTarifaDiferentes2(self): #Caso en el que las tarifas tienes valores distintos
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(2)
        self.assertTrue(self.tarifa.verificar(), 'Problema con funcion verificarDiferente() deberia aceptar tarifas qeu no son iguales')
    
    #---->Los que interactuan con fechas de dia de semana y fin de semana
    
    #Probamos si calcula correctamente un servicio prestado un lunes (deberia dar como resultado la tarifa de dia de semana (1))
    def testServicioDiaSemana(self): 
        tiempoDeServicio = [datetime(2017, 1, 2, 0, 0), datetime(2017, 1, 2, 0, 15)]
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(2)
        self.assertEquals(1, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'el precio del servicio deberia ser 1')
    
    #Probamos si calcula correctamente un servicio prestado un domigo (deberia dar como resultado la tarifa de fin de semana (2))
    def testServicioFinDeSemana(self):
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 1, 0, 15)]
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(2)
        self.assertEquals(2, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'el precio del servicio deberia ser 2')
    
    #Probamos si calcula correctamente un servicio prestado durante todo el fin de semana (deberia dar como resultado 48 horas 
    #multiplicado por la tarifa del fin de semana(48*2 = 96))
    def testServicioTodoFinDeSemana(self):
        tiempoDeServicio = [datetime(2017, 1, 7, 0, 0), datetime(2017, 1, 9, 0, 0)]
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(2)
        self.assertEquals(96, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'Problema con el calculo de horas fin de semana')
    
    #Probamos si calcula correctamente un servicio prestado durante todos les dia de semana (deberia dar como resultado 120 horas 
    #multiplicado por la tarifa de dia de semana(120*1 = 120))
    def testServicioTodoDiaSemana(self):
        tiempoDeServicio = [datetime(2017, 1, 2, 0, 0), datetime(2017, 1, 7, 0, 0)]
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(2)
        self.assertEquals(120, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'Problema con el calculo de horas dia de semana')
    
    #Las esquinas se forman probando los casos en lo sque las fronteras se interceptan (es la combinacion)
    #para estos casos probaremos los mas reelevantes para nosotros
    
    
    #Se verifica que aunque metiendo fechas y horas correctas, si el meterle alguna tarifa negativa entonces falla
    def testServicioTarifaNegativa(self):
        tiempoDeServicio = [datetime(2017, 1, 2, 0, 0), datetime(2017, 1, 7, 0, 0)]
        self.tarifa.setTarifaDiaSemana(-1)
        self.tarifa.setTarifaFinDeSemana(2)
        self.assertFalse(self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'Problema con la interaccion entre calcularServico y verificacion de tarifa negativa')
    
    #Se verifica que aunque se meta fechas y horas correctas, si se le mete tarifas con igual valor etonces fallara
    def testServicioTarifaDiferente(self):
        tiempoDeServicio = [datetime(2017, 1, 2, 0, 0), datetime(2017, 1, 7, 0, 0)]
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(1)
        self.assertFalse(self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'Problema con la interaccion entre calcularServico y verificacion diferencia de tarifa')
    
    #Se verifica qeu la funcion calcule bien cuando se trabaja la seman completa teniendo en cuenta de la diferencia de tarifas
    def testServicioMaxTiempo(self):
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 8, 0, 0)]
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(2)
        self.assertEqual(216, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'Problema con la interaccion entre calcularServico y verificacion de tiempo maximo')
    
    #Se verifica que auque la funcion reciba tarifas adecuadas y fechas existentes, si no cumple con el minimo de minutos requeridos (15min) entonces fallara
    def testServicioMinTiempo(self):
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 1, 0, 14)]
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(2)
        self.assertFalse(self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'Problema con la interaccion entre calcularServico y verificacion de tiempo minimo')
    
    #Se verifica si la funcion calcula perfectamente el pago cuando se trabaja con una tarifa endecimales por un minimo de
    #de tiempo trabajado un fin de semana 
    def testServicioFinDeSemanaConDecimalMinTiempo(self):
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 1, 0, 15)]
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(1.23)
        self.assertEquals(1.23, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'Verificar interaccion entre calculo, fecha, tarifa y tiempo')
    
    #Se verifica si la funcion calcula perfectamente el pago cuando se trabaja con una tarifa endecimales por el maximo de tiempo
    #teniendo en cuanta que unas horas pertenecen al fin de semana y las demas a los dias de semana
    def testServicioMaxTiempoConDecimal(self):
        tiempoDeServicio = [datetime(2017, 1, 1, 0, 0), datetime(2017, 1, 8, 0, 0)]
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(1.23)
        self.assertEquals(179.04, self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'Verificar interaccion entre calculo, fecha, tarifa y tiempo con decimales')
    
    #En cuanto a los casos de malicia tenemos
    
    def testFechaMalicia(self): #Puede que la entrada contenga una fecha de inicio que ocurra despues de la fecha de fin puesta
        tiempoDeServicio = [datetime(2017, 1, 2, 0, 0), datetime(2017, 1, 1, 0, 0)]
        self.assertFalse(self.s.verificarTiempo(tiempoDeServicio[0], tiempoDeServicio[1]), 'Problema con fecha terminada antes de empezar el servicio')
        
    #Verificamos su iteraccion con la funcion principal
    def testFechaMaliciaTotal(self):
        tiempoDeServicio = [datetime(2017, 1, 2, 0, 0), datetime(2017, 1, 1, 0, 0)]
        self.tarifa.setTarifaDiaSemana(1)
        self.tarifa.setTarifaFinDeSemana(1.23)
        self.assertFalse(self.s.calcularPrecio(self.tarifa, tiempoDeServicio), 'Problema en la interracion de fechaFin < fechaInicio con calcularServicio')
    
if __name__ == "__main__":
    #import sys;sys.arg = ['', 'Test.testName]
    unittest.main()
    