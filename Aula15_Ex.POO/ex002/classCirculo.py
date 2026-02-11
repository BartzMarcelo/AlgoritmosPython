class Circulo:

    PI= float(3.14159)

    # area = pi r²



    def __init__(self, raio):
        self.raio = raio 

    def calcular_area(self)-> float:
        # Fórmula: Área = π * raio²
        area = Circulo.PI * (self.raio ** 2)
        return area       
        
    def __str__(self)-> str:
        return  f"A área do círculo com raio {self.raio} é {self.calcular_area():.2f}."
