#Ejemplo de Interface Segregation, dividir las cosas en grupos más pequeños y específicos

class Impresora: # Defino la clase 
    def imprimir(self, documento): #Metodo para imprimir un documento 
        raise NotImplementedError("Método imprimir() no implementado")
    
    def escanear(self): # Metodo para escanear un documento 
        raise NotImplementedError("Método escanear() no implementado")
    
    def enviar_fax(self): # Metodo para enviar un fax
        raise NotImplementedError("Método enviar_fax() no implementado")

class ImpresoraBasica(Impresora): # Defino una clase con su parametro 
    def imprimir(self, documento): # Implemento el metodo 
        print("Imprimiendo el documento:", documento)

class ImpresoraAvanzada(Impresora): # Defino una clase con su parametro 
    def imprimir(self, documento): # Implemento el metodo 
        print("Imprimiendo el documento:", documento)
    
    def escanear(self):# Implemento el metodo 
        print("Escaneando el documento")

impresora_basica = ImpresoraBasica() # Creación de una instancia 
impresora_basica.imprimir("Documento 1")  # Salida: "Imprimiendo el documento: Documento 1"

impresora_avanzada = ImpresoraAvanzada() # Creación de una instancia 
impresora_avanzada.imprimir("Documento 2")  # Salida: "Imprimiendo el documento: Documento 2"
impresora_avanzada.escanear()  # Salida: "Escaneando el documento"