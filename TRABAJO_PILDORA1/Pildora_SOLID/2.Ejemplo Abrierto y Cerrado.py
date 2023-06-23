# Ejemplo OPEN/CLOSED, el codigo esta abrierto para ampliar y cerrado para modificar

class Forma:
     # Se define un método llamado "calcular_area" en la clase base "Forma".
    def calcular_area(self):
        raise NotImplementedError("Método calcular_area() no implementado")
        # El metodo lanza una excepción lo que indica que este método debe ser implementado en las clases derivadas
    
class Circulo(Forma): # Se crea la clase y hereda la clase anterior
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self): 
        return 3.14159 * self.radio * self.radio # Calcula y devuelve el circulo 

class Rectangulo(Forma):  # Se crea la clase y hereda la clase anterior
    def __init__(self, ancho, altura):
        self.ancho = ancho
        self.altura = altura
    
    def calcular_area(self):
        return self.ancho * self.altura # Calcula y devuelve el rectangulo 

# Ejemplo de uso
circulo = Circulo(5)
area_circulo = circulo.calcular_area()
print("Área del círculo:", area_circulo)

rectangulo = Rectangulo(4, 6)
area_rectangulo = rectangulo.calcular_area()
print("Área del rectángulo:", area_rectangulo)