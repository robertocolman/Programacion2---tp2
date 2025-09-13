class Circulo:
    PI = 3.14159

    def __init__(self, radio: float):
        self.radio = radio


    def establecerRadio(self, radio: float):
        self.radio = radio


    def obtenerRadio(self):
        return self.radio

    def obtenerDiametro(self):
        return self.radio * 2
   
    def obtenerArea(self):
        return self.PI * (self.radio ** 2)

    def obtenerPerimetro(self):
        return 2 * self.PI * self.radio