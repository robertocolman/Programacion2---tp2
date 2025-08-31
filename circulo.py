# -*- coding: utf-8 -*-
"""
Created on Sun Aug 31 13:05:06 2025

@author: nahva
"""

import math

class Circulo:
    PI = math.pi  

    def __init__(self, radio: float):
        self.radio = radio  # en centímetros

    def diametro(self):
        return self.radio * 2

    def perimetro(self):
        return 2 * self.PI * self.radio

    def __eq__(self, other):
        if isinstance(other, Circulo):
            return self.radio == other.radio
        return False
