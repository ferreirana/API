import time
import json
from loguru import logger
import sympy as sy
from sympy.interactive import init_printing
from service.constants import mensagens
import pandas as pd
import numpy as np



class CalculoService():

    def __init__(self):
        logger.debug(mensagens.INICIO_LOAD_MODEL)
        self.load_model()

    def load_model(self):

        logger.debug(mensagens.FIM_LOAD_MODEL)

    def executar_rest(self, value):
        response = {}

        logger.debug(mensagens.INICIO_PREDICT)
        start_time = time.time()

        response_predicts = self.calculo(value['a'], value['b'], value['c'])
        response_calc = self.integral(value['a'], value['b'], value['c'])

        response = {
                      "Raizes": response_predicts,
                      "Integral": response_calc}
        
        logger.debug(mensagens.FIM_PREDICT)
        logger.debug(f"Fim de todas os calculos em {time.time()-start_time}")

        return response

    def calculo(self, a, b, c):

        logger.debug('Iniciando o calculo...')

        delta = b[0]**2-4*a[0]*c[0]
        if (delta < 0):
            return ('Não existe raízes possiveis.')
        elif (delta == 0):
            response = (-b[0]+np.sqrt(delta))/2*a[0]      
            return round(response, 0)
        elif (delta > 0):
            x1 = (-b[0]+np.sqrt(delta))/2*a[0]
            x2 = (-b[0]-np.sqrt(delta))/2*a[0]    
            return round(x1, 0), round(x2, 0)

    def integral(self, a, b, c):

        logger.debug('Iniciando a integral...')
        init_printing(pretty_print=True)

        x, y, z = sy.symbols('x y z')

        func = x**a[0] * y**b[0] * z**c[0]

        result = sy.diff(func, x)

        return result

