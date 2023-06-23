#Ejemplo de kiss
#lista de los dias de la semana 
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def day_of_week(number): # Creo una variable y su parametro 
    if number < 1 or number > 7: # Verifica si el numero esta fuera del rango (1-7)
        raise ValueError("Invalid day number: " + str(number)) # Lanza un mensaje por si el numero no es valido 
    return days[number - 1] # Rota el nombre de la semana segun el numero

def main():
    print("1- Day 1 is " + day_of_week(1)) # Imprime el nombre del día correspondiente al número 1
    print("2- Day 1 is " + day_of_week(4)) # Imprime el nombre del día correspondiente al número 4

if __name__ == "__main__":
    main() # Llama a la funcion si se está ejecutando directamente como un programa principal