#librerias
from colorama import init, Fore, Style


# def mostrar_mensajes_iniciales (): #mensaje de bienvenido al juego y de ingrese número 
    
            


#Inicializar colorama
init()

def mostrar_mensajes_iniciales():
    print(f"{Fore.GREEN}¡Bienvenido al juego!{Style.RESET_ALL}")
    numero = input(f"{Fore.BLUE}Por favor, ingresa un número: {Style.RESET_ALL}")
    
    #Una vez que tenemos un número válido, lo convertimos a entero utilizando int() y lo retornamos
    return int(numero)

#llamamos a la función y mostramos el número ingresado por el usuario
numero_ingresado = mostrar_mensajes_iniciales()
print(f"{Fore.YELLOW}Has ingresado el número: {numero_ingresado}{Style.RESET_ALL}")