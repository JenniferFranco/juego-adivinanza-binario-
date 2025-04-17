#librerias
import random
from colorama import init, Fore, Style

#desarrollo de funciones

#mensaje de bienvenido al juego e indicaciones
def mostrar_mensajes_iniciales():
    print(f"{Fore.GREEN}¡Bienvenido al Juego de Adivinanza en Binario!{Style.RESET_ALL}")
    print(f"Convertí el siguiente número {Fore.GREEN}binario{Style.RESET_ALL} a {Fore.BLUE}decimal{Style.RESET_ALL}:")

#generar un número decimal al asar 
def generar_numero_secreto ():  
        num_secreto = random.randint(1,10); #establecer limite
        return num_secreto   
    
#transformar el número generado en decimal a binario
def transformar_a_binario(numero_ingresado):
    num_binario = ""  # se inicializa una cadena vacia para ir insertando los números
    dividendo = numero_ingresado
    while dividendo > 0:
        # Obtenemos el resto (0 o 1)
        num_resto = dividendo % 2
# Agregamos ese dígito al principio del resultado convirtiendo num_resto
# en string para poder sumarlo a num_binario
        num_binario = str(num_resto) + num_binario
# Dividimos el número por 2, descartando decimales
        dividendo = dividendo // 2
    return num_binario

#comparar el número secreto y darle ayuda al usuario (si el num es mayor o menor) 
def verificar_intento (num_decimal): 
    num_usuario = 0
    while num_decimal != num_usuario: #camparamos el número ingresado por el usurario con el generado con random
        num_usuario = int(input('¿Qué número crees que es?: '))
        if num_usuario == num_decimal:
            print(f'{Fore.GREEN}¡Acertaste!{Style.RESET_ALL}')
        elif num_usuario > num_decimal:    #ayuda al usuario si el número es menor 
            print(f'{Fore.RED}Incorrecto{Style.RESET_ALL}, el número es menor: ')
        else: #en caso contrario, ayuda al usuario si el número es mayor
            print(f'{Fore.RED}Incorrecto{Style.RESET_ALL}, el número es mayor: ')    
            
#programa principal
mostrar_mensajes_iniciales()
numero_decimal = generar_numero_secreto()
numero_binario = transformar_a_binario(numero_decimal)
print(numero_binario)

numero_usuario = verificar_intento(numero_decimal)
