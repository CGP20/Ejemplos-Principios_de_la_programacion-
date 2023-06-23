#Ejemplo de sustitución de Liskov, una estructura sólida y coherente

class Vehiculo: # Define la clase
    def acelerar(self): # Escribe el metodo 
        print("Acelerando el vehículo") # Imprime el metodo 

class Automovil(Vehiculo): # Define la clase
    def acelerar(self): # Escribe el metodo
        print("Acelerando el automóvil") # Imprime el metodo 

def probar_aceleracion(vehiculo):
    vehiculo.acelerar()
    
# Crea una instancia, la llama y la imprime 
vehiculo = Vehiculo()
probar_aceleracion(vehiculo)  # Salida: "Acelerando el vehículo"

automovil = Automovil()
probar_aceleracion(automovil)  # Salida: "Acelerando el automóvil"