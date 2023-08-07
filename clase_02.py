# CALCULADORA
operacion = 0
while True:
    try:
        numero1 = float (input ("Ingrese un número :"))
        print (numero1)
        break
    except ValueError:
        print ("Ingrese un número válido")
while True:
    try:
        numero2 = float (input ("Ingrese otro número :"))
        print (numero2)
        break
    except ValueError:
        print ("Ingrese un número válido")
while True:
    operador = input ("Ingrese un operador (+, -, *):")
    if operador not in ["+","-","*"]:
        print ("Ingrese un operador válido")
    else:
        break
if operador == "+":
    operacion = numero1 + numero2
elif operador == "-":
    operacion = numero1 - numero2
else:
    operacion = numero1 * numero2
print (f"{numero1} {operador} {numero2} = {operacion}")
