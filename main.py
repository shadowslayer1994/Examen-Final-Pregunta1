import tkinter as tk
from triangulo import Triangulo


p1 = (50, 150)
p2 = (150, 150)
p3 = (100, 50)

ventana = tk.Tk()
ventana.title("Dibujo de Triángulo")
canvas = tk.Canvas(ventana, width=300, height=300, bg="white")
canvas.pack()

triangulo = Triangulo(p1, p2, p3, relleno="blue", borde="red")
area = triangulo.calcular_area()
perimetro = triangulo.calcular_perimetro()


triangulo.dibujar(canvas)


canvas.create_text(100, 10, text=f"Área: {area:.2f}", fill="black")
canvas.create_text(100, 30, text=f"Perímetro: {perimetro:.2f}", fill="black")

ventana.mainloop()
