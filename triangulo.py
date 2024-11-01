import math
import tkinter as tk

class Triangulo:
    def __init__(self, p1, p2, p3, relleno="blue", borde="black"):
        self.p1 = p1  
        self.p2 = p2  
        self.p3 = p3  
        self.relleno = relleno  
        self.borde = borde  

    def calcular_area(self):
       
        area = abs((self.p1[0]*(self.p2[1]-self.p3[1]) + self.p2[0]*(self.p3[1]-self.p1[1]) + self.p3[0]*(self.p1[1]-self.p2[1])) / 2)
        return area

    def calcular_perimetro(self):

        lado1 = math.dist(self.p1, self.p2)
        lado2 = math.dist(self.p2, self.p3)
        lado3 = math.dist(self.p3, self.p1)
        return lado1 + lado2 + lado3

    def dibujar(self, canvas):
       
        canvas.create_polygon(
            self.p1, self.p2, self.p3,
            outline=self.borde,
            fill=self.relleno,
            width=2
        )
