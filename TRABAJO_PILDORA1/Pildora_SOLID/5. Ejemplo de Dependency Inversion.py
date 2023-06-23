# Ejemplo de Dependency Inversion, depender de abstracciones 
# o interfaces en lugar de depender de implementaciones concretas

class Notificador: # Creo la clase
    def notificar(self, mensaje):
        raise NotImplementedError("Método notificar() no implementado")
# Lanza una excepción para indicar que este método debe ser implementado en las clases derivadas.
class NotificadorEmail(Notificador):
    def notificar(self, mensaje):
        print("Enviando notificación por correo electrónico:", mensaje)

class NotificadorSMS(Notificador):
    def notificar(self, mensaje):
        print("Enviando notificación por SMS:", mensaje)

class Usuario:
    def __init__(self, nombre, notificador):
        self.nombre = nombre
        self.notificador = notificador
    
    def cambiar_notificador(self, notificador):
        self.notificador = notificador
    
    def enviar_notificacion(self, mensaje):
        self.notificador.notificar(mensaje)

# Crean una estancia y Envia una natificacion 
notificador_email = NotificadorEmail()
notificador_sms = NotificadorSMS()

usuario1 = Usuario("Usuario 1", notificador_email)
usuario1.enviar_notificacion("¡Hola Coders!")

usuario2 = Usuario("Usuario 2", notificador_sms)
usuario2.enviar_notificacion("¡Hola Mundo!")

usuario1.cambiar_notificador(notificador_sms)
usuario1.enviar_notificacion("¡Cambiamos de notificador!")