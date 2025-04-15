#librerias
import random;

#desarrollo de funciones

# def mostrar_mensajes_iniciales (): #mensaje de bienvenido al juego y de ingrese número 

# def generar_numero_secreto ():  #usar math para generar un número al asar
    
# def transformar_a_binario (): #transformar el número secreto a binario
    
def verificar_intento (num_decimal): 
    num_usuario = 0;
    while num_decimal != num_usuario:
        num_usuario = int(input('¿Qué número crees que es?: '))
        if num_usuario == num_decimal:
            print('¡Acertaste!');
        elif num_usuario > num_decimal:    
            print('Incorrecto, el número es menor: ')
        else:
            print('Incorrecto, el número es mayor: ')
         
            
        
            
            
#programa principal
print('Juego de Adivinanza en Binario');
print('Convertí el siguiente número binario a decimal:')
num_secreto = random.randint(1,10); #establecer limite
print(num_secreto)

# num = int(input('¿Qué número crees que es?: ')); 

#transformar_a_binario ()

verificar_intento (num_secreto);