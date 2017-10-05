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
    
if __name__ == "__main__":
    #import sys;sys.arg = ['', 'Test.testName]
    unittest.main()