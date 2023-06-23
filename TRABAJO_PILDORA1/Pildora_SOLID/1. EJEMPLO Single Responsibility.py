# EJEMPLOS DE SINGLE RESPONSIBILITY, cada parte del código tiene su responsabilidad

class Empleado: # Creo una clase y una variable
    def __init__(self, nombre, salario):
        self.nombre = nombre # Nombre del empleado
        self.salario = salario # Salario del empleado
    
    def obtener_nombre(self):
        return self.nombre # Devuelve el nombre del empleado
    
    def calcular_salario(self): # Realizar cálculos para obtener el salario dentro de la clase empleado
        return self.salario # Devuelve el salario del empleado 

class CalculadoraSalario:
    def calcular_salario(self, empleado): # Realizar cálculos para obtener el salario dentro de la clase calcular_salario
        return empleado.salario # Devuelve el salario 
    
empleado1 = Empleado("Carol", 800) # Crea la instancia del nombre y salario 
nombre = empleado1.obtener_nombre() # Obtiene el nombre del empleado 
print("Nombre del empleado:", nombre) # Imprime el nombre del empleado

calculadora = CalculadoraSalario() # Crea una instancia del salario 
salario = calculadora.calcular_salario(empleado1) # Obtiene el salario 
print("Salario del empleado:", salario) # Imprime el salario 