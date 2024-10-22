import string #me permite obtener rapidamente los conjuntos de caracteres que existen
import random #nos permite generar numero aleatorios

#print(string.ascii_letters) #devuelve todas las letras del abecedario(menos la Ñ)
#print(string.digits) #nos devuelve numeros del 0 al 9
#print(string.punctuation) #nos devuelve todos los signos

def generar_contraseña(longitud):
    #concatenar todos los caracteres
    caracteres = string.ascii_letters + string.digits 
    contrasena = ""
    for i in range(longitud):
        #hace que por cada iteracion del rango de la longitud ingresada... mediante el random.choice eliga un caracter al azar de "caracteres"
        contrasena += random.choice(caracteres)#elige un caracter al azar, y lo guarda en la variable "contraseña"
    return contrasena

longitud = int(input("Cual es la longitud de la contraseña deseada: ")) #pedimos al usarioa que ingrese un dato

nueva_password = generar_contraseña(longitud)#guardo el resultado de la funcion en una variable

print(f"La contraseña es: {nueva_password}") #muestro el resultado 