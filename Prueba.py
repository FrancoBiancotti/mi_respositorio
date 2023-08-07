# PRUEBA FACTORIAL
def factorial (n):
    factor = 1
    if n == 1:
        factor = 1
    else:
        factor = n * factorial (n-1)
    print (factor)
    return factor
factorial(5)

# PRUEBA FIBONACCI
def fibonacci (n):
    if n == 1 or n == 2:
        resultado = 1
    else:
        resultado = fibonacci (n-1) + fibonacci (n-2)
    return resultado
print (fibonacci (8))

# PRUEBA FIBONACCI 2
def fibonacci_2 (n):
    a,b = 1,1
    for i in range (n-2):
        resultado = a+b
        a = b
        b = resultado
    print (resultado)
    return resultado
print (fibonacci_2 (10))