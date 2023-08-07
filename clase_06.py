def dividir (a,b):
    print (a/b)
    return a/b

while True:
    try:
        a = int (input ("Ingrese un número: "))
        b = int (input ("Ingrese otro número: "))
        dividir (a,b)
        break
    except ArithmeticError:
        print ("Ha ocurrido un error aritmético, intente de nuevo")
    except Exception as e:
        print (f"Ha ocurrido un error del tipo {type(e).__name__}, intente de nuevo")

