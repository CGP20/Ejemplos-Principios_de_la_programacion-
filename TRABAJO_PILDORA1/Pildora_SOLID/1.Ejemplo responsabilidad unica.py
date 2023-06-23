# Ejemplo de responsabilidad unica 

# Ejemplo de código no DRY
def calcular_area_cuadrado(lado):
    area = lado * lado
    return area

def calcular_perimetro_cuadrado(lado):
    perimetro = 4 * lado
    return perimetro

# Ejemplo de código DRY
def calcular_area_y_perimetro_cuadrado(lado):
    area = lado * lado
    perimetro = 4 * lado
    return area, perimetro

lado = float(input("Ingrese la longitud del lado del cuadrado: "))
area, perimetro = calcular_area_y_perimetro_cuadrado(lado)
print("El área del cuadrado es:", area)
print("El perímetro del cuadrado es:", perimetro)