# librerias
import random

# desarrollo de funciones

# def mostrar_mensajes_iniciales (): #mensaje de bienvenido al juego y de ingrese número

# def generar_numero_secreto ():  #usar math para generar un número al asar

# def transformar_a_binario (): #transformar el número secreto a binario


def transformar_a_binario(numero_ingresado):
    num_binario = ""  # se inicializa y se va armando el numero binario
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


# Programa para probar si funciona "def transformar_a_binario"
decimal = int(input("Ingresa un numero decimal:"))
binario = transformar_a_binario(decimal)
print("El numero binario es ", binario)  # Imprimimos el número invertido

# def verificar_intento (): #comparar el número secreto y darle ayuda al usuario (si el num es mayor o menor)


# #programa principal
# print('Juego de Adivinanza en Binario');
# print('Convertí el siguiente número binario a decimal:')
# num_secreto = random.randint(1,10); #establecer limite
# print(num_secreto)

# num = int(input('¿Qué número crees que es?: '));

# #transformar_a_binario ()

# #verificar_intento ()
