# Un año es bisiesto
print (1)
numero = 10
es_par = True
if numero %2 ==0:
    es_par = True
print (es_par)
es_par = numero %2 == 0
#print (es_par)
#year = int (input("Ingresar un año: "))
#
#if year %400 ==0:
#    print (f"El año {year} es bisiesto")
#print (f"El año {year} es bisiesto")

EDAD = int(input("Ingrese edad: "))
NOMBRE = input("Ingrese nombre: ")
VALIDACION = False

if NOMBRE != "****" and EDAD > 5 and EDAD <20 and len(NOMBRE) >= 4 and len(NOMBRE) < 8 and EDAD*3>35:
    VALIDACION = True
    print("Se cumplen las condiciones")
else:
    print("No se cumplen las condiciones")