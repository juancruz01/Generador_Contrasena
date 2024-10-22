def suma (a,b):
    return a + b

def resta (a,b):
    return a - b

def multi(a,b):
    return a * b

def division(a,b):
    return a // b

def cuadrado(a,b):
    return a**b


while True:
    try: 
        operacion = int(input("Seleccione la operacion que desea realizar:\n1. Suma\n2. Resta\n3. Multiplicacion\n4. Division\n5. Cuadrado\n "))
        
        if operacion >= 0 and operacion <= 5:
            break
    except:
        print("-----------Ingrese un entero valido----------")



#preguntamos al usuario la operaicon que desea realizar


num1 = float(input("Ingrese el primer numero: "))
num2 = float(input("Ingrese el segundo numero: "))

if operacion == 1:
    resultado = suma(num1,num2)
elif operacion == 2:
    resultado = resta(num1,num2)
elif operacion == 3:
    resultado = multi(num1,num2)
elif operacion == 4:
    resultado = division(num1,num2)
elif operacion == 5:
    resultado = cuadrado(num1,num2)
else:
    print("Operacion no valida")

print(f"El resultado es : {resultado}")